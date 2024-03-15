# -*- coding: utf-8 -*-            
# @Author: 范博洲
import dataclasses
import os
import re
import subprocess
import sys
import threading
import time
from datetime import datetime

from ios_device.cli.base import InstrumentsBase
from ios_device.cli.cli import print_json
from ios_device.remote.remote_lockdown import RemoteLockdownClient
from ios_device.util.utils import convertBytes


class TunnelManager:
    def __init__(self):
        self.start_event = threading.Event()
        self.tunnel_host = None
        self.tunnel_port = None

    def get_tunnel(self):
        def start_tunnel():
            rp = subprocess.Popen([sys.executable, "-m", "pymobiledevice3", "remote", "start-tunnel"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
            while not rp.poll():
                line = rp.stdout.readline().decode()
                line = line.strip()
                if line:
                    print(line)
                if "--rsd" in line:
                    ipv6_pattern = r'--rsd\s+(\S+)\s+'
                    port_pattern = r'\s+(\d{1,5})\b'
                    self.tunnel_host = re.search(ipv6_pattern, line).group(1)
                    self.tunnel_port = int(re.search(port_pattern, line).group(1))
                    self.start_event.set()

        threading.Thread(target=start_tunnel).start()
        self.start_event.wait(timeout=15)


class PerformanceAnalyzer:
    def __init__(self, udid, host, port):
        self.udid = udid
        self.host = host
        self.port = port

    def ios17_proc_perf(self, bundle_id):
        """ Get application performance data """
        proc_filter = ['Pid', 'Name', 'CPU', 'Memory', 'DiskReads', 'DiskWrites', 'Threads']
        process_attributes = dataclasses.make_dataclass('SystemProcessAttributes', proc_filter)

        def on_callback_proc_message(res):
            if isinstance(res.selector, list):
                for index, row in enumerate(res.selector):
                    if 'Processes' in row:
                        for _pid, process in row['Processes'].items():
                            attrs = process_attributes(*process)
                            if name and attrs.Name != name:
                                continue
                            if not attrs.CPU:
                                attrs.CPU = 0
                            attrs.CPU = f'{round(attrs.CPU, 2)} %'
                            attrs.Memory = convertBytes(attrs.Memory)
                            attrs.DiskReads = convertBytes(attrs.DiskReads)
                            attrs.DiskWrites = convertBytes(attrs.DiskWrites)
                            print_json(attrs.__dict__, format)

        with RemoteLockdownClient((self.host, self.port)) as rsd:
            with InstrumentsBase(udid=self.udid, network=False, lockdown=rsd) as rpc:
                rpc.process_attributes = ['pid', 'name', 'cpuUsage', 'physFootprint',
                                          'diskBytesRead', 'diskBytesWritten', 'threadCount']
                if bundle_id:
                    app = rpc.application_listing(bundle_id)
                    if not app:
                        print(f"not find {bundle_id}")
                        return
                    name = app.get('ExecutableName')
                rpc.sysmontap(on_callback_proc_message, 1000)

    def ios17_fps_perf(self):
        """ Get fps data """

        def on_callback_fps_message(res):
            data = res.selector
            print_json({"currentTime": str(datetime.now()), "fps": data['CoreAnimationFramesPerSecond']}, format)

        with RemoteLockdownClient((self.host, self.port)) as rsd:
            with InstrumentsBase(udid=self.udid, network=False, lockdown=rsd) as rpc:
                rpc.graphics(on_callback_fps_message, 1000)


if __name__ == '__main__':
    assert os.geteuid() == 0, "必须使用sudo或管理员权限启动"
    bundle_id = "com.alipay.iphoneclient"
    udid = "00008110-0012148E1E8B801E"
    tunnel_manager = TunnelManager()
    tunnel_manager.get_tunnel()

    performance_analyzer = PerformanceAnalyzer(udid, tunnel_manager.tunnel_host, tunnel_manager.tunnel_port)

    threading.Thread(target=performance_analyzer.ios17_proc_perf, args=(bundle_id,)).start()
    time.sleep(0.1)
    threading.Thread(target=performance_analyzer.ios17_fps_perf).start()

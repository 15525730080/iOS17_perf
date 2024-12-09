# -*- coding: utf-8 -*-            
# @Author: 范博洲
import ctypes
import dataclasses
import os
import platform
import re
import subprocess
import sys
import threading
import time
from datetime import datetime

try:
    import ios_device
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "py_ios_device"])
try:
    import pymobiledevice3
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymobiledevice3"])
from ios_device.cli.base import InstrumentsBase
from ios_device.cli.cli import print_json
from ios_device.remote.remote_lockdown import RemoteLockdownClient
from ios_device.util.utils import convertBytes


class TunnelManager(object):
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
                assert "ERROR Device is not connected" not in line, "ERROR Device is not connected"
                if "--rsd" in line:
                    ipv6_pattern = r'--rsd\s+(\S+)\s+'
                    port_pattern = r'\s+(\d{1,5})\b'
                    self.tunnel_host = re.search(ipv6_pattern, line).group(1)
                    print(self.tunnel_host)
                    self.tunnel_port = int(re.search(port_pattern, line).group(1))
                    print(port_pattern)
                    self.start_event.set()

        threading.Thread(target=start_tunnel).start()
        self.start_event.wait(timeout=30)


class PerformanceAnalyzer(object):
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


def check_admin():
    if platform.system() == "Windows":
        return os.getuid() == 0  # Windows管理员权限检查
    else:  # Linux or macOS
        return os.geteuid() == 0  # Linux/Mac管理员权限检查


def run_with_admin_privileges(command):
    if platform.system() == "Windows":
        # Windows上以管理员权限运行
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit(0)  # 退出当前进程
    else:
        # Linux上使用sudo运行
        subprocess.run(['sudo', sys.executable] + command, check=True)


# 检查是否具有管理员权限
if not check_admin():
    print("没有管理员权限，尝试以管理员权限运行...")
    # 将当前脚本的路径和参数传递给run_with_admin_privileges函数
    run_with_admin_privileges(sys.argv)
    sys.exit()  # 退出当前进程

if __name__ == '__main__':
    udid = ""  # 目标设备
    bundle_id = ""  # 目标app
    if len(sys.argv) >= 3:
        udid = sys.argv[1]
        bundle_id = sys.argv[2]
    tunnel_manager = TunnelManager()
    tunnel_manager.get_tunnel()
    performance_analyzer = PerformanceAnalyzer(udid, tunnel_manager.tunnel_host, tunnel_manager.tunnel_port)
    threading.Thread(target=performance_analyzer.ios17_proc_perf, args=(bundle_id,)).start()
    time.sleep(0.1)
    threading.Thread(target=performance_analyzer.ios17_fps_perf).start()

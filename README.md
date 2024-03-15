# iOS17_perf
ios17以上设备性能统计脚本/IOS 17 and above device performance statistics script

# 使用教程
    pip install -r requirements.txt
<br/>

    修改main.py中的
    bundle_id = "target_app_name"
    udid = "target_ios_udid"
    将bundle_id指向需要测试的app名称，udid指向目标设备
    例如：
    bundle_id = "com.alipay.iphoneclient" #测试支付宝的性能
    udid = "00008110-0012148E1E8B801E"  #ios设备udid、app包名获取获取参见：py-ios-device
<br/>

    sudo python main.py  #执行时需要使用管理员权限/sudo
<br/>

# 示例日志
    (ven) ➜  iOS17_perf git:(main) ✗ sudo python main.py
    2024-03-15 14:32:06 xxxxxxxxxxxxx pymobiledevice3.cli.remote[94700] INFO tunnel created
    UDID: 00008110-0012148E1E8B801E
    ProductType: iPhone14,5
    ProductVersion: 17.2.1
    Interface: utun8
    Protocol: TunnelProtocol.QUIC
    RSD Address: fd05:d8ec:233d::1
    RSD Port: 59102
    Use the follow connection option:
    --rsd fd05:d8ec:233d::1 59102
    2024-03-15 14:32:07 [INFO] [Instrument] base.py[line:291] Sysmontap start ...
    2024-03-15 14:32:07 [INFO] [Instrument] base.py[line:292] wait for data ...
    2024-03-15 14:32:07 [INFO] [Instrument] base.py[line:309] {'global': ['Alloc system memory', 'Allocated PB Size', 'Device Utilization %', 'In use system memory', 'In use system memory (driver)', 'IOGLBundleName', 'recoveryCount', 'Renderer Utilization %', 'SplitSceneCount', 'TiledSceneBytes', 'Tiler Utilization %', 'CoreAnimationFramesPerSecond'], 'process': []}
    2024-03-15 14:32:07 [INFO] [Instrument] base.py[line:310] ['Built-In']
    {'currentTime': '2024-03-15 14:32:07.957304', 'fps': 0}
    {'Pid': 6944, 'Name': 'AlipayWallet', 'CPU': '0 %', 'Memory': '241.00 MiB', 'DiskReads': '562.65 MiB', 'DiskWrites': '1.79 GiB', 'Threads': 65}
    {'currentTime': '2024-03-15 14:32:08.976718', 'fps': 58}
    {'Pid': 6944, 'Name': 'AlipayWallet', 'CPU': '42.39 %', 'Memory': '241.03 MiB', 'DiskReads': '562.66 MiB', 'DiskWrites': '1.79 GiB', 'Threads': 65}
    {'currentTime': '2024-03-15 14:32:09.990906', 'fps': 55}
    {'Pid': 6944, 'Name': 'AlipayWallet', 'CPU': '42.09 %', 'Memory': '241.03 MiB', 'DiskReads': '562.66 MiB', 'DiskWrites': '1.80 GiB', 'Threads': 65}
    {'currentTime': '2024-03-15 14:32:11.002227', 'fps': 59}
    {'Pid': 6944, 'Name': 'AlipayWallet', 'CPU': '41.8 %', 'Memory': '241.03 MiB', 'DiskReads': '562.66 MiB', 'DiskWrites': '1.80 GiB', 'Threads': 65}
    {'currentTime': '2024-03-15 14:32:12.018603', 'fps': 60}
    {'Pid': 6944, 'Name': 'AlipayWallet', 'CPU': '50.16 %', 'Memory': '241.05 MiB', 'DiskReads': '564.55 MiB', 'DiskWrites': '1.80 GiB', 'Threads': 68}

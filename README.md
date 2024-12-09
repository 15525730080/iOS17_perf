# iOS17_perf
ios17以上设备性能统计脚本/IOS 17 and above device performance statistics script

# 使用教程
    python main.py [设备序列号] [目标App包名]
    
    🌰: python main.py 00008110-0012148E1E8B801E com.blizzard.wtcg.cn.hearthstone
<br/>

# 示例日志
    (.venv) ➜  ios17perf python main.py 00008110-0012148E1E8B801E com.blizzard.wtcg.cn.hearthstone
    没有管理员权限，尝试以管理员权限运行...
    2024-12-09 13:08:44 MBP-KVGGXG0W51-0559.local pymobiledevice3.cli.remote[82479] INFO tunnel created
    Identifier: 00008110-0012148E1E8B801E
    Interface: utun6
    Protocol: TunnelProtocol.QUIC
    RSD Address: fdf4:f1a6:2e3b::1
    RSD Port: 62829
    Use the follow connection option:
    --rsd fdf4:f1a6:2e3b::1 62829
    fdf4:f1a6:2e3b::1
    \s+(\d{1,5})\b
    2024-12-09 13:08:44 [INFO] [Instrument] base.py[line:291] Sysmontap start ...
    2024-12-09 13:08:44 [INFO] [Instrument] base.py[line:292] wait for data ...
    2024-12-09 13:08:45 [INFO] [Instrument] base.py[line:309] {'global': ['Alloc system memory', 'Allocated PB Size', 'Device Utilization %', 'In use system memory', 'In use system memory (driver)', 'IOGLBundleName', 'lastRecoveryTime', 'recoveryCount', 'Renderer Utilization %', 'SplitSceneCount', 'TiledSceneBytes', 'Tiler Utilization %', 'CoreAnimationFramesPerSecond'], 'process': []}
    2024-12-09 13:08:45 [INFO] [Instrument] base.py[line:310] ['Built-In']
    {'currentTime': '2024-12-09 13:08:45.297984', 'fps': 0}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '0 %', 'Memory': '1.37 GiB', 'DiskReads': '704.45 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:46.321178', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '42.7 %', 'Memory': '1.37 GiB', 'DiskReads': '704.51 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:47.334497', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '43.75 %', 'Memory': '1.37 GiB', 'DiskReads': '704.51 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:48.342401', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '50.19 %', 'Memory': '1.38 GiB', 'DiskReads': '706.76 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:49.359738', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '47.73 %', 'Memory': '1.37 GiB', 'DiskReads': '717.03 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:50.369925', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '41.6 %', 'Memory': '1.37 GiB', 'DiskReads': '717.12 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:51.381046', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '39.17 %', 'Memory': '1.37 GiB', 'DiskReads': '717.12 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:52.391671', 'fps': 23}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '46.7 %', 'Memory': '1.42 GiB', 'DiskReads': '736.32 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:53.404983', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '41.54 %', 'Memory': '1.43 GiB', 'DiskReads': '741.49 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:54.420073', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '50.12 %', 'Memory': '1.43 GiB', 'DiskReads': '743.91 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:55.428901', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '44.5 %', 'Memory': '1.43 GiB', 'DiskReads': '748.52 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:56.442118', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '44.15 %', 'Memory': '1.44 GiB', 'DiskReads': '755.46 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:57.453149', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '49.49 %', 'Memory': '1.44 GiB', 'DiskReads': '756.84 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:58.464673', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '52.87 %', 'Memory': '1.44 GiB', 'DiskReads': '757.12 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:08:59.481927', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '52.03 %', 'Memory': '1.44 GiB', 'DiskReads': '757.12 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:00.498510', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '47.72 %', 'Memory': '1.44 GiB', 'DiskReads': '760.25 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:01.502441', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '48.05 %', 'Memory': '1.44 GiB', 'DiskReads': '760.81 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:02.507867', 'fps': 29}
    {'currentTime': '2024-12-09 13:09:03.523942', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '51.73 %', 'Memory': '1.44 GiB', 'DiskReads': '761.01 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:04.536615', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '55.57 %', 'Memory': '1.44 GiB', 'DiskReads': '761.01 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:05.546184', 'fps': 25}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '54.68 %', 'Memory': '1.44 GiB', 'DiskReads': '761.01 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:06.557142', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '49.51 %', 'Memory': '1.45 GiB', 'DiskReads': '778.99 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:07.573504', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '53.51 %', 'Memory': '1.45 GiB', 'DiskReads': '779.49 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:08.575214', 'fps': 19}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '50.12 %', 'Memory': '1.44 GiB', 'DiskReads': '780.24 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:09.587172', 'fps': 27}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '83.14 %', 'Memory': '1.43 GiB', 'DiskReads': '806.30 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:10.602388', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '51.26 %', 'Memory': '1.46 GiB', 'DiskReads': '824.71 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:11.614105', 'fps': 22}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '76.58 %', 'Memory': '1.44 GiB', 'DiskReads': '825.29 MiB', 'DiskWrites': '1.23 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:12.627424', 'fps': 22}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '45.45 %', 'Memory': '1.45 GiB', 'DiskReads': '857.84 MiB', 'DiskWrites': '1.24 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:13.628472', 'fps': 8}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '85.24 %', 'Memory': '1.55 GiB', 'DiskReads': '906.93 MiB', 'DiskWrites': '1.24 MiB', 'Threads': 86}
    {'currentTime': '2024-12-09 13:09:14.638304', 'fps': 5}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '51.77 %', 'Memory': '1.65 GiB', 'DiskReads': '974.07 MiB', 'DiskWrites': '1.47 MiB', 'Threads': 87}
    {'currentTime': '2024-12-09 13:09:15.640835', 'fps': 1}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '92.52 %', 'Memory': '1.72 GiB', 'DiskReads': '1013.01 MiB', 'DiskWrites': '1.59 MiB', 'Threads': 87}
    {'currentTime': '2024-12-09 13:09:16.657861', 'fps': 8}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '76.15 %', 'Memory': '1.80 GiB', 'DiskReads': '1.05 GiB', 'DiskWrites': '1.75 MiB', 'Threads': 87}
    {'currentTime': '2024-12-09 13:09:17.661278', 'fps': 28}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '52.1 %', 'Memory': '1.82 GiB', 'DiskReads': '1.06 GiB', 'DiskWrites': '1.76 MiB', 'Threads': 87}
    {'currentTime': '2024-12-09 13:09:18.673871', 'fps': 29}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '51.08 %', 'Memory': '1.82 GiB', 'DiskReads': '1.06 GiB', 'DiskWrites': '1.76 MiB', 'Threads': 87}
    {'currentTime': '2024-12-09 13:09:19.682170', 'fps': 22}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '66.54 %', 'Memory': '1.82 GiB', 'DiskReads': '1.07 GiB', 'DiskWrites': '1.76 MiB', 'Threads': 85}
    {'currentTime': '2024-12-09 13:09:20.686028', 'fps': 30}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '52.21 %', 'Memory': '1.83 GiB', 'DiskReads': '1.07 GiB', 'DiskWrites': '1.76 MiB', 'Threads': 85}
    {'currentTime': '2024-12-09 13:09:21.693173', 'fps': 27}
    {'currentTime': '2024-12-09 13:09:22.697114', 'fps': 22}
    {'Pid': 37027, 'Name': 'hearthstone', 'CPU': '37.52 %', 'Memory': '1.83 GiB', 'DiskReads': '1.08 GiB', 'DiskWrites': '1.78 MiB', 'Threads': 85}

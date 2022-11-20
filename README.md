# 欢迎

[![GitHub release](https://img.shields.io/github/release/academicdog/onmyoji_bot)](https://github.com/AcademicDog/onmyoji_bot/releases) ![GitHub top language](https://img.shields.io/github/languages/top/academicdog/onmyoji_bot) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/academicdog/onmyoji_bot)  ![GitHub repo size](https://img.shields.io/github/repo-size/academicdog/onmyoji_bot)    ![GitHub](https://img.shields.io/github/license/academicdog/onmyoji_bot)   ![platforms](https://img.shields.io/badge/platform-win32|win64-brightgreen.svg) [![GitHub issues](https://img.shields.io/github/issues/academicdog/onmyoji_bot.svg)](https://github.com/academicdog/onmyoji_bot/issues) [![GitHub closed issues](https://img.shields.io/github/issues-closed/academicdog/onmyoji_bot.svg)](https://github.com/academicdog/onmyoji_bot/issues?q=is:issue+is:closed)  ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/academicdog/onmyoji_bot)  ![GitHub contributors](https://img.shields.io/github/contributors/academicdog/onmyoji_bot.svg)

<img align="right" width="300" src="https://raw.githubusercontent.com/AcademicDog/myresource/master/usage.png" alt="copy URL to clipboard" />

本工具用于阴阳师代肝，为各位阴阳师大佬养老护肝所用。

目前已开通项目网站，请访问🌍[此地址](https://academicdog.github.io/onmyoji_bot/)获取最新信息。

同时请访问🌍[此地址](https://doc.onmyojibot.com/zh/latest/)查看用法。

# 紧急通知

```diff
+ 目前纯桌面版已经不太安全，已收到多个封号通知(正在统计，大部分人用的纯桌面版），如果实在要用，请至少带上沙盒或模拟器，用法见说明3.4和5.1章。
- 目前纯桌面版已经不太安全，已收到多个封号通知(正在统计，大部分人用的纯桌面版），如果实在要用，请至少带上沙盒或模拟器，用法见说明3.4和5.1章。
```

# 特别感谢

特别感谢society765在本项目中给与的启发，本项目在其[工作基础](https://github.com/society765/yys-auto-yuhun)上修改完成。

同时感谢sup817ch的图像识别思路，本项目game_ctl模块基于其[工作基础](https://github.com/sup817ch/AutoOnmyoji)。

感谢壁咚咚咚咚咚、Tree.提供的技术指导，感谢Abc为本程序提供了应用图标。

感谢以下人员为测试工作做出的努力：鼠白小验实，忒修斯之旅，Garry，DD斩首, 暖。

# 注意事项

环境：python 3.7, 32 bit；yys PC端 默认分辨率 (1136x640)；yys MuMu模拟器 分辨率（1136x640）；win 10系统，屏幕(1920x1080)。

1. 窗口现在可以完全后台，可以被遮挡，但是**不能最小化**。

2. mumu模拟器需要安卓adb

3. 游戏精细画质，不要开启游戏中的“模型描边”。

4. 当使用高分辨率屏幕时，在阴阳师客户端程序兼容性选项里，不要勾选“替代高DPI缩放行为”，这个选项应该是默认不勾选的。

5. 如果不想安装运行环境，可以访问下载最新已[编译](https://github.com/AcademicDog/onmyoji_bot/releases)版本，该版本有图形界面，同时注意.exe文件和/img文件夹应该放在同一目录后再运行。

# 更新说明
更新日志请点击[这里](https://github.com/AcademicDog/onmyoji_bot/blob/master/CHANGELOG.md)

# 协议 (License)
# mumu模拟器的双开支持问题

Mumu模拟器单开的时候可以使用7555端口连接adb，多开引擎（App多开暂时不知如何获取多开APP的窗口）就没办法逐个窗口连接了。
因为MuMu也是基于vbox魔改来的，vbox原来支持的它也大部分支持，于是查看了vbox的文档，可以自己指定端口映射的命令-如下：
```
C:\Program Files\NemuVbox\Hypervisor\NemuManage.exe" modifyvm "虚拟机对应的名字" --natpf1 "myadb,tcp,,自定义的端口号,,5555
```
主要修改几个引号里面的内容，

第一个NemuManage的路径基本都固定，一般都不需要改。

第二个引号是虚拟机对应的名字，在
MuMu安装目录\emulator\nemu\vms\

里面查看，每个窗口对应一个文件夹，就是文件夹的名字。

（ps：如果你了解sqlite数据库，也可以使用数据库查看工具打开“C:\Users\Public\Documents\MuMu Files\NemuMultiPlayer\config\cache.db”这个数据库，里面就能比较清楚了看到对应的关系。）

第三个就是自定义的端口号了，自己随便取，不要跟已经有的冲突就可以。每个窗口一个。注意mumu模拟器双开时选择多开引擎
示例：
```
"C:\Program Files\NemuVbox\Hypervisor\NemuManage.exe" modifyvm "nemu-6.0-x64-default_1" --natpf1 "myadb,tcp,,8555,,5555"

```
在虚拟机关闭的情况下用cmd执行就可以了。

执行完，开启这个虚拟机，就可以用adb通过自定义的端口（主要不要冲突即没有其他应用占用端口）连接到了。以下命令可以从测试是否完成。
`adb devices`会列出当前连接的设备。
```cmd
adb connect 127.0.0.1:7555
adb connect 127.0.0.1:7555
adb devices
```

这样就可以实现了多个窗口同时用adb控制的功能。



该源代码使用了 [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) 开源协议。

This project is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license.
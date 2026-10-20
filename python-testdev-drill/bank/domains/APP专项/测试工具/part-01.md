# APP专项 · 测试工具

> 共 42 题 · 所属领域：APP专项 · 专题：测试工具

---

## Q006802

- 题型：简答
- 难度：入门

**题目**

```text
ADB 的命令常见的有哪些？
```

**答案**

```text
adb connect、adb devices、adb pull/push、adb shell、adb logcat
```

**解析**

```text
【核心考点】 ADB命令 Android测试
【题目解析】
本题考察Android Debug Bridge（ADB）的常用命令，这是移动测试的基础知识。ADB用于与Android设备通信，支持设备管理、文件传输、日志查看等操作。
【参考答案要点】
1. adb connect：连接远程设备（如模拟器或真机）。
2. adb devices：列出已连接的设备列表。
3. adb pull/push：从设备拉取文件或向设备推送文件。
4. adb shell：进入设备的Linux shell环境。
5. adb logcat：查看设备日志。
【面试角度】
回答时建议补充实际使用场景，例如“使用adb logcat过滤特定日志用于调试”，能展示实战经验。
【易错提示】
容易遗漏adb connect或adb shell等命令，面试中可能要求解释adb install和adb uninstall。
```

---

## Q006807

- 题型：简答
- 难度：入门

**题目**

```text
adb 可以用在ios手机上不？
```

**答案**

```text
不可以，是Android 调试工具
```

**解析**

```text
【核心考点】 ADB工具 移动测试平台
【题目解析】
本题考查ADB工具的适用范围。ADB（Android Debug Bridge）是专为Android设备设计的调试工具，用于与Android模拟器或真机通信，不兼容iOS系统。
【参考答案要点】
不可以。ADB是Android调试工具，仅适用于Android设备。iOS设备使用Xcode或libimobiledevice等工具进行调试。
【面试角度】
回答时明确区分Android和iOS测试工具链，体现对移动测试生态的理解。
【易错提示】
不要混淆ADB与通用调试工具，iOS有独立的调试体系。
```

---

## Q006808

- 题型：简答
- 难度：入门

**题目**

```text
adb 如何连接手机
```

**答案**

```text
参考：
adb connect 设备号
```

**解析**

```text
【核心考点】 ADB命令 设备连接
【参考答案要点】
1. 确保环境：已安装ADB工具并配置环境变量，手机开启开发者模式和USB调试。
2. 连接命令：使用adb connect 设备IP地址:端口号（默认端口5555）。例如：adb connect 192.168.1.100:5555。
3. 验证连接：执行adb devices查看设备列表，确认状态为"device"。
4. 注意事项：确保手机和电脑在同一网络；若连接失败，可尝试重启ADB服务（adb kill-server后adb start-server）。
【面试角度】
这是基础操作题，面试官期望你清晰描述步骤，并提及常见问题（如端口占用、驱动缺失）的解决方法。
【延伸知识】
ADB支持USB和无线两种连接方式。无线连接需先通过USB连接并执行adb tcpip 5555开启端口。此外，adb shell可进入设备终端进行高级调试。
```

---

## Q006809

- 题型：简答
- 难度：入门

**题目**

```text
adb命令?
```

**答案**

```text
adb connect、adb devices、adb pull/push、adb shell、adb logcat
```

**解析**

```text
【核心考点】 adb命令 Android测试
【参考答案要点】
常用的adb命令包括：
1. adb connect：连接远程设备或模拟器，如adb connect 127.0.0.1:5555。
2. adb devices：列出当前连接的设备列表。
3. adb pull/push：从设备拉取文件到本地（pull）或推送文件到设备（push）。
4. adb shell：进入设备的Linux shell环境，可执行各种命令。
5. adb logcat：查看设备日志，常用于调试和问题定位。
【面试角度】
面试官通常期望你至少说出3-5个常用命令，并简要说明其用途。如果能结合实际项目场景举例，如“使用adb logcat抓取崩溃日志”或“使用adb pull导出数据库文件”，会更有说服力。
【延伸知识】
adb命令是Android测试的基础工具，还可用于安装/卸载应用（adb install/uninstall）、模拟按键（adb shell input keyevent）、截屏（adb shell screencap）等，建议系统掌握。
```

---

## Q006810

- 题型：简答
- 难度：入门

**题目**

```text
adb命令了解吗？
```

**答案**

```text
adb connect、adb devices、adb pull/push、adb shell、adb logcat
```

**解析**

```text
【核心考点】 adb命令 移动测试基础
【题目解析】
本题考查Android调试桥（adb）的基本命令，是移动测试的必备技能。adb用于连接设备、传输文件、执行shell命令和查看日志，是测试工程师日常工作中频繁使用的工具。
【参考答案要点】
1. 连接设备：adb connect <设备IP>用于无线连接，adb devices列出已连接设备。
2. 文件传输：adb pull <远程路径> <本地路径>从设备拉取文件，adb push <本地路径> <远程路径>推送文件到设备。
3. shell命令：adb shell进入设备终端，可执行Linux命令如ls、pm等。
4. 日志查看：adb logcat实时查看系统日志，常用-s过滤标签。
【面试角度】
回答时可补充实际应用场景，例如“使用adb install安装测试包，adb uninstall卸载应用，adb shell dumpsys获取系统服务信息”。同时可提及adb在自动化测试中的集成，如Appium底层依赖adb。
【延伸知识】
adb还支持截屏（screencap）、录屏（screenrecord）、模拟按键（input keyevent）等，掌握这些命令能提升测试效率。
```

---

## Q006811

- 题型：简答
- 难度：入门

**题目**

```text
adb命令熟悉吗？如果是要获取device的id要用adb的哪个命令？
```

**答案**

```text
熟不熟悉实话实说，但是adb devices这个命令肯定不能忘记
```

**解析**

```text
【核心考点】 adb命令 Android测试
【参考答案要点】
1. 常用adb命令：包括 adb devices（列出设备）、adb install（安装应用）、adb logcat（查看日志）、adb shell（进入设备终端）等。
2. 获取设备ID：使用 adb devices 命令，输出中会显示设备的序列号（即设备ID）。例如，执行后返回 List of devices attached 及设备ID。
【面试角度】
回答时应诚实说明熟悉程度，但必须掌握 adb devices 等基础命令。可补充在多设备测试中如何通过 -s 选项指定设备ID，体现实际应用能力。
【易错提示】
注意 adb devices 仅显示已连接的设备，若设备未授权或驱动问题可能不显示。面试中常考察 adb kill-server 和 adb start-server 的故障排查。
```

---

## Q006815

- 题型：简答
- 难度：入门

**题目**

```text
android中，adb桥接，把电脑图片拷贝到手机的指令和把手机图片拷到电脑的指令？
```

**答案**

```text
adb push xxx.png /sdcard/
adb pull /sdcard/xxx.png D:\
```

**解析**

```text
【核心考点】 ADB命令 文件传输
【题目解析】
本题考查Android调试桥（ADB）中文件传输的基本命令。ADB提供了push和pull命令用于在电脑和手机之间传输文件，是移动测试中常用的基础操作。
【参考答案要点】
1. 电脑图片拷贝到手机：使用adb push命令，语法为adb push 本地文件路径 手机目标路径。示例：adb push xxx.png /sdcard/。
2. 手机图片拷贝到电脑：使用adb pull命令，语法为adb pull 手机文件路径 电脑目标路径。示例：adb pull /sdcard/xxx.png D:\。
【面试角度】
回答时建议补充权限问题和路径注意事项，例如“如果手机路径需要root权限，可能需要先执行adb root命令”，能体现对实际操作的深入理解。
【延伸知识】
ADB还支持adb install安装应用、adb shell进入设备终端等命令，掌握这些命令有助于提升移动测试效率。
```

---

## Q006823

- 题型：简答
- 难度：入门

**题目**

```text
在android设备中，使用adb命令提取文件，插入文件，提取系统日志的命令分别为什么
```

**答案**

```text
adb pull
adb push
adb logcat
```

**解析**

```text
【核心考点】 ADB命令 Android测试
【题目解析】
本题考查Android调试桥（ADB）的基础命令，是移动端测试工程师的必备技能。ADB用于与Android设备通信，执行文件操作、日志查看、安装应用等任务。
【参考答案要点】
1. 提取文件：adb pull <设备路径> <本地路径>，例如 adb pull /sdcard/test.txt ./ 将设备中的test.txt文件提取到当前目录。
2. 插入文件：adb push <本地路径> <设备路径>，例如 adb push ./test.txt /sdcard/ 将本地文件推送到设备。
3. 提取系统日志：adb logcat 命令用于实时查看设备日志，常用参数包括 -d（一次性输出日志）和 -v time（显示时间戳）。
【面试角度】
回答时建议补充实际应用场景，例如“在测试中，我常用 adb logcat | grep Error 过滤错误日志，或者用 adb pull /data/anr/traces.txt 提取ANR日志”。
【易错提示】
注意 adb pull 和 adb push 的路径顺序：第一个参数是源路径，第二个是目标路径。另外，提取系统日志时，可能需要先执行 adb root 获取权限。
```

---

## Q006837

- 题型：简答
- 难度：入门

**题目**

```text
现在大家都用什么软件双开测试？
```

**答案**

```text
现在有部分国产android ROM自带双开功能，同时我们也可以使用第三方提供的应用或者开源项目，比如像：LBE平行空间，GO双开，DualSpace等等
```

**解析**

```text
【核心考点】 应用双开 测试工具
【参考答案要点】
1. 系统自带双开：部分国产Android ROM（如MIUI、EMUI、ColorOS等）内置应用双开功能，可直接在设置中开启。
2. 第三方应用：如LBE平行空间、GO双开、DualSpace、Parallel Space等，支持大多数应用双开。
3. 开源方案：基于Android多用户或Work Profile的开源项目，如Island、Shelter等，提供更安全的双开环境。
【面试角度】
回答时建议说明双开测试的常见场景，如社交账号多开、游戏小号测试等，并提及兼容性风险（如某些应用检测双开环境导致封号）。
【易错提示】
注意区分双开与多开（多开通常指同时运行多个实例），双开工具可能影响应用稳定性或隐私安全，测试时需关注。
```

---

## Q006840

- 题型：简答
- 难度：入门

**题目**

```text
请写出实现下列功能的adb命令: 通过adb命令上传e盘下面的file文件到sdcard卡
```

**答案**

```text
adb push e:\file /sdcard
```

**解析**

```text
【核心考点】 ADB命令 文件传输
【题目解析】
本题考查Android调试桥（ADB）中文件上传命令的使用。adb push命令用于将本地文件上传到Android设备指定路径。参考答案正确给出了命令格式。
【参考答案要点】
adb push e:\file /sdcard
【面试角度】
面试中可能追问adb pull命令（从设备下载文件）以及权限问题（如/sdcard路径需可写）。
【易错提示】
注意Windows路径使用反斜杠，但ADB命令中路径分隔符建议使用正斜杠或双反斜杠，以避免转义问题。例如adb push e:/file /sdcard更通用。
```

---

## Q006841

- 题型：简答
- 难度：入门

**题目**

```text
请写出实现下列功能的adb命令: 通过adb命令从sdcard中获取file文件到e盘
```

**答案**

```text
adb pull /sdcard/file e:\
```

**解析**

```text
【核心考点】 ADB命令 文件传输
【题目解析】
本题考察ADB（Android Debug Bridge）中从设备拉取文件到本地的命令。ADB是Android开发和测试中常用的工具，用于调试和文件管理。
【参考答案要点】
正确的ADB命令为：adb pull /sdcard/file e:\
其中：
adb pull：从设备拉取文件的命令。
/sdcard/file：设备上的源文件路径。
e:\：本地目标路径（Windows格式，注意使用双反斜杠）。
【面试角度】
面试中可能还会问到adb push（推送文件到设备）和adb shell等命令，建议熟悉常用ADB操作。
【易错提示】
注意路径分隔符：Windows使用反斜杠，Linux/Mac使用正斜杠。另外，确保设备已连接并授权。
```

---

## Q006805

- 题型：简答
- 难度：简单

**题目**

```text
IOS的命令 了解过吗 ?
```

**答案**

```text
在iOS中，常用的命令包括：
1. ls - 列出当前目录中的文件和文件夹。
2. cd - 切换到另一个目录。
3. mkdir - 创建一个新的目录。
4. rm - 删除文件或目录。
5. cp - 复制文件或目录。
6. mv - 移动或重命名文件或目录。
7. pwd - 显示当前目录的路径。
8. ssh - 通过SSH连接到另一台计算机。
要在iOS设备上执行命令，您需要通过终端或SSH连接进行操作。一些常见的用于操作iOS设备的命令包括：
1. ssh - 通过SSH连接到iOS设备。
2. scp - 从iOS设备复制文件到另一台计算机或从另一台计算机复制文件到iOS设备。
3. ideviceinstaller - 安装和卸载iOS应用程序。
4. idevicescreenshot - 捕获iOS设备的屏幕截图。
5. idevicesyslog - 显示iOS设备的系统日志。
6. iproxy - 转发iOS设备的端口。
7. idevicediagnostics - 运行iOS</f
```

**解析**

```text
【核心考点】 iOS 基础命令 移动端测试
【题目解析】
本题考查对 iOS 设备常用命令行操作的了解。在 iOS 测试中，通过终端或 SSH 连接设备执行命令是常见的调试和自动化手段。题目中列出的命令涵盖了文件管理（ls、cd、mkdir、rm、cp、mv）、路径查看（pwd）和远程连接（ssh、scp）等基本操作。
【参考答案要点】
1. 文件操作命令：ls（列出目录）、cd（切换目录）、mkdir（创建目录）、rm（删除）、cp（复制）、mv（移动/重命名）、pwd（显示当前路径）。
2. 远程连接命令：ssh（远程登录设备）、scp（安全复制文件）。
3. 执行环境：通过终端直接操作或 SSH 连接至越狱设备。
【面试角度】
回答时建议结合实际测试场景，例如“在 iOS 自动化测试中，常用 scp 将测试脚本传输到设备，再用 ssh 执行”，能体现实践能力。
【易错提示】
注意 iOS 命令与 Linux 命令相似但环境受限，非越狱设备无法直接使用这些命令，面试时需明确说明前提条件。
```

---

## Q006806

- 题型：简答
- 难度：简单

**题目**

```text
adb shell 的作用是什么
```

**答案**

```text
adb shell 可以进入手机系统的交互界面，安卓手机系统是一个 linux 发行版，大多数 linux 通用操作都可以在 adb shell 中输入。
```

**解析**

```text
【核心考点】 ADB命令 移动端测试基础
【参考答案要点】
adb shell 用于在电脑端通过ADB（Android Debug Bridge）进入Android设备的Linux Shell环境。其作用包括：1. 执行Linux命令：如文件操作、进程管理、网络配置等；2. 调用系统服务：如查看日志（logcat）、模拟按键（input keyevent）、截图（screencap）等；3. 调试应用：如启动Activity、发送广播、查看数据库等。它是移动端测试和开发的重要工具。
【面试角度】
面试官通过此问题考察候选人对移动端测试基础工具的掌握程度。回答时应突出adb shell的实用场景，例如用于自动化测试中的设备控制、日志分析等。
【延伸知识】
adb shell是ADB工具的核心命令之一，常与adb devices、adb install、adb logcat等配合使用。在Appium自动化测试中，adb shell也常用于执行一些系统级操作，如清除应用数据、修改系统设置等。
```

---

## Q006812

- 题型：简答
- 难度：简单

**题目**

```text
adb命令，怎么看APP日志
```

**答案**

```text
adb logcat | findstr app进程号
```

**解析**

```text
【核心考点】 adb 命令 日志查看
【题目解析】
本题考查使用 adb 命令查看 Android 应用日志的方法。adb logcat 是 Android 调试桥提供的日志查看工具，通过过滤进程 ID 可以快速定位特定应用的日志输出。
【参考答案要点】
1. 命令格式：adb logcat | findstr [进程号]，在 Windows 下使用 findstr 过滤，Linux/Mac 使用 grep。
2. 获取进程号：先执行 adb shell ps | findstr [包名] 或 adb shell pidof [包名] 获取目标应用的 PID。
3. 其他常用过滤：按日志级别过滤（如 adb logcat *:E 只显示错误），按标签过滤（如 adb logcat -s TAG）。
4. 进阶用法：使用 adb logcat -v time 显示时间戳，或 adb logcat -b crash 查看崩溃日志。
【易错提示】
注意 Windows 下使用 findstr 而非 grep，且进程号需实时获取（应用可能重启导致 PID 变化）。面试中常考察如何同时过滤多个条件。
```

---

## Q006813

- 题型：简答
- 难度：简单

**题目**

```text
adb覆盖安装命令?
```

**答案**

```text
覆盖低版本APK
Android设备有更小版本Apk，进行覆盖安装：adb install -r xx.apk

覆盖高版本
Android设备有更高版本Apk，进行覆盖安装:adb install -r -d
adb install -r -d C:\Users\temp\xiaomi_highger.apk
```

**解析**

```text
【核心考点】 ADB命令 覆盖安装
【题目解析】
本题考查Android调试桥（ADB）中覆盖安装命令的使用。覆盖安装是移动测试中验证版本升级兼容性的常用操作，需区分低版本覆盖高版本和高版本覆盖低版本的参数差异。
【参考答案要点】
1. 覆盖低版本APK：使用adb install -r xx.apk，其中-r参数表示替换已存在的应用。
2. 覆盖高版本APK：使用adb install -r -d xx.apk，其中-d参数允许降级安装（即用低版本覆盖高版本）。
【面试角度】
面试中常结合版本兼容性测试提问，建议回答时补充说明-r和-d参数的区别，并强调降级安装需在开发者选项中开启“允许降级安装”权限。
【易错提示】
注意降级安装时-d参数必须与-r同时使用，单独使用-d无效；另外，部分厂商系统可能限制降级安装。
```

---

## Q006816

- 题型：简答
- 难度：简单

**题目**

```text
app的日志如何抓取?
```

**答案**

```text
app本身的日志，可以用logcat抓取
adb logcat >d:\hello.txt
也可以用ddms抓取，手机连上电脑，打开ddms工具，或者在Android Studio开发工具中，打开DDMS
```

**解析**

```text
【核心考点】 移动测试 日志抓取
【参考答案要点】
抓取App日志的常用方法包括：
1. 使用adb logcat命令：通过命令行执行adb logcat > d:\hello.txt，将日志输出到文件。
2. 使用DDMS工具：连接手机后，打开DDMS（在Android Studio中可通过Tools > Android > DDMS访问），在LogCat面板中查看和保存日志。
3. 使用Android Studio的Logcat窗口：直接集成在开发环境中，支持过滤和搜索。
【题目解析】
本题考查移动测试中日志抓取的基本技能。adb logcat是最常用的命令行方式，而DDMS和Android Studio提供图形化界面，便于实时查看和过滤。
【面试角度】
面试官可能追问如何过滤特定进程或标签的日志，例如adb logcat -s TAG_NAME。建议结合实际测试经验说明日志分析在定位崩溃或性能问题中的作用。
【易错提示】
常见错误包括：忘记开启USB调试模式导致无法连接；未指定输出文件路径导致日志丢失；混淆logcat与系统日志工具。
```

---

## Q006817

- 题型：简答
- 难度：简单

**题目**

```text
fiddler怎么抓安卓的请求
```

**答案**

```text
1) 保证安装手机跟电脑端同一个网络
2）fiddler-options里面要设置代理端口及开启远程访问
3）手机端设置代理，输入电脑端ip、及端口号
```

**解析**

```text
【核心考点】 抓包工具 Fiddler 移动端测试
【参考答案要点】
1. 确保网络连通：手机和电脑连接同一局域网（同一Wi-Fi网络）。
2. 配置Fiddler：打开Fiddler，选择菜单 Tools → Options → Connections，勾选“Allow remote computers to connect”，设置代理端口（默认8888），点击OK。
3. 手机端设置代理：在手机Wi-Fi设置中，选择当前网络，设置代理为“手动”，输入电脑的IP地址和Fiddler的端口号（如192.168.1.100:8888）。
4. 安装证书（可选）：如需抓取HTTPS请求，需在手机浏览器访问 http://电脑IP:端口号，下载并安装Fiddler根证书。
【面试角度】
回答时强调排错思路，例如“如果抓不到包，先检查网络连通性，再确认代理设置是否正确”，体现问题解决能力。
【延伸知识】
Fiddler也支持iOS和模拟器抓包，原理相同。其他抓包工具如Charles、Wireshark也有类似配置。
```

---

## Q006818

- 题型：简答
- 难度：简单

**题目**

```text
什么是adb命令？adb命令有哪些
```

**答案**

```text
adb即Android Debug Bridge（安卓调试桥），
常用命令如下：
adb --help / adb :看见帮助信息
adb start-server:启动 adb 服务
adb kill-server:关闭 adb 服务
adb devices:查看手机设备号
adb shell getprop ro.build.version.release:获取系统版本
adb push 电脑 手机
adb pull 手机 电脑
adb logcat | grep(unix) 包名
adb logcat | findstr(win) 包名
adb shell :进入 shell 命令行，可以操作 Linux 命令
adb shell dumpsys window windows | grep mFocusedApp:获取包名 启动名(win：adb shell dumpsys
window windows | findstr mFocusedApp)
adb install 路径/apk 文件:安装 apk 到手机上
adb uninstall 包名:卸载 app 从手机上
adb shell am start -W 包名/启动名:app 启动时间
```

**解析**

```text
【核心考点】 Android调试桥 adb命令
【题目解析】
本题考察对Android开发与测试中常用工具adb（Android Debug Bridge）的理解。adb是一个命令行工具，用于与Android设备进行通信，支持安装应用、调试、文件传输等操作。面试中常要求列举常用命令，以评估候选人的实际动手能力。
【参考答案要点】
1. 基本概念：adb即Android Debug Bridge（安卓调试桥），是Android SDK中的一个多功能命令行工具，允许开发者与模拟器或连接的Android设备进行交互。
2. 常用命令：
adb --help / adb：查看帮助信息
adb start-server：启动adb服务
adb kill-server：关闭adb服务
adb devices：查看已连接的设备列表
adb shell getprop ro.build.version.release：获取Android系统版本
adb push 本地路径 设备路径：从电脑推送文件到手机
adb pull 设备路径 本地路径：从手机拉取文件到电脑
adb logcat | grep（Unix）/ findstr（Windows） 包名：过滤指定应用的日志
adb shell：进入设备shell命令行
【面试角度】
回答时建议结合实际测试场景举例，例如“在测试中，我常用adb logcat抓取崩溃日志，或使用adb push/pull管理测试数据文件”，能体现实践能力。
【延伸知识】
除了基础命令，adb还支持安装/卸载应用（adb install/uninstall）、截屏（adb shell screencap）、模拟按键（adb shell input keyevent）等高级操作，这些在自动化测试中非常实用。
```

---

## Q006819

- 题型：简答
- 难度：简单

**题目**

```text
你对adb命令熟悉吗？能举例说一下用过哪些命令么？
```

**答案**

```text
Adb pull 从客户端拉取数据；
Adb push 推送数据到客户端；
Adb install 安装；
Adb uninstall 卸载对应包名的软件；
Adb shell 进入客户端；
Adb device 查看设备是否连接；
Adb logcat 导出日志。
```

**解析**

```text
【核心考点】 ADB命令 Android测试
【参考答案要点】
常用ADB命令及功能：
• adb pull：从Android设备拉取文件到电脑
• adb push：推送文件到Android设备
• adb install：安装APK应用
• adb uninstall：卸载指定包名的应用
• adb shell：进入设备Linux shell环境
• adb devices：查看已连接的设备列表
• adb logcat：导出或实时查看设备日志

【面试角度】
回答时建议结合实际测试场景，例如“使用adb logcat抓取崩溃日志定位问题”，或“通过adb install批量安装测试包”，体现动手能力。
【延伸知识】
ADB是Android Debug Bridge的缩写，是Android测试和开发的基础工具。高级用法包括adb shell dumpsys（查看系统服务状态）、adb shell am（启动Activity/Service）等，面试中提及可加分。
```

---

## Q006820

- 题型：简答
- 难度：简单

**题目**

```text
你最近这家公司都用过哪些测试机？
```

**答案**

```text
1，6、8p、x、xmax，小米 6、华为荣耀、vivo，
2，也可以参考云测平台列举的机型（例如：wetest，testin）
3，大公司测试机多，小公司测试机少
4，根据埋点数据选购热门机型测试。
```

**解析**

```text
【核心考点】 测试环境 兼容性测试
【题目解析】
本题考查测试人员的实际工作经验，尤其是移动端测试中设备选型的考量。面试官通过此问题评估候选人的项目真实性和对测试环境的理解。
【参考答案要点】
1. 列举具体机型：如iPhone 6/8p/X/Xs Max、小米6/8、华为P系列/荣耀、vivo X系列等，体现真实经验。
2. 参考云测平台：如WeTest、Testin等，可补充说明公司设备不足时借助云测服务。
3. 根据埋点数据：大公司根据用户设备占比选热门机型，小公司则受预算限制。
【面试角度】
回答时建议结合具体项目场景，例如"在某某项目中，我们主要测试了iOS和Android各3款主流机型，并利用云测平台覆盖了更多小众机型"，体现思考深度。
【延伸知识】
兼容性测试不仅关注机型，还需考虑操作系统版本、屏幕分辨率、网络环境等因素，面试中可主动提及以展示全面性。
```

---

## Q006821

- 题型：简答
- 难度：简单

**题目**

```text
使用过adb没？常用命令有哪些？
```

**答案**

```text
有用过，常用命令：adb logcat ，adb pull ，adb push ， adb install/uninstall，adb shell，adb shell monkey
```

**解析**

```text
【核心考点】 ADB命令 移动端测试
【参考答案要点】
常用ADB命令包括：
adb logcat：查看设备日志，用于调试和定位问题。
adb pull <远程路径> <本地路径>：从设备拉取文件到本地。
adb push <本地路径> <远程路径>：将本地文件推送到设备。
adb install/uninstall：安装或卸载应用。
adb shell：进入设备Linux shell，可执行各种命令。
adb shell monkey：运行Monkey测试，进行随机压力测试。
【面试角度】
回答时，建议结合实际测试场景说明，例如“在测试中，我常用adb logcat过滤特定标签来定位崩溃日志”，或“使用adb install -r覆盖安装测试升级功能”。同时可补充adb devices（查看连接设备）和adb shell dumpsys（获取系统服务信息）等进阶命令。
【延伸知识】
ADB是Android调试桥，是移动测试的基础工具。除了基本命令，还可结合adb shell am（Activity Manager）启动特定Activity，或adb shell pm（Package Manager）管理应用权限，用于自动化测试场景。
```

---

## Q006822

- 题型：单选
- 难度：简单

**题目**

```text
准备去一家从事手机APP开发的公司应聘测试职位，你可能需要掌握哪些工具的应用？（）
```

**选项**

```text
A. Bizrunner
B. Appium
C. Watir
D. Rational Function Tester
```

**答案**

```text
B
```

**正确选项**

```text
B. Appium
```

**解析**

```text
【核心考点】 移动测试工具 Appium
【题目解析】
本题考查移动APP测试工具的识别。Appium是开源跨平台移动应用自动化测试框架，支持iOS和Android，是手机APP测试的常用工具。
【选项解析】
✗ A. Bizrunner — 错误。Bizrunner并非主流测试工具，可能是干扰项。
✓ B. Appium — 正确。专门用于移动端APP的自动化测试，支持多种语言。
✗ C. Watir — 错误。Watir是Web应用测试工具，基于Ruby，不适用于手机APP。
✗ D. Rational Function Tester — 错误。IBM的自动化测试工具，主要用于Web和桌面应用，非移动端专用。
【易错提示】
注意区分移动端和Web端测试工具，Appium是移动端首选，而Watir、Selenium等用于Web。
```

---

## Q006827

- 题型：简答
- 难度：简单

**题目**

```text
如何查看一个 APP 的错误日志？
```

**答案**

```text
a. 查看 APP 的包名
b. 通过报名查看 APP 的进程号
c. 通过进程号，过滤 adb logcat 中的错误日志
```

**解析**

```text
【核心考点】 Android调试 adb命令 日志分析
【参考答案要点】
查看APP错误日志的典型步骤如下：
1. 获取APP包名：通过adb shell pm list packages | grep 或查看应用详情获取。
2. 获取进程ID（PID）：使用adb shell ps | grep 或adb shell pidof 。
3. 过滤错误日志：执行adb logcat -v time | grep ，或直接按级别过滤：adb logcat *:E（仅显示错误级别日志），也可结合grep进一步筛选。
此外，还可使用adb logcat -b crash查看崩溃日志，或通过Android Studio的Logcat工具直接查看。
【面试角度】
面试时建议补充实际调试场景，例如“在测试某APP闪退问题时，通过adb logcat -b crash获取堆栈信息，定位到空指针异常”。同时可提及日志级别（V/D/I/W/E）和常用过滤技巧，体现对Android调试工具的熟练度。
【易错提示】
注意：部分APP可能有多个进程，需确认目标进程的PID；另外，使用adb logcat -c可清空缓存，避免旧日志干扰。
```

---

## Q006830

- 题型：简答
- 难度：简单

**题目**

```text
常见的 adb 命令有哪些？
```

**答案**

```text
查看当前连接的设备： adb devices
安装软件： adb install 路径\xx.apk
卸载软件： adb uninstall <包名>
从电脑上发送文件到设备： adb push <本地路径> <远程路径>
adb push C:\test1.txt /sdcard/
从设备上下载文件到电脑： adb pull <远程路径> <本地路径>
adb pull /sdcard/test1.txt D:
实时获取日志： adb logcat -v time > D:\mylog.log
登录终端设备 shell： adb shell
查找包名/活动名： adb logcat | findstr START
（脚本中， cmp= 后面的值就是 包名/activity 名称）
启动 APP ：adb shell am start -n packageName/activity
关闭 app
语法： adb shell am force-stop 包名
监控 APP 启动时间 ：adb shell am start -W packageName/activity
Monkey 命令：
adb shell monkey -v -p mypackage 50
```

**解析**

```text
【核心考点】 ADB命令 Android调试 移动测试
【参考答案要点】
常见的 ADB 命令包括：
1. 查看当前连接的设备：adb devices
2. 安装软件：adb install 路径\xx.apk
3. 卸载软件：adb uninstall <包名>
4. 从电脑发送文件到设备：adb push <本地路径> <远程路径>（如 adb push C:\test1.txt /sdcard/）
5. 从设备下载文件到电脑：adb pull <远程路径> <本地路径>（如 adb pull /sdcard/test1.txt D:）
6. 实时获取日志：adb logcat -v time > D:\mylog.log
7. 登录终端设备 shell：adb shell
8. 查找包名/活动名：adb logcat | findstr ...（或使用 adb shell dumpsys package）
【面试角度】
本题考察移动测试基础，面试官期望候选人对 ADB 常用命令熟练掌握。建议回答时补充：adb install -r 覆盖安装、adb shell pm list packages 列出所有包名、adb shell input 模拟输入等高级用法，展示深度。
【易错提示】
注意 adb push 和 adb pull 的路径顺序：push 是本地到设备，pull 是设备到本地。卸载时需使用包名而非应用名，可通过 adb shell pm list packages 查询。日志输出时 -v time 参数可添加时间戳，便于分析。
```

---

## Q006832

- 题型：简答
- 难度：简单

**题目**

```text
怎么去抓app的系统日志？
```

**答案**

```text
使用adb 将手机端和电脑端链接，输入adb logcat 命令进行日志打印抓取
```

**解析**

```text
【核心考点】 日志抓取 adb命令
【参考答案要点】
1. 连接设备：使用USB或Wi-Fi将手机与电脑连接，确保adb devices识别设备。
2. 抓取日志：执行adb logcat命令，可加过滤条件如adb logcat -s TAG或adb logcat | grep 关键字。
3. 保存日志：使用adb logcat > log.txt将日志输出到文件，便于分析。
【面试角度】
回答时建议补充实际调试经验，例如如何根据日志定位ANR或崩溃问题，或使用adb logcat -b crash只抓取崩溃日志，能体现实战能力。
【延伸知识】
除了adb logcat，还可使用Android Studio的Logcat工具，或第三方工具如pidcat。面试中可能问到如何过滤特定进程的日志，可使用adb logcat --pid=进程ID。
```

---

## Q006834

- 题型：简答
- 难度：简单

**题目**

```text
我有多个安卓测试设备 需要给指定的设备发送shell命令 需要加那个参数？
```

**答案**

```text
通过加-s参数，比如：adb -s 设备id logcat > D:/test/log.txt
```

**解析**

```text
【核心考点】 ADB命令 多设备管理
【参考答案要点】
使用 -s 参数指定设备ID，例如：adb -s 设备id shell 命令。也可以先通过 adb devices 获取设备列表。
【面试角度】
回答时建议补充实际调试场景，例如“在自动化测试中，常通过adb -s参数控制不同设备”，体现实战能力。
【延伸知识】
除了-s参数，还可以使用环境变量 ANDROID_SERIAL 指定默认设备，或使用 adb -e（模拟器）和 adb -d（真机）简化操作。
```

---

## Q006838

- 题型：简答
- 难度：简单

**题目**

```text
简单介绍一下 Android SDK 的安装步骤
```

**答案**

```text
1、下载 jdk，配置jdk环境变量
2、下载安卓SDK ，配置ANDROID_HOME环境变量
3、打开安卓SDK包中的sdkmanager.bat包管理器，下载对应版本的SDK组件
```

**解析**

```text
【核心考点】 Android开发环境搭建 SDK配置
【题目解析】
Android SDK的安装是移动测试和开发的基础，主要步骤包括JDK安装、SDK下载、环境变量配置和组件管理。正确配置环境变量是确保adb、aapt等工具可用的关键。面试中常考察对SDK Manager和AVD Manager的熟悉程度。
【参考答案要点】
1. 安装JDK：下载并安装Java Development Kit，配置JAVA_HOME环境变量，并将bin目录添加到Path中。
2. 下载Android SDK：从官网或Android Studio中获取SDK，解压到指定目录，配置ANDROID_HOME环境变量指向该目录。
3. 配置Path：将%ANDROID_HOME%\tools和%ANDROID_HOME%\platform-tools添加到系统Path变量中。
4. 安装SDK组件：运行SDK Manager（sdkmanager.bat），下载所需版本的平台工具、构建工具和系统映像等。
【面试角度】
回答时可补充常见问题排查，如“环境变量配置后需重启终端生效”或“SDK Manager下载失败时可配置代理”。此外，提及Android Studio的集成安装方式也能体现对工具的全面了解。
【易错提示】
ANDROID_HOME路径中不要包含空格或中文，否则可能导致adb命令无法识别。
```

---

## Q006839

- 题型：简答
- 难度：简单

**题目**

```text
说几个常用的 ADB 命令？
```

**答案**

```text
adb --help / adb :看见帮助信息
adb start-server:启动 adb 服务
adb kill-server:关闭 adb 服务
adb devices:查看手机设备号
adb shell getprop ro.build.version.release:获取系统版本
adb shell :进入 shell 命令行，可以操作 Linux 命令
adb install 路径/apk 文件:安装 apk 到手机上
adb uninstall 包名:卸载 app 从手机上
adb shell am start -W 包名/启动名:app 启动时间
```

**解析**

```text
【核心考点】 ADB命令 移动端测试
【参考答案要点】
1. adb --help / adb：查看帮助信息。
2. adb start-server / adb kill-server：启动/关闭ADB服务。
3. adb devices：查看已连接的设备列表。
4. adb shell getprop ro.build.version.release：获取Android系统版本。
5. adb shell：进入设备shell命令行。
6. adb install 路径/apk文件：安装APK到设备。
7. adb uninstall 包名：卸载应用。
8. adb shell am start -W 包名/启动名：测量应用启动时间。
【面试角度】
面试中可补充实际应用场景，如使用adb logcat抓取日志、adb shell input模拟点击等，体现对移动测试工具的熟练度。
【延伸知识】
ADB（Android Debug Bridge）是Android开发与测试的通用调试工具，支持设备管理、应用安装卸载、日志抓取、文件传输等功能。
```

---

## Q006842

- 题型：简答
- 难度：简单

**题目**

```text
请写出实现下列功能的adb命令: 通过adb命令安装及卸载apk安装包
```

**答案**

```text
安装：adb install 安装包名称.apk

卸载：adb uninstall 包名
```

**解析**

```text
【核心考点】 ADB命令 Android测试
【题目解析】
本题考查Android调试桥（ADB）的基本命令，是移动测试工程师的必备技能。ADB是Android SDK中的命令行工具，用于与设备或模拟器通信。
【参考答案要点】
安装APK：adb install 安装包名称.apk
卸载APK：adb uninstall 包名
【面试角度】
回答时建议补充实际使用场景，例如："在持续集成中，我们常用adb install -r 覆盖安装旧版本"，或"卸载前需通过adb shell pm list packages获取包名"，体现经验深度。
【易错提示】
注意安装命令后跟的是文件名（含.apk扩展名），而卸载命令后跟的是包名（如com.example.app），两者不同，面试中常被混淆。
```

---

## Q006803

- 题型：简答
- 难度：中等

**题目**

```text
APP兼容性有做过测试吗？了解过云测平台吗？怎么使用的？
```

**答案**

```text
有，APP兼容性测试是关于应用是否可以在不同操作系统正常使用的测试，如果开发有Android和IOS两个平台的软件，那么在这两个平台都要做兼容性测试。如Android版本有4.1.1、4.2.1....，IOS版本有7.1.2\8.3\9.1等；
能否适配各种屏幕尺寸（Android系列：4.x、5.x市场占有率最高，IOS系列：iphone：3.5英寸、4英寸、4.8英寸、5.5英寸）；
分辨率适配（分辨率不同，界面图标、文字大小会不同。保证主流分辨率下图标展示完整，文字不被遮挡）；
一般测试兼容性像Android系统手机，选取市面上主流手机就行，例如：小米、华为、oppo、vivo等；ios系统手机就是iphone4、5、6、6s、6plus，或者借助云测试平台。

云测平台是基于云计算的一种新型测试方案。云测试提供一整套测试环境，测试人员利用虚拟桌面等手段登录到该测试环境，就可以立即展开测试。这将软硬件安装、环境配置、环境维护的代价转移给云测试提供者。服务商提供多种平台，多种浏览器的平台，一般的用户在本地用Selenium把自动化测试脚本编写好，然后上传到他们网站，然后就可以在他们的平台上运行Selenium脚本。
```

**解析**

```text
【核心考点】 APP兼容性测试 云测平台
【参考答案要点】
1. 兼容性测试定义：APP兼容性测试是验证应用在不同操作系统、设备型号、屏幕尺寸、分辨率及网络环境下能否正常运行的测试活动。
2. 测试范围：包括Android和iOS两大平台，需覆盖主流操作系统版本（如Android 4.1.1、4.2.1等，iOS 7.1.2、8.3、9.1等），以及不同屏幕尺寸（如3.5英寸、4英寸、4.8英寸、5.5英寸）和分辨率适配。
3. 设备选择：Android系统选取市面主流手机，如小米、华为、OPPO、vivo等；iOS系统覆盖iPhone主流型号。
4. 云测平台使用：云测平台（如Testin、百度MTC）提供远程真机测试服务，可上传APP包，选择多款设备并行执行兼容性测试，自动生成测试报告，包括安装/卸载、UI适配、功能验证等。
【面试角度】
回答时建议结合实际项目经验，例如“在XX项目中，我们使用云测平台覆盖了200+款Android设备，发现3款机型存在UI显示异常，及时修复后上线”，能体现实战能力。
【延伸知识】
兼容性测试还需关注网络兼容性（2G/3G/4G/5G/WiFi）、硬件兼容性（摄像头、传感器、GPS）以及系统权限适配（如Android 6.0以上动态权限申请）。
```

---

## Q006804

- 题型：简答
- 难度：中等

**题目**

```text
App端测试的抓包流程步骤？
```

**答案**

```text
1、打开Fiddler，设置代理，并允许远程连接
2、手机连接电脑的热点网络，或者同在一个局域网内
3、手机网络连接中，设置网络代理，IP是电脑的同网段IP地址，端口是8888，用手机下载一个fiddler的令牌；
4、打开网速模拟模式开关（Rules → Performances → Simulate Modem Speeds ）；
5、手机访问APP，或者用手机浏览器访问网络，观察功能响应或者页面刷新速度。
```

**解析**

```text
【核心考点】 抓包工具Fiddler 移动端测试
【题目解析】
本题考查移动端App测试中，使用Fiddler进行网络抓包和弱网模拟的完整流程。Fiddler作为代理工具，通过配置手机代理和安装证书，可以截获HTTP/HTTPS请求，并模拟网络延迟。
【参考答案要点】
1. 配置Fiddler代理：打开Fiddler，在Tools→Options→Connections中勾选“Allow remote computers to connect”，设置代理端口（默认8888）。
2. 手机连接网络：确保手机和电脑在同一局域网（如电脑开启热点，手机连接该热点）。
3. 设置手机代理：在手机WiFi设置中，将代理设为手动，填入电脑IP和端口8888，然后使用手机浏览器访问http://ip:8888下载并安装Fiddler根证书（用于解密HTTPS流量）。
4. 开启弱网模拟：在Fiddler菜单栏选择Rules→Performances→Simulate Modem Speeds，即可模拟2G/3G等慢速网络。
5. 开始抓包：操作手机App或浏览器，Fiddler中会显示所有请求，可观察响应时间、状态码等。
【面试角度】
回答时建议补充实际项目中的常见问题，例如：证书安装失败（需确认手机系统版本）、代理设置后无法上网（检查防火墙或端口冲突）、弱网模拟参数自定义（通过Rules→Customize Rules修改代码）。
【易错提示】
容易遗漏HTTPS抓包所需的证书安装步骤，或忘记开启远程连接选项，导致手机无法连接代理。
```

---

## Q006814

- 题型：简答
- 难度：中等
- 解析：AI 补全（原数据缺失解析）

**题目**

```text
adb这块儿的 logcat trance dropbox三种常用的日志方法，哪种是工作中经常用到的呢？
```

**答案**

```text
不管是anr还是crash，都会在dropbox里存着。
一般我们是打开adb logcat一直刷新的日志。遇到问题就直接ctrl+c，终止刷新，查看日志。
如果是anr的话，因为logcat看不到具体的。就只能去trace或者dropbox看了
```

**解析**

```text
【核心考点】移动端常用日志获取方式及适用场景。
【题目解析】日常最常用的是持续刷新 logcat，复现问题后立即停止，保留完整日志。发生 ANR 时 logcat 信息有限，需要查看 trace 或 dropbox；崩溃和 ANR 记录也会保存在 dropbox 中。三种方式结合，才能覆盖普通异常、无响应和系统级记录。
【答题要点】
1. logcat 适合实时复现和查看普通报错。
2. trace 用于分析 ANR 的线程堆栈。
3. dropbox 保存崩溃、ANR 等系统事件记录。
【面试提示】强调先复现再抓日志，并说明日志时间点对齐，体现排查经验。
```

---

## Q006825

- 题型：简答
- 难度：中等

**题目**

```text
如何去查看一个 APP 的错误日志？
```

**答案**

```text
a. 查看 APP 的包名
b. 通过报名查看 APP 的进程号
c. 通过进程号，过滤 adb logcat 中的错误日志
```

**解析**

```text
【核心考点】 Android调试 日志分析
【参考答案要点】
1. 查看APP包名：通过命令adb shell pm list packages或应用信息获取。
2. 查看进程号：使用adb shell ps | grep 包名获取PID。
3. 过滤错误日志：执行adb logcat | grep PID或adb logcat -v time *:E过滤错误级别日志。
【面试角度】
回答时建议补充实际调试经验，如使用adb logcat -c清空缓存后再抓取，或结合bugreport生成完整报告，体现对工具链的熟练度。
【延伸知识】
除了adb logcat，还可以使用Android Studio的Logcat窗口、DDMS或第三方工具如PID Cat进行更高效的日志过滤与分析。
```

---

## Q006826

- 题型：简答
- 难度：中等

**题目**

```text
如何定位到App页面元素，有哪些工具？
```

**答案**

```text
对于原生（native）页面元素：
(1)Android SDK自带的uiautomatorviewer.bat工具
(2)Appium desktop中的inspector工具
对于混合应用（Hybrid）中嵌套的web页面元素：
(1)Chrome浏览器的dev tool工具（需要翻墙）
(2)UC开发者工具（不需要翻墙，推荐）
```

**解析**

```text
【核心考点】 App元素定位 移动测试工具
【题目解析】
本题考察移动端自动化测试中元素定位的常用工具和方法。题目答案区分了原生页面和混合应用（Hybrid）两种场景，分别给出了推荐工具。这是Appium等移动测试框架的基础技能。
【参考答案要点】
1. 原生页面元素定位：
- Android：使用SDK自带的uiautomatorviewer.bat工具，可查看UI层次结构和属性。
- 跨平台：Appium Desktop内置的Inspector工具，支持iOS和Android，提供录制和元素定位功能。
2. 混合应用Web页面元素定位：
- Chrome DevTools：通过远程调试（需翻墙）查看WebView元素。
- UC开发者工具：无需翻墙，适合国内环境，支持UC浏览器内核的WebView调试。
3. 其他工具：Appium的driver.getPageSource()获取页面源码，XPath、ID、ClassName等定位策略。
【面试角度】
面试官可能追问元素定位策略选择（如ID优先于XPath）以及处理动态元素的方法（如使用相对XPath或等待机制）。建议结合Appium实战经验，说明如何解决元素不可见、加载延迟等问题。
【易错提示】
注意区分原生和WebView的定位方式：原生元素使用UIAutomator或XCUITest驱动，WebView需切换上下文（driver.switchTo().context()）。另外，Chrome DevTools需要开启WebView调试模式，部分App可能默认关闭。
```

---

## Q006828

- 题型：简答
- 难度：中等

**题目**

```text
如何查看安卓 app 界面的 activity 和起始 activity
```

**答案**

```text
1. 使用 pm 管理器查看包名
adb shell pm list package -f
将获取手机内所有 apk 对应的包名和路径
如果是 windows 可以后接 findstr，例如：
adb shell pm list package -f | findstr douban

2. 使用 am 管理器，查看包名
adb shell am monitor

3. 使用 aapt 查看包名、界面名
aapt 是 sdk 自带的一个工具，在 sdk\builds-tools\目录下

以豆瓣 App 为例：

1.把安装包放到 aapt 目录下

2.从 cmd 中切换目录到 sdk\builds-tools\下

3.执行 aapt dump badging
运行后的结果中以下两行分别是应用包名 package 和 入 口 activity 名 称
package:name='com.tencent.qqmusic'
launchable-activity: name='com.tencent.qqmusic.activity.AppStarterActivity'
```

**解析**

```text
【核心考点】 Android 测试 ADB 命令 Activity 管理
【题目解析】
本题考查 Android 测试中如何通过 ADB 命令获取 App 的 Activity 和起始 Activity。这是移动测试的基础技能，面试中常考察对 ADB 工具链的掌握程度。
【参考答案要点】
1. 使用 pm 管理器查看包名：执行 adb shell pm list package -f | findstr douban（Windows）或 grep douban（Linux/Mac），获取 App 的包名和 APK 路径。
2. 使用 am 管理器查看 Activity：执行 adb shell am monitor，然后启动目标 App，在日志中查看当前 Activity 名称。
3. 使用 aapt 工具查看：在 SDK 的 build-tools 目录下，执行 aapt dump badging app.apk，输出中包含 launchable-activity: name='com.example.MainActivity' 等起始 Activity 信息。
【面试角度】
回答时建议结合实际项目经验，例如“在测试某 App 时，我使用 aapt 工具快速定位了启动 Activity，从而编写了自动化测试脚本”，能体现实践能力。
【易错提示】
注意 am monitor 需要实时操作 App，而 aapt 是静态分析 APK 文件，两者适用场景不同。面试中可能追问如何区分 App 的多个 Activity。
```

---

## Q006829

- 题型：简答
- 难度：中等

**题目**

```text
安卓中如何取出日志信息？
```

**答案**

```text
把安卓系统日志信息实时导入到本地：adb logcat -v time > d:\mylog.log
运行使用某个 app，实时获取该 app 的日志信息（cmd 里面的返回信息） ：
adb shell monkey -p com.android.calendar -v 1000 > d:\mylog2.log
```

**解析**

```text
【核心考点】 Android日志管理 ADB命令
【题目解析】
本题考查Android测试中日志提取的常用ADB命令。adb logcat是核心工具，配合参数可过滤和导出日志；adb shell monkey用于压力测试并获取应用日志。
【参考答案要点】
1. 导出全部日志：使用命令 adb logcat -v time > d:\mylog.log，将系统日志实时导入本地文件，-v time参数添加时间戳。
2. 获取特定应用日志：结合monkey测试，如 adb shell monkey -p com.android.calendar -v 1000 > d:\mylog2.log，运行指定应用并捕获日志。
3. 过滤日志：可使用 adb logcat -s TAG 按标签过滤，或 adb logcat | grep "关键字" 筛选特定信息。
【面试角度】
面试中常问日志分析技巧，如如何定位ANR或崩溃日志。建议补充说明使用 adb bugreport 获取完整诊断信息，提升答案深度。
【易错提示】
注意日志文件路径需有写入权限，且monkey测试的-v数量影响日志详细程度，过多可能导致文件过大。
```

---

## Q006831

- 题型：简答
- 难度：中等

**题目**

```text
微信小程序怎么抓包？
```

**答案**

```text
抓包过程跟app一样。
1、保证安装手机跟电脑端同一个网络
2、对fiddler进行简单配置：端口号、勾选“Allow remote computers to connect”；如果是Https请求还需要勾选“Decrpt HTTPS traffic”
3、打开手机，进入wifi设置网络代理：填入电脑端ip、fiddler端口号
然后操作小程序就可以抓取到数据包了。如果是https请求，需要在手机中浏览器，输入电脑ip:端口号，访问获取fiddler证书并安装安装证书。证书安装成功后就可以在fiddler上抓取HTTPS的请求了。
当然也可以，把小程序在电脑端打开，然后在电脑上通过fiddler去抓。
```

**解析**

```text
【核心考点】 抓包工具 Fiddler 微信小程序
【题目解析】
本题考察测试工程师对移动端抓包的实际操作能力，特别是针对微信小程序这种特殊环境。微信小程序使用HTTPS协议，抓包需要额外配置证书。
【参考答案要点】
1. 环境准备：确保手机和电脑在同一局域网内。
2. Fiddler配置：设置端口号（如8888），勾选“Allow remote computers to connect”；若抓取HTTPS，还需勾选“Decrypt HTTPS traffic”。
3. 手机代理设置：进入WiFi设置，手动配置代理为电脑IP和Fiddler端口。
4. 证书安装：在手机浏览器访问电脑IP:端口号，下载并安装Fiddler根证书，才能解密HTTPS流量。
5. 开始抓包：操作小程序，Fiddler即可捕获请求数据。
【面试角度】
回答此类问题时，建议结合实际项目经验举例说明，例如“在测试某小程序支付功能时，通过抓包发现请求参数缺失，定位到前端bug”，能体现问题排查能力。
【易错提示】
常见错误：忘记安装证书导致无法抓取HTTPS；或代理设置后未关闭，导致手机无法上网。建议抓包后及时关闭代理。
```

---

## Q006833

- 题型：简答
- 难度：中等

**题目**

```text
怎么抓app 的包？
```

**答案**

```text
前提：保证安装手机跟电脑端同一个网络
1、首先需安装fiddler抓包工具
2、安装成功后对fiddler进行简单配置：
打开fiddler，Tools->Fiddler Options---勾选“Decrpt HTTPS traffic”，选中后Fiddler可以截获HTTPS请求---勾选“Allow remote computers to connect”，选中后允许别的机器把HTTP/HTTPS请求发送到Fiddler上---配置完成后，重新启动Fiddler
3、获取Fiddler所在机器的IP地址（运行cmd-->ipconfig，即可获得IP地址）
4、在手机中设置网络代理
打开手机设置 —> WLAN —> 选择手动代理--》代理服务器主机名：填写Fiddler所在机器的IP地址---》代理服务器端口：填写Fiddler设置的代理端口
5、上面配置好后就可以在Fiddler就可以抓取到移动端App应用的请求了
6、如果要抓取HTTPS的请求，那么要在Android手机安装Fiddler证书
打开手机中的浏览器，输入192.168.3.104:8888，这是你上面在手机中设置网络代理Fiddler的服务地址。如果出现响应页面说明访问代理服务Fiddler成功，就可以安装证书了。证书安装成功后就可以在fiddler上抓取HTTPS的请求了
```

**解析**

```text
【核心考点】 移动端测试 抓包工具 Fiddler
【参考答案要点】
抓取App网络包（以Fiddler为例）的通用步骤如下：
1. 环境准备：确保手机和电脑连接在同一个局域网（Wi-Fi）下。
2. Fiddler配置：打开Fiddler，进入Tools → Fiddler Options：
- 勾选“Decrypt HTTPS traffic”，以截获HTTPS请求。
- 勾选“Allow remote computers to connect”，允许手机等远程设备连接。
- 配置完成后重启Fiddler。
3. 获取电脑IP：在命令行运行ipconfig，找到本机IP地址。
4. 手机设置代理：在手机Wi-Fi设置中，将代理设为手动，填入电脑IP和Fiddler默认端口（通常为8888）。
5. 安装证书（HTTPS抓包）：手机浏览器访问http://电脑IP:8888，下载并安装Fiddler根证书，以解密HTTPS流量。
【面试角度】
面试官常关注HTTPS抓包原理和常见问题排查，例如：为什么抓不到HTTPS包？（未安装证书或证书未信任）；为什么手机连不上代理？（防火墙未放行8888端口）。建议回答时补充这些细节，展示深度。
【延伸知识】
除Fiddler外，常用抓包工具还包括Charles、Wireshark、mitmproxy等。对于iOS 14+或Android 7+，部分App因SSL Pinning机制无法直接抓包，需要配合Xposed、Frida等工具绕过，属于高级技巧。
```

---

## Q006835

- 题型：简答
- 难度：中等

**题目**

```text
手机怎么抓HTTPS的包？
```

**答案**

```text
前提：保证安装手机跟电脑端同一个网络
1、首先需安装fiddler抓包工具
2、安装成功后对fiddler进行简单配置：
打开fiddler，Tools->Fiddler Options---勾选“Decrpt HTTPS traffic”，选中后Fiddler可以截获HTTPS请求---勾选“Allow remote computers to connect”，选中后允许别的机器把HTTP/HTTPS请求发送到Fiddler上---配置完成后，重新启动Fiddler(具体的步骤可不用这么细)
3、获取Fiddler所在机器的IP地址（运行cmd-->ipconfig，即可获得IP地址）
4、在手机中设置网络代理
打开手机设置 —> WLAN —> 选择手动代理--》代理服务器主机名：填写Fiddler所在机器的IP地址---》代理服务器端口：填写Fiddler设置的代理端口
5、上面配置好后就可以在Fiddler就可以抓取到移动端App应用的请求了
6、如果要抓取HTTPS的请求，那么要在Android手机安装Fiddler证书
打开手机中的浏览器，输入192.168.3.104:8888，这是你上面在手机中设置网络代理Fiddler的服务地址。如果出现响应页面说明访问代理服务Fiddler成功，就可以安装证书了。证书安装成功后就可以在fiddler上抓取HTTPS的请求了
```

**解析**

```text
【核心考点】 移动端测试 抓包工具 HTTPS
【参考答案要点】
前提：手机和电脑连接同一网络。
1. 安装并配置Fiddler：打开Fiddler，进入Tools → Fiddler Options，勾选“Decrpt HTTPS traffic”以截获HTTPS请求，勾选“Allow remote computers to connect”以允许其他设备发送请求，重启Fiddler。
2. 获取电脑IP：在命令行运行ipconfig，记录IP地址。
3. 手机端设置代理：在手机Wi-Fi设置中，将代理设为手动，输入电脑IP和Fiddler默认端口（8888）。
4. 安装证书：手机浏览器访问http://电脑IP:8888，下载并安装Fiddler根证书，以解密HTTPS流量。
【面试角度】
回答时，建议强调证书安装和代理配置的细节，因为这是常见易错点。此外，可提及使用Charles等替代工具，展示知识广度。
【延伸知识】
抓包原理：Fiddler作为中间人代理，截获并转发请求。HTTPS抓包需安装根证书，使客户端信任Fiddler的伪造证书。注意iOS 10.3+和Android 7.0+对用户证书的限制，可能需要额外配置。
```

---

## Q006836

- 题型：简答
- 难度：中等

**题目**

```text
手机是如何用Fiddler抓请求的?(跟网页用法一样吗?)
```

**答案**

```text
前提：保证安装手机跟电脑端同一个网络
1、对fiddler进行简单配置：
打开fiddler，Tools->Fiddler Options---勾选“Decrpt HTTPS traffic”，选中后Fiddler可以截获HTTPS请求---勾选“Allow remote computers to connect”，选中后允许别的机器把HTTP/HTTPS请求发送到Fiddler上---配置完成后，重新启动Fiddler
2、获取Fiddler所在机器的IP地址（运行cmd-->ipconfig，即可获得IP地址）
3、在手机中设置网络代理
打开手机设置 —> WLAN —> 选择手动代理--》代理服务器主机名：填写Fiddler所在机器的IP地址---》代理服务器端口：填写Fiddler设置的代理端口
4、上面配置好后就可以在Fiddler就可以抓取到移动端App应用的请求了
5、如果要抓取HTTPS的请求，那么要在Android手机安装Fiddler证书
打开手机中的浏览器，输入192.168.3.104:8888，这是你上面在手机中设置网络代理Fiddler的服务地址。如果出现响应页面说明访问代理服务Fiddler成功，就可以安装证书了。证书安装成功后就可以在fiddler上抓取HTTPS的请求了
```

**解析**

```text
【核心考点】 抓包工具 Fiddler 移动端测试
【题目解析】
本题考察Fiddler在移动端抓包的配置与原理。与网页端不同，手机端需要设置代理并安装证书以解密HTTPS流量。回答需清晰描述配置步骤和关键点。
【参考答案要点】
1. Fiddler配置：打开Fiddler，在Tools→Fiddler Options中勾选“Decrypt HTTPS traffic”以解密HTTPS请求，勾选“Allow remote computers to connect”以允许手机连接。
2. 获取IP：在Fiddler所在电脑运行cmd→ipconfig，获取IP地址。
3. 手机设置代理：在手机WLAN设置中，选择手动代理，填入电脑IP和Fiddler默认端口（8888）。
4. 安装证书：手机浏览器访问代理地址（如192.168.1.100:8888），下载并安装Fiddler根证书，以解密HTTPS流量。
5. 与网页区别：网页端通常无需设置代理和安装证书，直接使用Fiddler即可抓包；手机端需额外配置代理和证书，且不同系统（iOS/Android）证书安装步骤略有差异。
【面试角度】
面试中常追问HTTPS抓包原理，如中间人攻击机制，以及不同手机系统（如iOS 14+）的证书信任问题，建议提前准备。
【易错提示】
容易遗漏证书安装步骤，导致HTTPS请求无法抓取；或混淆代理设置与VPN设置。
```

---

## Q006843

- 题型：简答
- 难度：中等

**题目**

```text
请求是个https协议的，抓取app接口的时候，有什么特别的操作和条件抓到它吗？
```

**答案**

```text
前提：保证安装手机跟电脑端同一个网络
1、首先需安装fiddler抓包工具
2、安装成功后对fiddler进行简单配置：
打开fiddler，Tools->Fiddler Options---勾选“Decrpt HTTPS traffic”，选中后Fiddler可以截获HTTPS请求---勾选“Allow remote computers to connect”，选中后允许别的机器把HTTP/HTTPS请求发送到Fiddler上---配置完成后，重新启动Fiddler(具体的步骤可不用这么细)
3、获取Fiddler所在机器的IP地址（运行cmd-->ipconfig，即可获得IP地址）
4、在手机中设置网络代理
打开手机设置 —> WLAN —> 选择手动代理--》代理服务器主机名：填写Fiddler所在机器的IP地址---》代理服务器端口：填写Fiddler设置的代理端口
5、上面配置好后就可以在Fiddler就可以抓取到移动端App应用的请求了
6、如果要抓取HTTPS的请求，那么要在Android手机安装Fiddler证书
打开手机中的浏览器，输入192.168.3.104:8888，这是你上面在手机中设置网络代理Fiddler的服务地址。如果出现响应页面说明访问代理服务Fiddler成功，就可以安装证书了。证书安装成功后就可以在fiddler上抓取HTTPS的请求了
```

**解析**

```text
【核心考点】 HTTPS抓包 Fiddler 移动端测试
【题目解析】
抓取HTTPS协议的APP接口需要处理SSL/TLS加密。Fiddler作为中间人代理，通过安装其根证书来解密HTTPS流量。同时，移动端抓包还需确保手机和电脑在同一网络，并配置代理。
【参考答案要点】
前提条件：手机和电脑连接同一局域网。
操作步骤：
1. Fiddler配置：打开Fiddler，进入Tools → Options → HTTPS，勾选“Decrypt HTTPS traffic”，并勾选“Allow remote computers to connect”。重启Fiddler。
2. 获取电脑IP：运行cmd输入ipconfig，记录IPv4地址。
3. 手机代理设置：在手机WiFi设置中，将代理设为手动，填写电脑IP和Fiddler默认端口（8888）。
4. 安装证书：手机浏览器访问http://电脑IP:8888，下载并安装Fiddler根证书（iOS需在设置中信任描述文件）。
5. 开始抓包：在手机上操作APP，Fiddler即可显示HTTPS请求详情。
【面试角度】
回答时建议强调证书安装与信任是HTTPS抓包的关键步骤，并提及不同系统（Android/iOS）的差异，如Android 7.0以上需配置网络安全策略，体现对移动端测试的深入理解。
【易错提示】
常见错误：忘记安装证书或未信任证书导致抓包失败；未勾选“Allow remote computers to connect”导致手机无法连接；端口被防火墙阻止。
```

---

## Q006824

- 题型：简答
- 难度：未标注
- 解析：AI 补全（原数据缺失解析）

**题目**

```text
在做APP测试时，如何去获取APP的安装包？
```

**答案**

```text
公司内部有一个移动端包管理平台，开发写完代码后，会打包发布到包管理平台中。无论安卓还是iOS，
都可以通过手机浏览器访问包管理平台，然后点击不同系统、不同版本的安装包进行下载，在手机上点击安装就行。
```

**解析**

```text
【核心考点】移动应用安装包的获取渠道。
【题目解析】常见做法是开发完成打包后上传到公司内部的包管理平台，测试人员用手机浏览器访问平台，按系统类型和版本选择安装包下载并安装。该方式便于统一管理版本和权限，也避免测试人员自行编译。
【答题要点】
1. 包源统一，版本可追溯。
2. 按系统、版本、渠道选择对应安装包。
3. 安装前确认包名、版本和签名正确。
【面试提示】可补充提测流程和包权限管理，说明你了解团队协作方式。
```

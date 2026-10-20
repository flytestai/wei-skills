# 自动化 · Appium

> 共 14 题 · 所属领域：自动化 · 专题：Appium

---

## Q003181

- 题型：简答
- 难度：简单

**题目**

```text
APP 底层实现架构？
```

**答案**

```text
APP 实现层面---- 前端 UI--- 后台服务 -- 数据库；
```

**解析**

```text
【核心考点】 APP架构 分层设计
【题目解析】
本题考察APP底层实现架构的基本理解。典型的APP架构通常分为三层：前端UI层（用户界面）、后台服务层（业务逻辑处理）、数据库层（数据存储）。回答时需清晰描述各层职责及交互关系。
【参考答案要点】
1. 前端UI层：负责用户交互和界面展示，包括iOS/Android原生或跨平台框架。
2. 后台服务层：处理业务逻辑，如用户认证、数据校验、API接口等，通常采用微服务或单体架构。
3. 数据库层：存储和管理数据，如MySQL、Redis等。
【面试角度】
面试官可能进一步追问各层之间的通信方式（如RESTful API、WebSocket）或常见架构模式（如MVC、MVVM）。建议结合具体项目说明，例如“我们项目采用MVVM架构，前端通过Retrofit与后台交互”。
【延伸知识】
现代APP架构还可能包括缓存层（如本地数据库）、消息队列等，以提升性能和可靠性。
```

---

## Q003183

- 题型：简答
- 难度：简单

**题目**

```text
Appium 都有哪些启动方式
```

**答案**

```text
1.客户端启动(appium desktop版本，在可视化界面中配置参数)
2.命令行启动(npm命令安装appium。在命令行当中运行appium启动，可配置参数。)
```

**解析**

```text
【核心考点】 Appium 移动端测试
【题目解析】
本题考查Appium的启动方式。Appium支持桌面版（Appium Desktop）和命令行（CLI）两种启动方式，各有适用场景。
【参考答案要点】
1. 桌面版启动：使用Appium Desktop GUI工具，在界面中配置服务器参数（如端口、地址），点击启动按钮。适合初学者和调试。
2. 命令行启动：通过npm安装appium后，在终端运行appium命令，可附加参数如-p 4723指定端口。适合持续集成和自动化。
【面试角度】
可补充Appium 2.0的插件机制和appium driver install命令，展示对最新版本的了解。
【易错提示】
注意Appium Desktop已逐渐被Appium Inspector替代，但核心概念相同。
```

---

## Q003185

- 题型：单选
- 难度：简单

**题目**

```text
Appium只支持Java 来编写测试脚本。（）
```

**选项**

```text
A. 对
B. 错
```

**答案**

```text
B
```

**正确选项**

```text
B. 错
```

**解析**

```text
【核心考点】 Appium基础 多语言支持
【题目解析】
本题考查Appium对编程语言的支持情况。Appium是一个开源的移动端自动化测试框架，基于WebDriver协议，支持多种编程语言编写测试脚本，包括但不限于Java、Python、Ruby、JavaScript、C#等。因此，题目中“只支持Java”的说法是错误的。
【选项解析】
✗ A. 对 — 错误。Appium支持多种语言，并非仅限于Java。
✓ B. 错 — 正确。Appium支持Java、Python、Ruby等多种语言，因此该说法错误。
【易错提示】
部分初学者可能误以为Appium仅支持Java，因为早期教程多以Java为例。实际Appium设计为语言无关，通过HTTP接口与客户端通信，任何能发送HTTP请求的语言均可使用。
```

---

## Q003187

- 题型：简答
- 难度：简单

**题目**

```text
DesiredCapabitlies类有什么作用？
```

**答案**

```text
DesiredCapabilities类可以告诉SeleniumWebDriver执行的测试环境的细节，它的setCapability方法可以在SeleniumGrid中使用，用于在不同机器配置进行并行执行，它可以用于设置执行测试用例是采用的浏览器属性（如Chrome、IE、Firefox）、平台名称（如Linux、Windows）等。
```

**解析**

```text
【核心考点】 Selenium WebDriver 测试配置
【题目解析】
本题考查Selenium中DesiredCapabilities类的用途，属于自动化测试基础。该类用于定义测试环境配置，如浏览器类型、版本、平台等，尤其在Selenium Grid中实现分布式并行测试。
【参考答案要点】
1. 作用：DesiredCapabilities类封装了测试环境的属性，如浏览器（Chrome、Firefox）、平台（Windows、Linux）、版本等。
2. 使用场景：在Selenium Grid中，通过setCapability方法设置节点要求，实现跨平台、跨浏览器的并行测试。
3. 示例：设置Chrome浏览器：DesiredCapabilities caps = new DesiredCapabilities(); caps.setBrowserName("chrome"); caps.setPlatform(Platform.WINDOWS);
【易错提示】
注意DesiredCapabilities在Selenium 3中仍常用，但在Selenium 4中推荐使用Options类（如ChromeOptions）替代，面试时提及这一点可展示知识更新。
```

---

## Q003182

- 题型：简答
- 难度：中等

**题目**

```text
Appium UI 自动化中显式等待和隐式等待的异同？
```

**答案**

```text
1. 相同点都是智能等待，在一定时间范围内不断查找元素，一旦找到立刻结束查找继续执行代码，没找到才会一直找到超时为止；

2. 不同点是隐式等待是全局性设置，并且可以随时更改，在更改后对之后的 findxxx 方法生效，对点击、输入、滑动之类的操作不起作用；显式等待仅仅针对单一元素生效，并且不仅仅是针对查找，也可以针对元素的某些属性进行自定义判断很可能下一个问题就是你在测试过程中常用哪种等待？三种都有，相互结合根据各自不同特点应用不同的场景；

3. 大部分元素出现的时间可以用隐式等待统一设置；

4. 特性元素出现时间较长，可以用显式等待针对他进行超时设置；

5. 当操作类型必须等待一段时间才能完成时，使用 sleep，比如有数据推送的界面；

6. 如果因为间隔较小导致操作失败，必须加 sleep，比如滑动、返回。
```

**解析**

```text
【核心考点】 Appium等待机制 显式等待 隐式等待
【参考答案要点】
相同点：都是智能等待，在一定时间范围内不断查找元素，一旦找到立刻结束查找继续执行代码，没找到才会一直找到超时为止。
不同点：
1. 作用范围：隐式等待是全局性设置，对之后的所有findxxx方法生效，但对点击、输入、滑动等操作不起作用；显式等待仅针对单一元素生效，且可针对元素的属性进行自定义判断。
2. 使用场景：大部分元素出现时间可用隐式等待统一设置；特性元素出现时间较长时，可用显式等待针对其设置超时；当操作类型必须等待一段时间才能完成时，也需显式等待。
【面试角度】
面试中常追问“你在测试过程中常用哪种等待？”，建议回答三种等待（隐式、显式、强制等待）相互结合，根据各自特点应用不同场景。
【延伸知识】
强制等待（time.sleep()）会固定阻塞线程，不推荐在自动化脚本中大量使用，仅用于调试或特定延迟场景。
```

---

## Q003184

- 题型：简答
- 难度：中等

**题目**

```text
Appium与 Selenium的关系和区别
```

**答案**

```text
区别：
1、appium是用来实现移动端app的自动化测试，selenium是实现web网页自动化测试
2、appium分为appium代码客户端和appium服务端，服务端有命令行和桌面应用2种，对app的操作请求由appium服务端发送到手机端，通过手机端调用ios/android系统自带的测试框架来完成；
3、selenium对网页的操作请求，是由浏览器的驱动程序来操作浏览器完成的。主流的浏览器都有对应的驱动程序。

关系：
appium并没有重新造轮子，直接延用了selenium的底层通信协议标准，并在它的基础上增加了移动端自动化的通信协议
在代码层面上，也继承了selenium中webdriver。
在元素定位上也是继承了selenium的定位类，并在它的基础上添加移动端的定位方法
```

**解析**

```text
【核心考点】 Appium Selenium 自动化测试框架
【题目解析】
本题考察对Appium和Selenium两个主流自动化测试框架的理解，包括它们的区别和联系。Appium是移动端自动化框架，Selenium是Web端自动化框架，但Appium基于Selenium的通信协议和API设计，两者在底层架构上有继承关系。
【参考答案要点】
区别：
1. 应用领域不同：Appium用于移动端App（iOS/Android）自动化测试，Selenium用于Web网页自动化测试。
2. 架构不同：Appium包含代码客户端和独立服务端（命令行或桌面应用），服务端将操作请求发送到手机端，由手机端调用系统原生测试框架执行；Selenium则通过浏览器驱动程序直接操作浏览器。
关系：
Appium并未重新实现底层通信协议，而是直接延用了Selenium的WebDriver协议标准，并在其基础上扩展了移动端特有的操作协议（如触摸、手势等）。在代码层面，Appium的客户端库也继承了Selenium的WebDriver类，因此API风格高度相似。
【面试角度】
回答时如果能提及实际使用经验，例如“在项目中，我们使用Appium进行Android App的回归测试，其定位元素的方式与Selenium类似，但增加了对原生控件的支持”，会显得更专业。
【延伸知识】
Appium支持跨平台测试，同一套代码可运行在iOS和Android上；Selenium支持多种浏览器（Chrome、Firefox等）。两者都支持多种编程语言（Java、Python等）。
```

---

## Q003186

- 题型：简答
- 难度：中等

**题目**

```text
App自动化自己搭的框架里面是有logger那些还有用例不通过时屏幕截图用到哪个库？
```

**答案**

```text
截图可以使用 appium 框架当中的 save_screentshot_as_file 等方法。日志的话，可以使用logging或者loguru库。
```

**解析**

```text
【核心考点】 Appium框架 日志处理 截图方法
【参考答案要点】
1. 截图：使用Appium的save_screenshot_as_file方法，或WebDriver的get_screenshot_as_file方法，将截图保存到指定路径。
2. 日志：使用Python的logging模块或第三方库loguru，配置日志级别、格式和输出，便于调试和记录测试过程。
【面试角度】
回答时建议结合实际框架设计，例如在用例失败时自动截图并记录日志，展示对异常处理的考虑。可提及使用pytest的钩子函数实现自动化截图。
【延伸知识】
Appium还支持get_screenshot_as_base64获取截图base64编码，便于嵌入报告。日志库loguru相比logging更简洁，支持彩色输出和自动轮转，适合快速搭建测试框架。
```

---

## Q003189

- 题型：简答
- 难度：中等

**题目**

```text
app自动化这部分，你主要用的什么框架？
```

**答案**

```text
app自动化主要使用的开源框架appium，结合测试框架pytest，还有PO设计思想，共同搭建了app自动化测试框架。
其中有对于app的基本操作进行二次封装，并加入了日志记录用例执行过程，和对于报错的异常截图处理
```

**解析**

```text
【核心考点】 App自动化 Appium PO设计模式 pytest
【题目解析】
本题考查App自动化测试框架的选型与设计。Appium是主流开源框架，支持跨平台；pytest是Python测试框架，提供灵活的参数化和断言；PO（Page Object）设计模式用于封装页面元素和操作，提高代码可维护性。
【参考答案要点】
1. 框架组成：Appium作为底层驱动，pytest作为测试执行框架，PO模式组织页面对象。
2. 封装内容：对App的基本操作（如点击、滑动）进行二次封装，加入日志记录和异常截图处理，便于调试和报告。
3. 优势：提高用例复用性，降低维护成本，支持数据驱动和并发执行。
【面试角度】
回答时建议突出设计思路，例如“我们通过PO模式将页面元素定位与业务逻辑分离，当UI变更时只需修改对应Page类”。
【延伸知识】
还可以结合CI/CD流程，将App自动化集成到Jenkins中，实现定时或代码触发执行。
```

---

## Q003190

- 题型：简答
- 难度：中等

**题目**

```text
app自动化这部分，你主要用的是什么框架？
```

**答案**

```text
app自动化，主要是使用了appium开源库，pytest测试框架，allure测试报告搭建的自动化框架，对app页面通用的操作封装成了basepage，加入了日志记录用例执行过程，和失败截图的功能 。
```

**解析**

```text
【核心考点】 App自动化测试框架 Appium Pytest
【参考答案要点】
1. 框架组成：使用Appium作为移动端自动化驱动，Pytest作为测试执行框架，Allure生成测试报告。
2. 封装设计：对App页面通用操作（如点击、滑动、输入等）封装为BasePage基类，提高代码复用性。
3. 日志与截图：集成日志记录用例执行过程，失败时自动截图，便于问题定位。
【面试角度】
回答此类问题时，建议结合实际项目经验说明框架的搭建细节，例如如何管理元素定位、如何处理等待机制、如何实现多设备并行等，能体现技术深度。
【延伸知识】
Appium基于WebDriver协议，支持iOS和Android；Pytest的fixture和参数化功能可大幅提升用例维护效率；Allure支持历史趋势和分类统计，是面试高频亮点。
```

---

## Q003191

- 题型：单选
- 难度：中等

**题目**

```text
下列关于Appium的描述正确的是（）
```

**选项**

```text
A. Appium自动化测试需要重新编译App
B. Appium Server 只支持Linux平台
C. Appium同时封装了UiAutomator 和Instrumentation
D. Appium主要用来对移动App做性能测试
```

**答案**

```text
C
```

**正确选项**

```text
C. Appium同时封装了UiAutomator 和Instrumentation
```

**解析**

```text
【核心考点】 Appium 移动测试 自动化测试
【题目解析】
本题考查Appium框架的基本概念。Appium是一个跨平台移动自动化测试工具，支持Android和iOS。它基于Client-Server架构，通过WebDriver协议与设备交互。在Android端，Appium封装了UiAutomator（API 16+）和Instrumentation（旧版本）两种自动化引擎。
【选项解析】
✗ A. Appium自动化测试需要重新编译App — 错误。Appium支持不重新编译App，通过Appium Inspector或uiautomatorviewer定位元素，无需修改源码。
✗ B. Appium Server 只支持Linux平台 — 错误。Appium Server是跨平台的，支持Windows、macOS、Linux。
✓ C. Appium同时封装了UiAutomator 和Instrumentation — 正确。Appium在Android端使用UiAutomator2（默认）或Instrumentation（旧版）驱动。
✗ D. Appium主要用来对移动App做性能测试 — 错误。Appium主要用于功能测试和回归测试，性能测试通常使用JMeter、Monkey等工具。
【易错提示】
常见误区：认为Appium需要重新编译App（A选项），或认为Appium只能做性能测试（D选项）。实际上Appium的核心优势是跨平台和无需修改App。
```

---

## Q003192

- 题型：简答
- 难度：中等

**题目**

```text
使用Appium可能遇到的错误是什么？
```

**答案**

```text
可能遇到的问题：
错误1：需要以下所需的功能，但不提供：设备名称，platformName
错误2：找不到adb，请使用Android SDK根目录路径设置ANDROID_HOME环境变量
错误3：openqa.selenium.SessionNotCreatedException：无法创建新的会话
```

**解析**

```text
【核心考点】 Appium环境配置 移动端测试
【参考答案要点】
1. 缺少必要参数：如未提供设备名称（deviceName）或平台名称（platformName），Appium无法识别目标设备，会抛出异常。
2. ANDROID_HOME环境变量未设置：Appium依赖adb工具，若环境变量缺失，会报"找不到adb"错误，需配置Android SDK路径。
3. Session创建失败：如openqa.selenium.SessionNotCreatedException，通常由Capabilities配置错误、Appium版本不兼容或设备连接问题导致。
【面试角度】
回答时建议结合实际调试经验，例如"我在项目中遇到ANDROID_HOME未配置时，通过设置系统变量解决"，能体现问题排查能力。
【延伸知识】
Appium启动前需确保adb devices能识别设备，且Appium Server版本与客户端库匹配。常见错误还包括端口冲突（如4723被占用）和Appium Inspector连接失败。
```

---

## Q003193

- 题型：简答
- 难度：中等

**题目**

```text
请描述Appium来做Android平台自动化测试原理
```

**答案**

```text
Appium要能真正自动化手机上的应用必须依赖于各个移动平台所带的自动化框架；
IOS 、Android都有自己的框架， IOS9.3以前用的框架是 uiautomation ，现在用的是XCUITest;
Android用的是 uiautomator,现在最新的有个uiautomator2。
框架提供的是运行库，运行库运行在移动设备上。
```

**解析**

```text
【核心考点】 Appium 移动自动化测试 自动化原理
【参考答案要点】
Appium通过WebDriver协议与移动设备通信，其原理如下：
1. 客户端发送请求：测试脚本通过Appium客户端库发送HTTP请求到Appium Server。
2. Appium Server解析：Server将请求转换为对应平台的自动化指令。
3. 平台框架执行：Android使用UIAutomator/UIAutomator2，iOS使用XCUITest，这些框架在设备上执行操作并返回结果。
4. 返回响应：结果通过Server返回给客户端。
【面试角度】
回答时强调跨平台特性和无需修改应用代码的优势，体现对Appium架构的深入理解。
【延伸知识】
Appium支持多种语言编写脚本，如Java、Python、JavaScript等，且兼容真机和模拟器，是业界主流的移动自动化框架。
```

---

## Q003194

- 题型：简答
- 难度：中等

**题目**

```text
请简述Appium的工作原理，以及它的优缺点。
```

**答案**

```text
Appium分为client端（通过Java编写的代码，也可以通过其他语言编写），Appium指令服务器，sdk通信环境或移动端设备。
Client端发送自动化指令给Appium server，Appium Server接收到client发送的指令后，转换为移动端能够识别的指令，然后发送给移动端设备，并对移动端设备进行操作。
appium 的优点有：跨平台、多语言、开源、统一的API、更新速度快。
缺点有：
一、不太稳定，尤其是长时间运行后，
二、中文输入不太友好，
三、运行效率比较慢
四、手机系统高低版本切换的时候比较麻烦
五、有些控件无法识别
```

**解析**

```text
【核心考点】 Appium 移动测试
【参考答案要点】
工作原理：Appium采用Client-Server架构。Client端（如Java代码）发送自动化指令给Appium Server；Server将指令转换为移动端能识别的指令（如UI Automator或XCUITest），并发送给移动设备执行；执行结果返回Server再传回Client。
优点：跨平台（iOS/Android）、多语言支持、开源免费、统一API、社区活跃、更新快。
缺点：稳定性较差（尤其长时间运行）、中文输入支持不友好、运行效率较慢、高低版本切换麻烦、部分控件无法识别。
【面试角度】
回答时，建议结合实际使用经验，例如：“在项目中，我们使用Appium进行回归测试，遇到中文输入问题时，通过修改输入法配置解决。” 这能体现问题解决能力。
【延伸知识】
Appium基于WebDriver协议，支持Selenium Grid实现分布式测试，提升执行效率。此外，其Inspector工具可用于元素定位。
```

---

## Q003188

- 题型：简答
- 难度：较难

**题目**

```text
appium 的工作原理是什么
```

**答案**

```text
安卓：

appuim 基于 uiautomator2 的原理
appium 服务启动后默认在 4723 端口上创建一个 http 服务，脚本通过服务地址
http://xxxx:4723/wd/hub 和 appium 进行通信
在 初 始 化 脚 本 和 appium 连 接 的 过 程 中 appium 会 向 手 机 就 安 装 辅 助 app
uiautomator2.server.apk 和 uiautomator2.server.test.apk，并且做端口转发 adb forward tcp
8200 tcp 6790,安装以后会在手机上启动 uiautomator2 的 server，这个 server 启动后会
在手机上创建一个 netty server，端口是 6790，appium 和手机上的 uiautomator2 server
的 6790 端口进行通信，把从 4723 端口收到的脚本指令通过 8200 端口转发到手机的 6790
端口上

IOS 手机：
Appium 服务启动后默认在 4723 端口上创建一个 http 服务，脚本通过服务地址
http://xxxx:4723/wd/hub 和 appium 进行通信
在初始化脚本和 appium 连接的过程中会向手机编译安装 webdriveragent app，并且启
动 wda 在手机上创建一个基于 8100 的 http 服务，appuim 通过 4723 的端口接收到脚本传递
的指令，appium 再通过本地的 8100 端口将收到的指令转发给手机上 8100 wda 服务，wda
服务接收到指令再去操作待测 app，操作完成后返回给 appium 操作结果，appium 再将结果
返回给脚本
```

**解析**

```text
【核心考点】 Appium架构 移动端自动化
【题目解析】
本题考查Appium框架在Android平台的工作原理，重点在于理解客户端-服务端通信机制、辅助应用部署及端口转发流程。Appium基于WebDriver协议，通过HTTP接口与设备交互，底层依赖UIAutomator2实现元素定位和操作。
【参考答案要点】
1. 服务启动：Appium服务默认在4723端口创建HTTP服务，脚本通过http://xxxx:4723/wd/hub发送请求。
2. 初始化连接：Appium向手机安装辅助APK（uiautomator2.server.apk和uiautomator2.server.test.apk），并执行端口转发adb forward tcp:8200 tcp:6790。
3. 通信执行：手机端启动UIAutomator2服务，接收Appium指令并执行自动化操作，结果通过转发端口返回。
【面试角度】
回答时建议结合实际项目中的设备连接问题，例如端口冲突或APK版本不匹配导致的初始化失败，能体现问题排查能力。
【易错提示】
注意区分Appium与Selenium的通信差异，Appium需额外处理设备端组件部署，而Selenium直接驱动浏览器。
```

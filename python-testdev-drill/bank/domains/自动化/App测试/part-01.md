# 自动化 · App测试

> 共 12 题 · 所属领域：自动化 · 专题：App测试

---

## Q003196

- 题型：简答
- 难度：入门

**题目**

```text
App自动化用的是真机还是虚拟机？
```

**答案**

```text
在实际测试过程中都会用到。
```

**解析**

```text
【核心考点】 App自动化测试环境 真机 vs 模拟器
【参考答案要点】
在实际测试过程中，真机和虚拟机都会用到。真机用于验证真实用户场景、硬件兼容性（如GPS、指纹、摄像头等）；虚拟机（模拟器）用于快速迭代测试、多版本覆盖、CI/CD集成。通常策略是：模拟器跑冒烟和回归，真机跑验收和兼容性。
【面试角度】
建议结合项目经验说明选择依据：例如“我们项目使用Genymotion模拟器做日常功能测试，发布前在5款主流真机上做兼容性测试”。还可提及模拟器的局限（如无法测试真机特有功能、性能差异），展示对测试环境的深入理解。
【延伸知识】
常见的模拟器方案：Android自带AVD、Genymotion、夜神；iOS只能用Xcode模拟器。云真机平台（如Testin、Firebase Test Lab）可弥补真机覆盖不足。
```

---

## Q003197

- 题型：简答
- 难度：简单

**题目**

```text
app自动化你们一般用什么工具定位元素？
```

**答案**

```text
Android SDK自带的UIAutomatorViewer或者Appium检查器
```

**解析**

```text
【核心考点】 App自动化 元素定位工具
【题目解析】
本题考查App自动化测试中元素定位工具的掌握情况。Android和iOS平台各有常用工具。
【参考答案要点】
1. Android：常用Android SDK自带的UIAutomatorViewer，可查看UI元素属性。
2. 跨平台：Appium Inspector（Appium检查器）支持Android和iOS，提供可视化元素定位。
3. 其他：如Selendroid、Robotium等，但UIAutomatorViewer和Appium Inspector最常用。
【面试角度】
建议结合实际使用经验，如“我用UIAutomatorViewer定位元素后，在Appium脚本中使用XPath”，展示工具链整合能力。
【延伸知识】
还可提及iOS的Accessibility Inspector，以及使用ID、ClassName、XPath等定位策略的优缺点。
```

---

## Q003198

- 题型：单选
- 难度：简单

**题目**

```text
下列哪个不是移动APP测试的自动化测试框架？（）
```

**选项**

```text
A. MonkeyRunner
B. Appium
C. UiAutomator
D. Selenium
```

**答案**

```text
D
```

**正确选项**

```text
D. Selenium
```

**解析**

```text
【核心考点】 移动测试框架 自动化测试
【题目解析】
本题考查移动APP自动化测试框架的识别。选项中，MonkeyRunner、Appium、UiAutomator均为移动端测试框架，而Selenium主要用于Web端自动化测试，不适用于移动APP原生应用（但可通过Appium等扩展支持移动端）。因此，Selenium不是移动APP测试的自动化框架。
【选项解析】
✗ A. MonkeyRunner — 错误。MonkeyRunner是Android SDK自带的测试工具，可用于移动端自动化。
✗ B. Appium — 错误。Appium是跨平台移动端自动化测试框架，支持iOS和Android。
✗ C. UiAutomator — 错误。UiAutomator是Android的UI自动化测试框架。
✓ D. Selenium — 正确。Selenium主要用于Web浏览器自动化，不直接用于移动APP测试。
【易错提示】
注意Selenium WebDriver可通过Appium扩展支持移动端，但Selenium本身是Web测试框架，不是移动APP框架。
```

---

## Q003203

- 题型：简答
- 难度：简单

**题目**

```text
简述ulautomatorviewer原理（无需解释底层原理，简述工作流程即可）
```

**答案**

```text
android SDK自带的元素定位工具，可以将当前连接到你电脑上的手机屏幕进行一个快照，然后可以看到手机当前页面的层级关系和每个控件的属性
```

**解析**

```text
【核心考点】 Android测试工具 UI自动化
【题目解析】
本题考查Android SDK自带的UI自动化测试工具uiautomatorviewer的工作原理。该工具用于分析当前应用界面的UI元素层次结构，帮助测试人员定位元素属性。
【参考答案要点】
1. 连接设备：通过adb连接Android设备或启动模拟器。
2. 截取屏幕快照：uiautomatorviewer对当前设备屏幕进行截图，并获取当前页面的UI布局信息。
3. 解析布局文件：工具解析系统返回的XML布局文件，展示界面元素的层级关系和属性（如resource-id、class、text等）。
4. 交互分析：用户点击界面上的元素，工具高亮显示对应节点及其属性，便于定位元素编写自动化脚本。
【面试角度】
面试官可能追问uiautomatorviewer的局限性，例如无法动态获取WebView内容、对动态加载元素支持不足等，展示对工具的深入理解。
【易错提示】
常见误解：uiautomatorviewer只能用于真机，实际上也支持模拟器；另外它仅提供静态分析，无法模拟用户操作。
```

---

## Q003204

- 题型：简答
- 难度：简单

**题目**

```text
请列举App页面中常见的布局及控件
```

**答案**

```text
常见的布局：
线性布局LinearLayout、表格布局TableLayout、相对布局RelativeLayout、帧布局FrameLayout、绝对布局AbsoluteLayout
常见的控件：
TextView 显示文字，文本控件
ImageView 显示图片
EditText 输入框
Button 按钮
CheckBox 复选框
RadioButton 单选按钮
ProgressBar 加载进度条
```

**解析**

```text
【核心考点】 App测试 UI布局 控件识别
【参考答案要点】
常见布局：
1. 线性布局（LinearLayout）— 按水平或垂直方向排列子元素。
2. 相对布局（RelativeLayout）— 基于相对位置定位子元素。
3. 帧布局（FrameLayout）— 子元素堆叠显示。
4. 表格布局（TableLayout）— 以行和列组织子元素。
5. 绝对布局（AbsoluteLayout）— 通过坐标精确控制位置（已较少使用）。
常见控件：
1. TextView — 显示文本。
2. EditText — 输入文本。
3. Button — 按钮，触发点击事件。
4. ImageView — 显示图片。
5. CheckBox — 复选框，支持多选。
6. RadioButton — 单选按钮，需配合RadioGroup使用。
7. ProgressBar — 进度条，显示加载状态。
【面试角度】
回答时建议结合实际测试经验，例如“在测试登录页面时，我常检查EditText的输入限制和Button的点击反馈”，能体现对控件特性的理解。
【延伸知识】
Android布局和控件是UI自动化测试的基础，如使用Appium定位元素时需熟悉其属性（如resource-id、class name）。建议掌握常用控件的测试要点，如EditText的边界值、Button的响应时间等。
```

---

## Q003205

- 题型：简答
- 难度：简单

**题目**

```text
请简单介绍一下使用过的安卓UI自动化测试工具？
```

**答案**

```text
appium：
是一个移动端的自动化框架，可用于测试原生应用，移动网页应用和混合型应用，且是跨平台的。
robotium：
是一款国外的Android自动化测试框架，主要针对Android平台的应用进行黑盒自动化测试，它提供了模拟各种手势操作（点击、长按、滑动等）、查找和断言机制的API，能够对各种控件进行操作。
```

**解析**

```text
【核心考点】 移动端自动化测试工具 Appium Robotium
【参考答案要点】
Appium： 是一个跨平台的移动端自动化测试框架，支持原生应用、移动网页应用和混合型应用。它基于WebDriver协议，支持多语言（如Java、Python）编写脚本，具有跨平台（iOS、Android）和无需重新编译应用的特点。
Robotium： 是一款针对Android平台的黑盒自动化测试框架，提供模拟手势操作（点击、长按、滑动等）、查找和断言机制的API。它适用于原生和混合应用，但仅支持Android，且需要应用源码或签名包。
【面试角度】
回答此类问题时，建议结合实际项目经历举例说明，例如“在项目中，我使用Appium进行跨平台回归测试，利用其元素定位策略提高了脚本稳定性”，能有效提升答案深度。
【延伸知识】
Appium与Robotium的主要区别在于：Appium支持跨平台，无需修改应用代码，但速度较慢；Robotium仅限Android，但执行速度快，且支持更底层的操作。面试中常被问及选择依据，建议从项目需求、平台兼容性和性能角度分析。
```

---

## Q003199

- 题型：简答
- 难度：中等

**题目**

```text
在App页面中经常有很多提示信息弹出来，请问这些提示信息（toast）怎么获取到？
```

**答案**

```text
获取toast信息要求：

Android系统版本5.1+
获取方式：
(1) 设置Appium执行引擎为UIAutomator2
desiredCapabilities.setCapabiliy(“automationName”,”UIAutomator2”);
(2) 通过xpath表达式获取toast文本信息
//*[contains(@text,"文本值")]
```

**解析**

```text
【核心考点】 Appium自动化测试 Toast元素定位 移动测试
【题目解析】
本题考查移动端自动化测试中Toast提示信息的获取方法。Toast是一种轻量级消息提示，通常几秒后自动消失，传统元素定位方式难以捕获。题目要求说明获取方式，属于中等难度的实践题。
【参考答案要点】
1. 前提条件：Android系统版本需5.1及以上，且Appium执行引擎需设置为UIAutomator2（通过desiredCapabilities.setCapability("automationName", "UIAutomator2")）。
2. 获取方式：使用XPath表达式定位Toast元素，例如//*[contains(@text,"文本值")]，其中"文本值"为期望的Toast内容。由于Toast是瞬时元素，需在出现时立即捕获，通常结合显式等待（如WebDriverWait）使用。
3. 注意事项：Toast元素属于系统级别的UI组件，无法通过常规的ID或ClassName定位；UIAutomator2引擎相比默认引擎对Toast支持更好。
【面试角度】
回答时建议补充实际测试场景，例如"在测试登录功能时，我们通过捕获Toast提示'登录成功'来验证用例通过"，并提及等待策略（如设置等待时间3秒）以确保Toast出现时能成功定位。此外，可讨论iOS端Toast获取的差异（iOS使用UIAutomation引擎）。
【易错提示】
常见误区：尝试用常规元素定位方法（如findElementById）获取Toast，或未设置UIAutomator2引擎导致定位失败。注意Toast文本可能包含特殊字符，需转义处理。
```

---

## Q003202

- 题型：简答
- 难度：中等

**题目**

```text
如何获取到测试App的包名及入口类名？
```

**答案**

```text
通过android SDK自带的aapt工具，对应的命令aapt dump badging APK路径解析得到
在结果中搜索package-name即为对应的包名
搜索lunchable-activity即为对应的入口类名
```

**解析**

```text
【核心考点】 Android测试 APK解析
【题目解析】
在Android测试中，获取应用的包名和入口Activity是进行自动化测试、性能测试或手动测试的基础。常用方法是通过Android SDK中的aapt工具解析APK文件。
【参考答案要点】
1. 使用aapt工具：Android SDK自带的aapt（Android Asset Packaging Tool）可以解析APK文件。
2. 命令格式：aapt dump badging <APK路径>
3. 解析结果：在输出中搜索package: name=获取包名，搜索launchable-activity: name=获取入口Activity类名。
【面试角度】
面试官可能追问其他方法，如使用Android Studio的Profile或adb命令，或通过反编译工具查看AndroidManifest.xml，展示知识广度。
【易错提示】
注意aapt命令需要配置环境变量，且APK文件路径需正确；另外，不同版本的aapt输出格式可能略有差异。
```

---

## Q003206

- 题型：简答
- 难度：中等

**题目**

```text
请简单介绍你曾使用过的一款 APP 自动化测试工具 ？
```

**答案**

```text
开放性问题，带点主观意见
1.对比其他熟悉的自动化工具的优缺点
2.自动化的简要方案（简要的同时关键内容请具体）。（提示： appnium 等）
```

**解析**

```text
【核心考点】 APP自动化测试 工具选型
【参考答案要点】
这是一道开放性问题，建议从以下角度回答：
1. 工具介绍：例如 Appium，支持跨平台（iOS/Android），基于 WebDriver 协议，支持多种编程语言。
2. 优缺点对比：与同类工具如 Airtest、Robot Framework 对比，突出 Appium 的灵活性和社区支持。
3. 自动化方案：简要描述测试框架搭建、元素定位策略、测试用例设计及持续集成集成。
【题目解析】
此类问题考察候选人的实际项目经验和技术深度。回答时应避免空泛，需结合具体工具版本、遇到的问题及解决方案。例如提到 Appium 时，可说明如何解决元素定位不稳定、多设备并行测试等挑战。
【面试角度】
面试官期望看到候选人对工具原理的理解，而非简单罗列功能。建议提及 Appium 的会话管理、隐式等待策略等细节，并说明在项目中如何权衡工具选型。
【延伸知识】
除 Appium 外，还可了解 Espresso（Android原生）、XCUITest（iOS原生）及基于图像识别的 Airtest，不同场景下工具选择差异较大。
```

---

## Q003195

- 题型：简答
- 难度：较难

**题目**

```text
App自动化有做过吗？知道用到哪些技术框架吗？
```

**答案**

```text
实话实说，但即使没做过，appium这个app测试框架肯定是要知道的，现在主流的安卓app测试框架就是appium，如果还知道uiautomator,weditor就更好了
```

**解析**

```text
【核心考点】 App自动化测试 测试框架
【题目解析】
本题考查候选人对App自动化测试的实际经验和知识广度。即使没有实际项目经验，也应了解主流框架和工具。
【参考答案要点】
1. 主流框架：Appium是目前最主流的跨平台App自动化测试框架，支持Android和iOS，基于WebDriver协议。
2. 其他工具：
- UiAutomator：Android原生测试框架，适用于Android 4.3+。
- Espresso：Google官方Android测试框架，适合白盒测试。
- XCUITest：Apple官方iOS测试框架。
- Weditor：基于Python的App元素定位工具，常与Appium配合使用。
【面试角度】
如果没有实际经验，建议坦诚说明，但展示学习意愿和知识储备，例如：“我了解Appium的原理和基本使用，自学过相关教程，并搭建过Demo环境。”同时可提及对元素定位策略（如ID、XPath、Accessibility ID）的理解。
【延伸知识】
高级话题包括：Appium的Desired Capabilities配置、真机与模拟器测试、Appium与Selenium Grid集成、持续集成（CI）中的App自动化等。了解这些能体现深度。
```

---

## Q003200

- 题型：简答
- 难度：较难

**题目**

```text
如何在App的滑动列表ListView找到对应的元素并点击？
```

**答案**

```text
在java-client中并没有提供ScrollTo方法，不要和JS弄混淆。
Appium可以使用uiautomator的
new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches(\"" + selector + "\").instance(0))
```

**解析**

```text
【核心考点】 Appium 滑动列表 元素定位
【题目解析】
本题考察Appium中处理滑动列表（如ListView）的元素定位技巧。由于列表项可能不在当前屏幕可见范围内，需使用滚动操作来查找元素。Java-Client未直接提供ScrollTo方法，需借助UIAutomator的API实现。
【参考答案要点】
使用UIAutomator的滚动方法：new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches("元素文本").instance(0))。此方法会滚动到目标元素可见，然后可通过Appium的findElement定位并点击。
【面试角度】
面试官可能追问性能优化，如“如果列表很长，如何减少滚动次数？”可回答结合index或使用显式等待，提升脚本稳定性。
【延伸知识】
Appium还支持通过MobileElement的swipe方法模拟滑动，但UIAutomator方法更高效，适合复杂列表。
```

---

## Q003201

- 题型：简答
- 难度：较难

**题目**

```text
如何在App的滑动列表（ListView）中找到对应的元素并点击
```

**答案**

```text
Appium可以使用UIAutomator的原生方法：
new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches(\"" + selector + "\").instance(0))
```

**解析**

```text
【核心考点】 Appium UI自动化 滑动列表 UIAutomator
【题目解析】
本题考查在移动端UI自动化测试中，如何处理可滚动的列表（如ListView、RecyclerView）中元素的定位和点击。由于列表中的元素可能不在当前屏幕可视区域内，直接使用常规的findElement方法会失败，需要先滚动到目标元素所在位置。Appium提供了多种滚动策略，其中利用UIAutomator的原生方法是一种高效的方式。
【参考答案要点】
方法一（UIAutomator原生方法）：使用new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches("文本内容").instance(0))，先找到可滚动的控件，然后滚动到匹配文本的元素，最后再执行点击。
方法二（Appium的MobileElement方法）：使用driver.findElement(MobileBy.AndroidUIAutomator("new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\"文本内容\"))"))，然后点击。
方法三（使用TouchAction或W3C Actions）：通过坐标滑动，逐步滚动列表，直到目标元素出现，但这种方法不稳定且效率低。
【面试角度】
回答时建议强调实际项目中的最佳实践，例如优先使用UIAutomator原生方法，因为它性能好且稳定。同时，可以提及如果列表是动态加载的，需要增加等待机制。另外，iOS平台对应的是XCUITest的滚动方法，能体现跨平台能力。
【延伸知识】
Appium 2.0 中推荐使用W3C WebDriver协议，对于滚动操作，可以使用new Actions(driver).scrollToElement(element).perform()，但底层实现仍依赖于平台原生方法。
```

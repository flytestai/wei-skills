# Selenium与UI自动化题

> 独立模块：Selenium与UI自动化题（中小厂自动化岗核心模块）
> 来源：selenium 4 面经真题、UI 自动化实战、POM 设计模式。

## 一、元素定位（必考）

### 1. 有哪些元素定位方式，优先级怎么排
- tags: 定位, 必考
- difficulty: easy
- frequency: 高频
- prompt: Selenium 有哪些元素定位方式？你怎么选？
- answer: 八种：id、name、class name、tag、link text、partial link text、xpath、css。优先级：id（唯一最快）> 语义化 css（如 [data-testid]）> xpath。绝不依赖动态 class 和绝对路径 xpath（//div[1]/div[2]/span 这种改版即崩）。Selenium 4 写法：driver.find_element(By.ID, "xx")。

### 2. xpath 的常用写法
- tags: xpath, 高频
- difficulty: medium
- frequency: 高频
- prompt: 手写几个常用的 xpath。
- answer: 绝对路径 /html/body/div（不用）；相对路径 //input[@id='kw']；文本定位 //button[text()='登录']；包含 //div[contains(@class,'item')]；父子 //div[@id='list']/a；轴 //a following-sibling::div（兄弟）。测试岗最常考 contains 和 text() 两种。

### 3. 动态元素怎么定位
- tags: 定位, 必考
- difficulty: medium
- frequency: 高频
- prompt: 元素 id 是动态变化的（如 id="btn-12345"），怎么定位？
- answer: 三招：①xpath/css 用属性前缀或包含匹配：[starts-with(@id,'btn-')] 或 contains；②找稳定锚点：先定位不变的父容器，再相对定位子元素；③让开发加 data-testid 这种测试专用属性（最推荐，提需求也是测开的职责）。

## 二、等待策略（必考）

### 4. 三种等待的区别
- tags: 等待, 必考
- difficulty: easy
- frequency: 高频
- prompt: 强制、隐式、显式等待的区别？你用哪种？
- answer: sleep(3)：写死，浪费且不可靠；implicitly_wait(10)：全局一次，只判断存在不判断可点，且与显式混用会叠加；WebDriverWait+EC：针对单元素等特定条件（可点击/可见/消失），最精准。实践：显式为主，个别场景 sleep 兜底，隐式禁用。

### 5. 显式等待的代码怎么写
- tags: 等待, 代码
- difficulty: easy
- frequency: 高频
- prompt: 手写显式等待，等元素可点击再点击。
- answer: from selenium.webdriver.support.ui import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC; WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login"))).click()。讲清 10 是最长等待时间，条件满足立即通过。

## 三、核心 API 与弹窗处理

### 6. 怎么处理 alert 确认框
- tags: 弹窗, 高频
- difficulty: easy
- frequency: 高频
- prompt: 原生 alert 弹窗怎么处理？
- answer: alert = driver.switch_to.alert，然后 alert.accept() 确认或 alert.dismiss() 取消，alert.text 取内容。坑：JS 弹窗不是 DOM 元素，find_element 定位不到，必须走 switch_to.alert。

### 7. iframe 里的元素定位不到怎么办
- tags: iframe, 必考
- difficulty: easy
- frequency: 高频
- prompt: 元素明明在页面上，find_element 却报 NoSuchElementException，可能是什么原因？
- answer: 第一嫌疑：元素在 iframe 里。driver.switch_to.frame(iframe元素或name/id) 切进去再定位，完了 switch_to.default_content() 切回主文档。其他可能：页面未加载完（等待不够）、元素在新窗口（要 switch_to.window）、定位方式在动态渲染下失效。

### 8. 多窗口/多标签页怎么切换
- tags: 窗口, 中高频
- difficulty: easy
- frequency: 中高频
- prompt: 点击链接打开了新标签页，怎么在新页面操作？
- answer: driver.current_window_handle 先存旧句柄；点击后 driver.window_handles 拿全部句柄；遍历找新句柄 driver.switch_to.window(handle)；操作完切回旧句柄。坑：不切句柄的话 driver 还在旧页面操作，元素找不到。

### 9. select 下拉框怎么操作
- tags: 表单, 中高频
- difficulty: easy
- frequency: 中高频
- prompt: 原生 select 下拉框怎么选值？
- answer: from selenium.webdriver.support.select import Select；Select(element).select_by_visible_text("上海") 或 by_value/by_index。坑：非原生 select（div 模拟的）必须先点击展开再点击选项，Select 类无效。

### 10. 怎么截图和执行 JS
- tags: API, 中高频
- difficulty: easy
- frequency: 中高频
- prompt: UI 自动化失败时怎么截图？怎么用 JS 操作页面？
- answer: 截图 driver.get_screenshot_as_file("fail.png")（失败钩子里自动截，配 Allure 附件）；JS：driver.execute_script("arguments[0].scrollIntoView();", element) 滚动到元素、execute_script("window.scrollTo(0,500)")、JS 点击 element.click() 处理被遮挡元素。

## 四、浏览器与执行优化

### 11. 无头模式是什么，为什么要用
- tags: 无头, 高频
- difficulty: easy
- frequency: 高频
- prompt: 什么是无头浏览器？CI 里为什么要用？
- answer: 无头 = 不渲染可见界面的浏览器（options.add_argument("--headless")），占资源少、速度快。CI 服务器（Linux 容器）没有图形界面，必须无头跑。坑：无头下屏幕分辨率默认很小，截图可能异常，要加 --window-size=1920,1080。

### 12. 怎么提升 UI 自动化执行速度
- tags: 性能, 中高频
- difficulty: medium
- frequency: 中高频
- prompt: UI 自动化跑得慢，怎么提速？
- answer: ①无头模式；②砍掉 sleep 全换显式等待（每处 sleep 3 秒 × 100 用例就是 5 分钟）；③并发：pytest-xdist 多进程分跑（注意登录态和数据隔离）；④精简用例：只留核心链路，细节验证下沉到接口层；⑤复用登录：session 级 fixture 登录一次。

## 五、框架设计（POM 必考）

### 13. 什么是 PO 模式（Page Object）
- tags: POM, 必考
- difficulty: medium
- frequency: 高频
- prompt: 什么是 Page Object 设计模式？为什么要用？
- answer: 每个页面封装成一个类：属性是定位器、方法是页面操作（login_page.input_user()）。三层价值：①元素改了只改页面类一处，不改用例；②用例只写业务流程，可读性高；③页面操作可复用。标配：BasePage 封装点击/输入/等待/截图，业务页继承。

### 14. BasePage 基类怎么设计
- tags: POM, 框架
- difficulty: medium
- frequency: 高频
- prompt: 手写一个 BasePage 的核心结构。
- answer: class BasePage: __init__(self, driver) 存 driver；封装 click(locator)（显式等待+点击+失败截图）、input(locator, text)、wait_element(locator, timeout)。加分点：click 里带 try 和截图钩子，失败自动存证。

### 15. UI 自动化怎么做数据驱动
- tags: 数据驱动, 中高频
- difficulty: medium
- frequency: 中高频
- prompt: UI 自动化怎么参数化多组数据？
- answer: pytest 参数化 + YAML/Excel 数据源：yaml 存用户名密码组合，parametrize 拉平后每条数据跑一次登录流程，ids 显示用例名。跟接口自动化数据驱动思路一致，只是动作换成了 UI 操作。

### 16. 什么时候该用 UI 自动化而不是接口自动化
- tags: 测试策略, 必考
- difficulty: easy
- frequency: 高频
- prompt: 什么场景必须 UI 自动化？
- answer: 接口测不了的：①页面渲染正确性（样式、布局、控件交互）；②端到端核心链路验收（登录-下单-支付全链走通）；③前端 JS 逻辑（表单联动、校验提示）。其余业务规则尽量下沉接口层。口诀：UI 保链路，接口保逻辑。

## 六、Selenium 底层认知（加分项）

### 17. Selenium 的原理是什么
- tags: 原理, 加分
- difficulty: medium
- frequency: 中高频
- prompt: Selenium 是怎么驱动浏览器的？
- answer: 三件套：浏览器驱动（chromedriver）+ WebDriver 协议（W3C 标准的 HTTP REST 接口）+ 浏览器。client（你的 Python 代码）向 chromedriver 发 HTTP 请求（如 POST /session/xx/element），driver 解析后操作浏览器，返回结果。所以：driver 版本必须和浏览器版本匹配；多台机器跑 = driver 各自跑各自浏览器（天然支持分布式/网格）。

### 18. selenium 和 playwright 怎么选
- tags: 工具选型, 中高频
- difficulty: medium
- frequency: 中高频
- prompt: 新项目选 Selenium 还是 Playwright？
- answer: 中小厂现状：存量项目 Selenium 多，但新项目 Playwright 趋势明显。Playwright 优势：自动等待元素（内置 auto-wait，直接消灭大部分 flaky）、多语言 API 统一、自带 trace/screenshot 录制、速度更快、支持多浏览器（含 webkit）。Selenium 优势：生态成熟、招聘好找人、资料多。面试答法：两个都熟，新项目倾向 Playwright。

# AI测试赋能 · 编程

> 共 26 题 · 所属领域：AI测试赋能 · 专题：编程

---

## Q007001

- 题型：单选
- 难度：入门

**题目**

```text
Junit的TestCase类提供（）和tearDown（）方法，分别完成对测试环境的建立和拆除。
```

**选项**

```text
A. setUp（）
B. set（）
C. setap（）
D. setDown（）
```

**答案**

```text
A
```

**正确选项**

```text
A. setUp（）
```

**解析**

```text
【核心考点】 JUnit框架 测试生命周期方法
【题目解析】
本题考查JUnit 3中TestCase类的生命周期方法。在JUnit 3中，setUp()方法在每个测试方法执行前调用，用于初始化测试环境；tearDown()方法在每个测试方法执行后调用，用于清理资源。
【选项解析】
✓ A. setUp() — 正确。JUnit 3的标准方法名，用于建立测试环境。
✗ B. set() — 错误。不是JUnit中的标准方法。
✗ C. setap() — 错误。拼写错误，正确拼写为setUp。
✗ D. setDown() — 错误。JUnit中对应清理的方法是tearDown()，而非setDown()。
【易错提示】
注意JUnit 3与JUnit 4/5的差异：JUnit 4使用@Before和@After注解，JUnit 5使用@BeforeEach和@AfterEach。面试中需根据题目语境判断版本。
```

---

## Q007004

- 题型：简答
- 难度：入门

**题目**

```text
TestNG中如何跳过一个测试方法？
```

**答案**

```text
可以使用@Test(enabled=false)跳过一个测试方法
```

**解析**

```text
【核心考点】 TestNG 测试方法跳过
【题目解析】
本题考察TestNG框架中跳过测试方法的基本操作。TestNG提供了多种方式控制测试执行，其中@Tes(enabled=false)是最直接的方法，用于临时禁用某个测试用例。
【参考答案要点】
在@Test注解中添加enabled=false属性即可跳过，例如：@Test(enabled=false)。此外，还可以通过依赖方法（dependsOnMethods）或组（groups）实现条件跳过。
【面试角度】
回答时可扩展跳过与忽略的区别：enabled=false完全跳过，而@Test(timeOut)或异常预期等属于条件执行，面试中常对比这些场景。
【易错提示】
注意enabled属性默认值为true，如果误写为false会导致测试被忽略，排查时需检查注解配置。
```

---

## Q006997

- 题型：简答
- 难度：简单

**题目**

```text
@BeforeMethod和@BeforeClass之间的区别是什么?
```

**答案**

```text
@BeforeMethod—在每个测试方法之后会运行带该注解的方法
@BeforeClass—带该注解的方法在当前类中的第一个测试方法运行之前运行。
```

**解析**

```text
【核心考点】 TestNG注解 测试生命周期
【参考答案要点】
1. @BeforeMethod：在每个测试方法（@Test）执行之前运行。适用于在每个测试前进行初始化操作，如重置变量、打开浏览器等。
2. @BeforeClass：在当前测试类中的第一个测试方法执行之前运行一次。适用于类级别的初始化，如建立数据库连接、加载配置文件等。
【面试角度】
回答时建议结合实际测试场景说明区别，例如“@BeforeMethod用于每个用例前清除缓存，@BeforeClass用于整个测试类前启动服务”，能体现对注解作用域的理解。
【延伸知识】
TestNG还有@BeforeSuite、@BeforeTest、@BeforeGroups等注解，分别对应不同作用域。理解这些注解的执行顺序有助于编写高效的测试框架。
```

---

## Q006998

- 题型：简答
- 难度：简单

**题目**

```text
Cucumber中参数化用的是什么符号？
```

**答案**

```text
在步骤中可以使用<>来定义参数，在尝试根据步骤定义匹配步骤之前，Cucumber将使用表中的值替换这些参数。
```

**解析**

```text
【核心考点】 Cucumber参数化 BDD
【题目解析】
本题考查Cucumber框架中参数化的实现方式。Cucumber支持通过占位符在步骤定义中传递参数，使测试用例更灵活。
【参考答案要点】
Cucumber中参数化使用尖括号（<>）作为符号。在Feature文件的步骤中，使用<参数名>定义占位符，然后在Scenario Outline中通过Examples表格提供具体值。例如：
Feature: 登录功能
Scenario Outline: 用户登录
Given 用户输入用户名 <username>
When 用户输入密码 <password>
Then 登录成功
Examples:
| username | password |
| admin | 123456 |
在步骤定义中，使用正则表达式或Cucumber表达式捕获参数，如@Given("用户输入用户名 {string}")。
【面试角度】
面试中可能进一步询问参数化类型，如int、float、string等，或对比DataTable和Scenario Outline的区别。建议展示对Cucumber表达式的理解。
【易错提示】
注意尖括号仅在Scenario Outline中有效，普通Scenario中直接使用具体值。另外，Cucumber 3.x后推荐使用Cucumber表达式替代正则表达式，但尖括号语法仍被支持。
```

---

## Q007003

- 题型：简答
- 难度：简单

**题目**

```text
TestNG中@test注解的priority参数的值是否可以为0或者负数？
```

**答案**

```text
可以为0但是不可以为负数
```

**解析**

```text
【核心考点】 TestNG 注解参数
【题目解析】
在TestNG中，@Test注解的priority参数用于指定测试方法的执行优先级，数值越小优先级越高。该参数允许为0或负数，但通常建议使用非负整数以保持可读性。priority的默认值为0，因此设置为0与默认值相同，负数则优先级更高。
【参考答案要点】
可以为0，也可以为负数。priority参数接受int类型，0是默认值，负数表示比默认优先级更高。
【易错提示】
注意区分priority与dependsOnMethods：priority仅控制执行顺序，不保证依赖关系；而dependsOnMethods用于强制依赖。面试中常混淆这两个概念。
```

---

## Q007006

- 题型：简答
- 难度：简单

**题目**

```text
TestNG怎么运行一组测试用例？
```

**答案**

```text
可以使用TestNG的groups属性，来执行一组测试用例
@Test(groups={"smoke-test"})
```

**解析**

```text
【核心考点】 TestNG 分组测试
【题目解析】
本题考查TestNG框架中分组测试（groups）的使用。TestNG允许通过groups属性将测试用例分组，并在运行时选择执行特定组，常用于冒烟测试、回归测试等场景。通过XML配置文件或命令行指定groups，可灵活控制测试执行范围。
【参考答案要点】
1. 定义分组：在@Test注解中使用groups属性，如@Test(groups={"smoke-test"})。
2. 运行分组：通过testng.xml配置文件，使用标签指定要运行的组，或在命令行中使用-Dgroups参数。
3. 示例：testng.xml中配置，则只执行标记为smoke-test的用例。
【易错提示】
注意分组名称区分大小写，且需确保在XML中正确引用。另外，一个测试方法可属于多个组。
【面试角度】
这是TestNG基础功能，回答时建议结合实际项目经验说明分组测试如何提高效率，如冒烟测试组、回归测试组等。
```

---

## Q007007

- 题型：简答
- 难度：简单

**题目**

```text
Testng中都有哪些注解？
```

**答案**

```text
BeforeSuit/AfterSuit；
BeforeTest/AfterTest；
BeforeClass/AfterClass；
BeforeMethod/AfterMethod；
```

**解析**

```text
【核心考点】 TestNG框架 测试注解
【参考答案要点】
TestNG中常用的注解包括：@BeforeSuite 和 @AfterSuite：在测试套件之前/之后执行。@BeforeTest 和 @AfterTest：在测试类之前/之后执行。@BeforeClass 和 @AfterClass：在测试类中所有方法之前/之后执行一次。@BeforeMethod 和 @AfterMethod：在每个测试方法之前/之后执行。@Test：标记为测试方法。@DataProvider：提供测试数据。@Parameters：传递参数。@Listeners：添加监听器。这些注解用于控制测试执行的生命周期，实现初始化、清理和数据驱动等功能。
【面试角度】
回答时，建议强调注解的执行顺序和实际应用场景，例如“@BeforeMethod常用于初始化浏览器驱动，@AfterMethod用于截图失败用例”。同时，可对比JUnit的注解差异，展示对测试框架的深入理解。
【延伸知识】
TestNG还支持分组（@Test(groups=...)）、依赖（dependsOnMethods）和并行执行，这些高级特性在面试中常被问及，可用于优化测试执行效率。
```

---

## Q007010

- 题型：简答
- 难度：简单

**题目**

```text
什么是Cucumber的功能文件（featurefile）？
```

**答案**

```text
编写Cucumber测试的文件成为功能文件（特性文件），功能文件的扩展名必须是”.feature”。
```

**解析**

```text
【核心考点】 Cucumber BDD 功能文件
【题目解析】
本题考查Cucumber框架中功能文件（Feature File）的基本概念。Cucumber是一种行为驱动开发（BDD）工具，功能文件是Cucumber测试的核心载体，用于以自然语言描述软件功能，并驱动自动化测试执行。
【参考答案要点】
1. 定义：功能文件是Cucumber测试的入口文件，通常以.feature为扩展名，用于描述一个或多个业务功能场景。
2. 内容结构：包含Feature（功能描述）、Scenario（场景）、Given/When/Then（步骤定义）等关键字，采用Gherkin语法编写，支持中英文。
3. 作用：作为开发、测试、产品三方沟通的桥梁，同时作为自动化测试脚本的输入，通过步骤定义映射到具体代码执行。
【面试角度】
回答时建议强调功能文件与步骤定义文件的对应关系，以及如何通过Gherkin语法实现可读性与自动化执行的统一。可补充说明Cucumber支持多种语言（Java、Python、Ruby等），但功能文件语法一致。
【易错提示】
注意功能文件扩展名必须为.feature，且通常放在项目根目录下的features/文件夹中。不要混淆功能文件与步骤定义文件（Step Definition），后者是代码实现，扩展名根据语言不同（如.java、.py）。
```

---

## Q007015

- 题型：简答
- 难度：简单

**题目**

```text
如何在TestNG中让测试用例执行失败？
```

**答案**

```text
1、让测试代码抛出异常
2、Assert类断言失败
```

**解析**

```text
【核心考点】 TestNG 测试框架 断言
【题目解析】
本题考察TestNG中如何让测试用例执行失败，属于测试框架的基础知识。TestNG提供多种机制来标记测试失败，包括断言和异常处理。
【参考答案要点】
1. 让测试代码抛出异常：在测试方法中，如果代码抛出未捕获的异常（如RuntimeException），TestNG会将该测试标记为失败。例如：throw new RuntimeException("测试失败");
2. Assert类断言失败：使用TestNG的Assert类进行断言，当条件不满足时，断言失败会抛出AssertionError，导致测试失败。例如：Assert.assertEquals(actual, expected); 如果actual不等于expected，测试失败。
【面试角度】
此题为基础题，面试中可能进一步询问如何自定义失败信息或使用软断言（如SoftAssert）来收集多个失败而不立即终止。了解这些能展示对框架的深入掌握。
【易错提示】
注意区分断言失败和异常导致失败：断言失败是预期行为，而异常可能是代码错误。TestNG对两者都视为失败，但处理方式略有不同。
```

---

## Q007016

- 题型：简答
- 难度：简单

**题目**

```text
如果不使用testng能否运行一个测试
```

**答案**

```text
我们可以使用其他的测试框架，比如Junit或者Cucumber
```

**解析**

```text
【核心考点】 测试框架 TestNG替代方案
【题目解析】
本题考查测试框架的灵活性和替代方案。TestNG是Java中常用的测试框架，但并非唯一选择。面试官通过此题考察候选人对测试工具生态的了解。
【参考答案要点】
1. 替代框架：可以使用JUnit（JUnit 4/5）、Cucumber（BDD框架）等运行测试。
2. 注意事项：不同框架的注解、运行方式、报告生成等有差异，迁移时需要调整代码。例如，JUnit使用@Test，TestNG使用@Test并支持依赖测试。
3. 实际应用：在项目中，如果团队已熟悉JUnit，可优先使用；若需要数据驱动测试或并行执行，TestNG更合适。
【延伸知识】
除了JUnit和Cucumber，还有Spock（Groovy）、TestContainers（集成测试）等框架，了解多种工具能提升测试架构设计能力。
```

---

## Q007018

- 题型：简答
- 难度：简单

**题目**

```text
是否可以通过testng.xml文件传递测试数据
```

**答案**

```text
是的。我们可以通过testng.xml配置parameter传递参数和值。如：
在testng.xml文件中编写参数如下 ：
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="测试套件" >
<parameter name="browserName" value="chrome"/>
<test name="测试">
<classes>
<class name="com.test.testcases.LoginTest"/>
</classes>
</test>
</suite>

在测试方法中使用参数：
@Parameters({ "browserName" }) @Test public void browserTest(String browserName) { if(browserName.equals("Chrome")){ driver = new ChromeDriver(); }else if(browserName.equals("Firefox")){ driver = new FirefoxDriver(); } }
```

**解析**

```text
【核心考点】 TestNG 参数化测试
【参考答案要点】
是的，可以通过testng.xml文件传递测试数据。
1. 使用标签：在testng.xml中定义参数名称和值，例如：<parameter name="browserName" value="chrome" />。
2. 在测试类中接收：通过@Parameters注解将参数注入到测试方法参数中，例如：@Parameters("browserName")。
3. 作用范围：参数可在<suite>、<test>或<class>级别定义，支持不同粒度。
4. 局限性：只能传递简单类型（字符串、整数等），复杂对象需使用@DataProvider。
【面试角度】
面试中常会追问与@DataProvider的区别。testng.xml适合配置环境参数（如浏览器、URL），而@DataProvider适合传递多组测试数据。两者可结合使用。
【易错提示】
注意@Parameters注解只能用于方法参数，不能用于类字段。另外，参数名需与xml中完全匹配，否则会报错。
```

---

## Q007019

- 题型：简答
- 难度：简单

**题目**

```text
测试工程师无需进行代码审查和开发文档评审工作。这句话对吗？
```

**答案**

```text
不完全正确。虽然测试工程师的主要职责是执行测试，但是进行代码审查和开发文档评审工作可以帮助测试工程师更好地了解被测试系统的细节和功能，从而更好地设计和执行测试用例，提高测试效率和质量。此外，测试工程师在代码审查和文档评审过程中也可以提出一些问题和建议，帮助开发人员和其他相关人员更好地改进和完善系统。
```

**解析**

```text
【核心考点】 测试工程师职责 代码审查
【题目解析】
本题考查对测试工程师角色定位的理解。传统观点认为测试只负责执行，但现代测试强调质量内建，测试工程师应参与早期活动。
【参考答案要点】
这句话不完全正确。测试工程师参与代码审查和开发文档评审有以下好处：
1. 深入理解系统：通过审查代码和文档，测试人员能更全面了解系统架构和实现细节，从而设计更精准的测试用例。
2. 提前发现缺陷：在早期阶段发现逻辑错误或需求歧义，降低修复成本。
3. 促进团队协作：测试人员提出的问题有助于开发改进代码质量，形成质量共担文化。
【面试角度】
回答时强调质量内建理念，并举例说明参与代码审查如何帮助发现隐藏问题，能体现测试工程师的主动性。
【易错提示】
不要认为测试工程师必须审查所有代码，而是根据项目需要选择性参与，重点在于理解业务逻辑和接口。
```

---

## Q007021

- 题型：简答
- 难度：简单

**题目**

```text
编写程序，生成一个文件，文件名为“学生姓名.txt”,并将a的内容写入文件中。a=['学号：1907381106','姓名：陈佳']。用Python语言实现
```

**答案**

```text
a = ['学号：1907381106','姓名：陈佳']

file_name = a[1][3:] + ".txt"

with open(file_name, "w") as f:
for line in a:
f.write(line + '\n')
```

**解析**

```text
【核心考点】 文件操作 字符串处理 Python基础语法
【参考答案要点】
1. 提取文件名：从列表a中获取姓名部分，使用切片a[1][3:]提取“陈佳”，拼接为“陈佳.txt”。
2. 打开文件：使用with open(file_name, "w") as f:以写入模式打开文件，确保自动关闭。
3. 写入内容：遍历列表a，每行写入一个元素，并添加换行符'\n'。
【面试角度】
此题为基础编程题，考察文件读写和字符串操作。面试中常作为手写代码题，需注意文件路径、编码（如UTF-8）和异常处理（如文件不存在）。
【易错提示】
常见错误：忘记添加换行符导致内容连成一行；未使用with语句导致文件未关闭；切片索引错误（如a[1][3:]误写为a[1][2:]）。
```

---

## Q006999

- 题型：简答
- 难度：中等

**题目**

```text
Cucumber中的Background关键字有什么作用？
```

**答案**

```text
Background关键字允许为该功能中的场景添加一些上下文，它可以包含一个或者多个给定步骤，它在每个场景之前运行，但在任何before钩子之后，在功能文件中，将Background放在第一个场景之前，每个功能只能有一组背景步骤，如果你需要不同的场景使用不同的Background步骤，你需要将他们分成不同的功能文件。
```

**解析**

```text
【核心考点】 Cucumber BDD Background关键字
【题目解析】
本题考查Cucumber中Background关键字的用途，属于中等难度。Background用于定义每个场景之前执行的公共步骤，避免重复，提高可维护性。
【参考答案要点】
1. 作用：Background关键字用于为功能文件中的每个场景设置公共上下文，例如初始化数据、登录系统等。
2. 执行顺序：在每个场景之前运行，但在任何Before钩子之后。
3. 使用限制：每个功能文件只能有一个Background块；如果不同场景需要不同上下文，应拆分为多个功能文件。
4. 示例：
Feature: 用户登录
Background:
Given 用户已注册
And 用户已登录
Scenario: 修改密码
When 用户点击修改密码
Then 显示修改密码页面
【面试角度】
回答时建议结合实际项目经验，例如：“在测试电商订单流程时，我将登录和购物车初始化放在Background中，每个场景只关注订单操作，大大减少了重复代码。” 这能体现对BDD实践的理解。
【易错提示】
常见错误：误以为Background可以用于多个功能文件，或混淆Background与Before钩子的执行顺序。面试中应准确说明其作用域和限制。
```

---

## Q007000

- 题型：简答
- 难度：中等

**题目**

```text
Cucumber步骤定义文件的目的是什么？
```

**答案**

```text
Cucumber中的步骤定义是一个Java方法，其表达式将其链接到一个或者多个Cucumber步骤，当Cucumber在某个场景中执行一个Gherkin步骤时，它将寻找匹配的步骤定义并执行它。 比如下面的Cucumber场景：
Scenario: Login

Given user logins to the site
用户登录到步骤的站点部分(Given关键字后面的文本)将匹配以下步骤定义:
public class StepDefinitions{ 　　　　@Given("user logins to the site") 　　　　public void user_login_to_site(){ 　　　　　　　　System.out.println("Userisloggedintothesite"); 　　　　} }
```

**解析**

```text
【核心考点】 Cucumber BDD 步骤定义
【参考答案要点】
1. 连接Gherkin步骤与Java代码：步骤定义是一个Java方法，通过注解（如@Given、@When、@Then）与Gherkin场景中的步骤文本匹配，当Cucumber执行场景时，自动调用对应方法。
2. 实现测试逻辑：步骤定义中编写具体的测试操作和断言，例如模拟用户登录、验证页面元素等。
3. 提高可读性和可维护性：将业务需求（Gherkin）与技术实现（Java代码）分离，便于非技术人员理解测试场景。
【面试角度】
回答时需强调步骤定义是BDD（行为驱动开发）的核心，它实现了需求与测试的桥梁。建议举例说明，如“在登录场景中，@Given("user logins to the site")会触发一个方法，执行输入用户名和密码的操作”。
【易错提示】
不要混淆步骤定义与测试用例本身，步骤定义是方法，而测试用例由多个Gherkin步骤组成。另外，注意正则表达式匹配的准确性，避免步骤定义无法被正确调用。
```

---

## Q007002

- 题型：简答
- 难度：中等

**题目**

```text
Python自动测试中，常遇到过哪些问题?如何解决的？
```

**答案**

```text
在Python自动化测试中，常遇到以下一些问题：
1：页面元素定位失败：由于页面元素的定位方式多种多样，有些元素可能存在动态加载、位置发生变化等情况，导致在定位时失败。解决方法包括使用等待方法、更改定位方式等。
2：代码逻辑错误：编写测试代码时，可能会出现逻辑错误，例如判断条件不正确、方法调用错误等。解决方法包括仔细检查代码、使用调试工具等。
3：脚本执行时间过长：由于自动化测试需要执行大量测试用例，脚本执行时间可能会过长，影响测试效率。解决方法包括使用多线程或协程、减少重复代码等。
4：测试数据管理问题：测试数据的管理和维护可能会出现问题，例如测试数据不准确、数据冲突等。解决方法包括使用测试数据生成工具、定期清理测试数据等。
5：集成测试问题：在进行集成测试时，可能会出现测试环境配置不正确、服务接口异常等问题。解决方法包括使用Mock数据、修改测试环境配置等。
总之，解决Python自动化测试中遇到的问题需要结合具体情况采取不同的方法。建议编写测试代码时，注重代码质量和可维护性，遵循良好的编码规范，尽量减少代码中的重复部分，以提高代码的可读性和可维护性。同时，建议采用合适的测试工具和框架，结合团队的实际需求进行调整和优化。

这个问题是主观题，你只要从上述几个情况中，选择1-2个问题进行说明即可，主要是展示你个人的问题定位能力以及问题解决能力。

•
```

**解析**

```text
【核心考点】 Python自动化测试 常见问题解决
【题目解析】
本题考察面试者对Python自动化测试实践中常见问题的理解和解决能力。自动化测试不仅涉及脚本编写，还包括环境、数据、执行效率等多方面挑战。回答时应结合具体场景，展示问题分析和解决思路。
【参考答案要点】
1. 页面元素定位失败：常见原因包括动态加载、iframe切换、元素属性变化。解决方法：使用显式等待（如WebDriverWait）、相对定位（如XPath轴）、重试机制。
2. 代码逻辑错误：如条件判断失误、方法调用错误。解决方法：单元测试覆盖关键逻辑、使用断点调试、日志输出辅助排查。
3. 脚本执行时间过长：大量用例串行执行导致。解决方法：并行执行（如pytest-xdist）、优化用例设计（减少冗余步骤）、合理使用测试数据。
4. 测试数据管理问题：数据不准确、冲突或依赖。解决方法：使用数据驱动框架（如DDT）、独立测试数据（如数据库回滚）、随机数据生成。
【面试角度】
建议结合实际项目经历举例，例如“在电商项目中，我们通过显式等待解决了动态加载元素的定位问题”，能体现经验深度。
【易错提示】
避免只罗列问题而不提具体解决方案，面试官更关注解决思路和实际应用。
```

---

## Q007005

- 题型：简答
- 难度：中等

**题目**

```text
TestNG可以支持并行执行测试用例吗？支持多少线程？可能会遇到什么问题？
```

**答案**

```text
我们可以在TestNG中的testng.xml配置文件中使用parallel属性并行地运行测试用例，可以支持使用无限的线程数，但这可能会导致内存问题，具体由电脑配置决定
```

**解析**

```text
【核心考点】 TestNG并行执行 测试配置
【参考答案要点】
1. 支持并行执行：TestNG允许在testng.xml中通过parallel属性（如methods、tests、classes）配置并行执行测试用例。
2. 线程数配置：通过thread-count属性设置线程数，理论上可以支持无限线程，但受限于系统资源和硬件配置。
3. 可能问题：线程过多会导致内存溢出、CPU过载、资源竞争（如数据库连接池耗尽），以及测试结果不稳定（如共享状态冲突）。
【面试角度】
回答时建议结合实际项目经验，例如“我们项目中使用parallel='methods'和thread-count=5，避免了资源竞争”，并提及线程安全的注意事项，如使用ThreadLocal管理共享数据。
【延伸知识】
TestNG还支持依赖测试和分组并行，可进一步优化执行效率。面试中可能追问如何调试并行问题，建议准备日志分析或线程转储的示例。
```

---

## Q007008

- 题型：简答
- 难度：中等

**题目**

```text
pytest fixture 和 mark.parametrize参数化执行的先后步骤
```

**答案**

```text
按传入顺序执行
```

**解析**

```text
【核心考点】 pytest框架 fixture 参数化
【题目解析】
本题考察pytest中fixture与mark.parametrize的执行顺序。这是pytest框架的核心机制，理解顺序有助于编写正确的测试用例。fixture用于提供测试前置条件，parametrize用于传递多组数据，两者结合时执行顺序有明确规则。
【参考答案要点】
在pytest中，当测试函数同时使用fixture和mark.parametrize时，执行顺序为：先执行fixture，再执行参数化。具体步骤：
1. pytest解析测试函数，识别fixture依赖和参数化标记。
2. 对于每组参数化数据，pytest会创建一个独立的测试实例。
3. 在每个测试实例中，先调用fixture函数（若fixture有scope，则按scope规则缓存），然后将参数化数据传入测试函数。
4. 因此，fixture在每个参数化组合中都会被执行一次（除非fixture的scope为session或module且已缓存）。
【面试角度】
面试官常通过此题考察对pytest执行机制的底层理解。可进一步说明：若fixture也依赖参数化数据，可使用fixture参数化（通过@pytest.fixture(params=...)）实现更灵活的组合。同时注意fixture的scope（function/class/module/session）对执行次数的影响。
【易错提示】
常见误区：认为参数化先于fixture执行，或混淆fixture的scope导致缓存误判。建议通过简单示例（如打印日志）验证顺序，加深理解。
```

---

## Q007009

- 题型：简答
- 难度：中等

**题目**

```text
为什么说TestNG比Junit更好更强大？
```

**答案**

```text
TestNG比Junit支持更多的注解
TestNG支持配置测试顺序，但JUnit不支持
TestNG支持注解方式的各种监听器，但JUnit不支持
TestNG的测试报告比Junit更好
```

**解析**

```text
【核心考点】 TestNG vs JUnit 测试框架对比
【参考答案要点】
1. 注解支持更丰富：TestNG 提供 @BeforeSuite、@AfterSuite、@BeforeGroup、@AfterGroup 等注解，而 JUnit 4 仅提供 @BeforeClass、@AfterClass 等，TestNG 在分组和依赖测试方面更灵活。
2. 测试顺序可配置：TestNG 支持通过 @Test(priority = N) 指定执行顺序，JUnit 4 默认不保证顺序，需额外使用 @FixMethodOrder。
3. 监听器机制更强大：TestNG 内置 IAnnotationTransformer、ITestListener 等接口，支持注解级别和运行时的监听器注入，JUnit 4 的 @Rule 和 @RunWith 相对有限。
4. 测试报告更完善：TestNG 默认生成 emailable-report.html 和 index.html 等报告，包含失败截图、耗时统计等，JUnit 4 需集成第三方报告工具。
【面试角度】
回答时建议结合实际项目迁移经验，例如“在将 JUnit 4 迁移到 TestNG 后，我们利用分组测试减少了 30% 的执行时间”，能体现实战能力。
【延伸知识】
JUnit 5 已大幅改进，支持 @Nested、@DisplayName 等，并引入 Jupiter 扩展模型，与 TestNG 差距缩小。面试中可对比两者最新版本，展示技术前瞻性。
```

---

## Q007011

- 题型：简答
- 难度：中等

**题目**

```text
什么是Cucumber的场景大纲？它的目的是什么？
```

**答案**

```text
使用场景大纲可以对多个数据集执行相同的场景，数据是由表格结构提供的。
```

**解析**

```text
【核心考点】 Cucumber BDD 场景大纲
【题目解析】
本题考查Cucumber中场景大纲（Scenario Outline）的概念与用途。场景大纲是Cucumber BDD框架中的核心功能，用于通过占位符和示例表格，对同一测试场景执行多组数据，实现数据驱动的测试设计。
【参考答案要点】
1. 定义：场景大纲是一种模板化的场景定义，使用尖括号（如<param>）作为参数占位符，结合Examples表格提供多组测试数据。
2. 目的：避免重复编写相似的场景，提高测试用例的可维护性和覆盖率。例如，测试登录功能时，可通过场景大纲覆盖多个用户名和密码组合。
3. 执行机制：Cucumber会为Examples表格中的每一行数据生成一个独立的测试用例，并依次执行。
【面试角度】
回答时建议结合实际项目案例说明场景大纲的应用，例如“在电商项目中，使用场景大纲测试不同商品类型的价格计算逻辑”，能体现对BDD和数据驱动测试的深入理解。
【易错提示】
注意区分场景大纲与普通场景：普通场景适用于单一数据组合，而场景大纲适用于多组数据的参数化测试。面试中常混淆两者。
```

---

## Q007013

- 题型：简答
- 难度：中等

**题目**

```text
如何使用TestNG运行特定类型的测试用例?
```

**答案**

```text
可以在TestNG中使用组(group)来运行特定类型的测试用例。
```

**解析**

```text
【核心考点】 TestNG 测试分组 测试执行
【题目解析】
本题考查TestNG框架中分组（Group）功能的使用。TestNG允许通过@Test(groups = {"groupName"})注解将测试用例分组，然后在testng.xml配置文件中指定要运行的组，实现选择性执行。
【参考答案要点】
1. 定义组：在测试方法上使用@Test(groups = {"smoke", "regression"})注解，将测试用例归类到不同组。
2. 配置testng.xml：在testng.xml文件中使用<groups>标签指定要运行的组，例如<run><include name="smoke"/></run>，则只运行属于smoke组的测试用例。
3. 命令行或IDE执行：通过Maven或Gradle插件，或直接在IDE中运行testng.xml文件。
【面试角度】
面试官通过此题考察候选人对测试框架高级功能的掌握程度。建议补充说明组依赖（@Test(dependsOnGroups = {"groupName"})）和组排除（<exclude name="broken"/>）等进阶用法，体现技术深度。
【延伸知识】
TestNG还支持元组（Meta Groups），可以在testng.xml中定义组包含其他组，实现更灵活的测试分类。了解此功能有助于应对复杂测试场景。
```

---

## Q007014

- 题型：简答
- 难度：中等

**题目**

```text
如何分析TestNG框架运行失败？
```

**答案**

```text
1、TestNG测试运行失败会在控制台输出对应异常信息（断言失败/代码执行报错信息），根据异常信息进行定位
2、通过IDEA提供的断点调试功能定位问题
```

**解析**

```text
【核心考点】 TestNG框架 故障排查
【参考答案要点】
1. 查看控制台异常信息：TestNG运行失败时，控制台会输出异常堆栈信息，包括断言失败原因或代码执行错误，根据异常类型和消息定位问题。
2. 使用IDE断点调试：在IDEA等开发工具中设置断点，逐步执行测试代码，观察变量值和执行流程，定位失败点。
【面试角度】
回答时建议结合实际调试经验，例如“在项目中，我常用IDEA的断点调试结合日志输出，快速定位TestNG测试失败的原因”，能体现实践能力。
【延伸知识】
除了控制台和断点，还可以使用TestNG的监听器（如ITestListener）捕获失败事件，或结合日志框架（如Log4j）记录详细执行信息，提高排查效率。
```

---

## Q007017

- 题型：简答
- 难度：中等

**题目**

```text
描述JUnit和TestNG单元测试框架之间的异同
```

**答案**

```text
相似之处：
1、提供了许多不同的注解
2、支持忽略测试
3、支持接受异常
4、支持并行运行
不同支持：
与Junit相比，TestNG的报告更好
Junit没有依赖测试，而TestNG的依赖测试非常强大
```

**解析**

```text
【核心考点】 单元测试框架 JUnit TestNG
【题目解析】
本题考察对主流Java单元测试框架的理解，需要对比JUnit和TestNG的异同。两者都支持注解、异常测试、忽略测试和并行执行，但TestNG在依赖测试和报告方面更强大。
【参考答案要点】
相似之处：
1. 提供多种注解（如@Test、@Before等）。
2. 支持忽略测试（@Ignore或@Test(enabled=false)）。
3. 支持异常测试（expected属性）。
4. 支持并行执行。
不同之处：
1. TestNG的报告生成能力更强，支持HTML和XML报告。
2. TestNG支持依赖测试，可指定测试方法的执行顺序，而JUnit默认不保证顺序。
3. TestNG支持分组测试，JUnit5通过@Tag实现类似功能。
【面试角度】
回答时建议结合实际项目使用经验，例如“在项目中我们使用TestNG进行依赖测试，确保登录用例先于购买用例执行”，能体现实践深度。
【延伸知识】
JUnit5引入了更多特性，如动态测试、参数化测试等，与TestNG的差距缩小。了解版本差异有助于应对追问。
```

---

## Q007020

- 题型：简答
- 难度：较难
- 答案：AI 补全（原数据缺失文字答案）

**题目**

```text
编写 Animal 类和 Dog 类； 根据用户输入的数值，创建相应个数的 Animal 对象和 Dog 对象（10分） C++
```

**答案**

```text
1. 定义Animal基类：包含基本属性如名称、年龄，以及虚函数如speak()。
2. 定义Dog派生类：继承Animal，重写speak()方法，添加特有属性和方法。
3. 动态创建对象：根据用户输入数值n，使用new操作符创建n个Animal对象和n个Dog对象，存储于指针数组或容器中。
4. 内存管理：使用delete释放动态分配的内存，避免内存泄漏。
```

**解析**

```text
【核心考点】 面向对象编程 继承 动态对象创建
【参考答案要点】
1. 定义Animal基类：包含基本属性如名称、年龄，以及虚函数如speak()。
2. 定义Dog派生类：继承Animal，重写speak()方法，添加特有属性和方法。
3. 动态创建对象：根据用户输入数值n，使用new操作符创建n个Animal对象和n个Dog对象，存储于指针数组或容器中。
4. 内存管理：使用delete释放动态分配的内存，避免内存泄漏。
【面试角度】
回答时需强调多态性和动态内存管理，例如使用基类指针数组指向派生类对象，并正确调用虚函数。同时注意析构函数声明为虚函数。
【延伸知识】
可提及C++11智能指针（如unique_ptr）替代裸指针，以及STL容器vector管理动态对象，体现现代C++编程实践。
```

---

## Q007012

- 题型：简答
- 难度：困难

**题目**

```text
如何为您手头使用的“购物车”功能（或“杯子”）设计一套测试用例？
```

**答案**

```text
1. 功能测试 (Functionality)

• 添加商品：未登录状态添加、登录后添加、添加同款商品（数量是否累加）、添加不同商品。

• 购物车数量限制：达到上限时的提示、超出库存时的操作。

• 删除商品：单删、全选删除、批量删除。

• 商品状态：商品失效或下架后的购物车展示及结算处理。

2. 界面与交互测试 (UI/UX)

• 布局：页面排版是否整齐，图片和文字是否对齐。

• 响应：不同分辨率（手机、平板、PC端）下的展示适配。

• 交互：全选/反选按钮的联动是否正常，增减商品数量的加减号是否可用。

3. 性能测试 (Performance)

• 加载速度：在网络缓慢或高并发（如大促）时，加入购物车接口的响应时间（应在合理范围内，如 <2 秒）。

• 稳定性：长时间挂起购物车页面是否会出现内存泄漏。

4. 安全测试 (Security)

• 参数篡改：在前端拦截请求，尝试修改商品单价或总价（如改为 $0.01），验证后端是否有金额校验。

• 并发安全：多端同时操作购物车或极端网络下的并发扣减是否会出现数据异常。

5. 兼容性测试 (Compatibility)

• 平台兼容：在 iOS、Android、Windows、macOS 上的表现。

• 浏览器兼容：在 Chrome、Safari、Edge 等不同内核浏览器上的显示与功能。
```

**解析**

```text
def bubble_sort(arr):
n = len(arr)
for i in range(n):
# 提前退出标志，如果本轮没有发生交换，说明列表已经有序
swapped = False

# 内层循环负责相邻元素的两两比较和交换
for j in range(0, n - i - 1):
if arr[j] > arr[j + 1]:
# 交换相邻两个元素
arr[j], arr[j + 1] = arr[j + 1], arr[j]
swapped = True

# 如果没有数据交换，说明已经排好序，结束循环
if not swapped:
break

return arr

# 测试代码
numbers = [64, 34, 25, 12, 22, 11, 90]
print("排序前：", numbers)
bubble_sort(numbers)
print("排序后：", numbers)
```

---

## Q007022

- 题型：简答
- 难度：未标注
- 解析：AI 补全（原数据缺失解析）

**题目**

```text
请编写一个Cucumber框架的feature文件示例
```

**答案**

```text
Feature:Logintosite
Scenario:Userlogin with valid credentials
Given user is on loginpage
When user enters valid username
And user enters valid password
Then login success message isdisplayed
```

**解析**

```text
【核心考点】行为驱动开发中 feature 文件的写法。
【题目解析】feature 文件用自然语言描述业务行为，先写 Feature 说明功能，再用 Scenario 描述场景，步骤按 Given、When、Then 组织：Given 准备前置条件，When 执行操作，And 补充步骤，Then 校验结果。
【答题要点】
1. Feature 概括功能，Scenario 描述单个场景。
2. Given 准备数据，When 触发动作，Then 断言结果。
3. 步骤应业务化，避免写具体实现细节。
【面试提示】可说明 feature 与步骤定义分离，便于共同维护。
```

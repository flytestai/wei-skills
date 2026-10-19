# HTTP协议与接口测试题

> 独立模块：HTTP协议与接口测试题（中小厂测开必考，接口测试岗核心）
> 来源：中小厂面经真题、postman/requests 实战、HTTP 八股。

## 一、HTTP 协议基础（必考）

### 1. HTTP 和 HTTPS 的区别
- tags: HTTP, 安全, 必考
- difficulty: easy
- frequency: 高频
- prompt: HTTP 和 HTTPS 有什么区别？
- answer: HTTP 明文传输 80 端口；HTTPS = HTTP + TLS 加密，443 端口，需要 CA 证书。抓包工具抓 HTTPS 要装根证书。一句总结：HTTPS 防的是传输链路上被窃听和篡改。

### 2. GET 和 POST 的区别
- tags: HTTP, 必考
- difficulty: easy
- frequency: 高频
- prompt: GET 和 POST 的区别？
- answer: ①参数位置：GET 在 URL 问号后、POST 在 body；②语义：GET 获取幂等、POST 提交会产生新数据；③缓存：GET 能被浏览器缓存，POST 不缓存；④长度：GET 受 URL 长度限制（浏览器实现约定，不是协议规定）。加分点：POST body 三种格式（form/json/multipart）要看 Content-Type。

### 3. 常见的 HTTP 状态码
- tags: HTTP, 必考
- difficulty: easy
- frequency: 高频
- prompt: 说出常见 HTTP 状态码及含义。
- answer: 200 成功；301 永久重定向；302 临时重定向；304 协商缓存命中；400 参数错误；401 未认证（没登录/token 失效）；403 无权限；404 不存在；405 方法不允许；500 服务器内部错误；502 网关错误（后端挂了）；504 网关超时（后端响应慢）。测开重点：401 和 403 的区分，502 和 504 的区分。

### 4. Cookie 和 Session 和 Token 的区别
- tags: 会话, 必考
- difficulty: medium
- frequency: 高频
- prompt: Cookie、Session、Token（JWT）的区别？接口自动化怎么处理登录态？
- answer: Cookie 存客户端，随请求自动带；Session 存服务端，客户端只存 session_id；Token 自包含（JWT 把用户信息签名后编码在 token 里），服务端无需存会话、天然支持分布式。接口自动化实践：登录接口拿 token，塞进后续请求的 Authorization header（Bearer token），用 fixture 全局复用。

### 5. 什么是幂等性，哪些接口是幂等的
- tags: 接口设计, 高频
- difficulty: medium
- frequency: 高频
- prompt: 什么是幂等性？为什么测开要关注？
- answer: 幂等 = 同一请求执行一次和 N 次效果相同。GET/PUT/DELETE 幂等；POST 不幂等。测试点：重复提交订单、重复点击支付按钮，服务端要做幂等控制（唯一索引/token 机制/分布式锁）。自动化里用重复调同一接口 N 次验证幂等是高频考题。

### 6. PUT 和 POST 的区别
- tags: HTTP, 中高频
- difficulty: medium
- frequency: 中高频
- prompt: PUT 和 POST 都是向服务端提交数据，区别在哪？
- answer: 语义不同：PUT 幂等，用于整体更新（客户端指定资源 URL）；POST 不幂等，用于创建资源（URL 由服务端分配）。RESTful 风格里 POST /users 创建、PUT /users/1 全量更新、PATCH /users/1 部分更新。

## 二、接口测试实战（测开核心）

### 7. 接口测试用例设计维度
- tags: 用例设计, 必考
- difficulty: medium
- frequency: 高频
- prompt: 给你一个接口，你怎么设计测试用例？
- answer: 六层：①正常：正确入参+业务流程；②参数校验：必填缺失、类型错、长度边界、枚举非法值；③异常：鉴权（无 token/过期/伪造）、权限不足、依赖服务异常；④数据：幂等重复提交、并发；⑤落库：接口返回成功后查库验证数据正确；⑥兼容：header/Content-Type 变体。口诀：正常、异常、边界、鉴权、落库、幂等。

### 8. 接口自动化断言怎么做
- tags: 断言, 必考
- difficulty: easy
- frequency: 高频
- prompt: 接口自动化的断言，你会断哪些内容？
- answer: 三层断言：①HTTP 层：状态码、响应时间（性能红线）；②业务层：code、message、success 字段；③数据层：关键字段值比对+数据库落库校验。反面教材：只断 200 状态码——业务 code=1 失败也返回 200，漏测。

### 9. 接口之间有数据依赖怎么处理
- tags: 接口关联, 必考
- difficulty: medium
- frequency: 高频
- prompt: 下单接口依赖登录的 token 和创建地址的 id，自动化怎么处理？
- answer: 上下文传递：登录后把 token 存全局 dict 或 fixture，下单用例从上下文取；跨用例字段用变量提取器（正则/jsonpath 从响应提取 order_id 存变量，后续用 ${order_id} 引用）。讲清两种粒度：fixture 传 token（会话级）+ 变量提取器传业务数据（用例级）。

### 10. token 过期怎么处理
- tags: 接口自动化, 工程实战
- difficulty: medium
- frequency: 中高频
- prompt: 长时间跑自动化 token 过期了怎么办？
- answer: 封装层拦截：收到 401 自动重新登录刷新 token 并重发请求（requests 的 auth 钩子或封装 retry）；或 fixture 里判断过期时间提前刷新。加分：讲 token 的 refresh 机制（双 token：access 短期 + refresh 长期）。

### 11. 怎么测试一个文件上传接口
- tags: 接口测试, 实战
- difficulty: medium
- frequency: 中高频
- prompt: 文件上传接口怎么测？
- answer: requests 用 files 参数传 multipart：files={'file': open('x.png','rb')}。用例维度：正常格式、超大文件（限制边界）、错误格式后缀、空文件、恶意文件名（../ 路径穿越）、并发上传。加分：提 Content-Type 是 multipart/form-data 且 boundary 自动生成。

### 12. mock 是什么，什么时候用
- tags: Mock, 必考
- difficulty: medium
- frequency: 高频
- prompt: 什么是 Mock？测试里什么场景用？
- answer: Mock = 用假实现替换真实依赖。场景：①下游服务未开发完（契约先行）；②第三方支付/短信这种外部依赖（不稳定且花钱）；③异常注入（模拟下游超时/500，验证己方容错）。Python 实现：unittest.mock.patch、pytest monkeypatch、独立 Mock 平台（WireMock）。

### 13. 怎么定位是前端 bug 还是后端 bug
- tags: 排查, 必考
- difficulty: medium
- frequency: 高频
- prompt: 页面显示错了，怎么判断是前端还是后端的问题？
- answer: 抓包看接口：F12 Network 或 Charles 看响应。响应数据本身错 → 后端 bug；响应数据对但页面渲染错 → 前端 bug；请求参数就发错了 → 前端 bug。这是中小厂测开最爱的问题，考的是你的排查链路而不是背概念。

### 14. 接口测试要做安全方面的验证吗
- tags: 安全测试, 中高频
- difficulty: medium
- frequency: 中高频
- prompt: 接口测试会涉及安全测试吗？测什么？
- answer: 会，基础安全项：SQL 注入（参数带 ' or 1=1）、XSS（参数带 <script>）、越权（普通用户 token 调管理员接口——水平越权/垂直越权）、敏感信息泄露（返回体含密码明文）、未授权访问（去掉 token 直接调）。中小厂不要求渗透级，但这几个必须能说。

### 15. postman 和 python 脚本做接口测试的区别
- tags: 工具选型, 中高频
- difficulty: easy
- frequency: 中高频
- prompt: Postman 也能做接口测试，为什么要写 Python 自动化？
- answer: Postman 适合单接口调试和轻量集合测试，上手快但：复杂业务逻辑难表达（断言和数据处理能力弱）、不易版本管理、难和 CI/SQL 校验/日志体系集成。Python+pytest+requests 的自动化能做：复杂断言、数据驱动、数据库校验、Jenkins 集成、报告体系。答的时候给结论：调试用 Postman，工程化回归用框架。

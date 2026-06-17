# 测试工程化与CI/CD

### 1. Git 中 merge 和 rebase 有什么区别
- tags: Git, 持续集成
- difficulty: medium
- prompt: 在团队协作中，Git 的 merge 和 rebase 有什么区别？分别适合什么场景？
- answer: merge 会保留分支合并历史，适合团队协作保留完整提交脉络；rebase 会把当前分支的提交“挪到”目标分支最新提交之后，让历史更线性，但如果对已共享分支随意 rebase，容易给协作者带来冲突和历史重写问题。

### 2. Jenkins Pipeline 和 Freestyle Job 有什么区别
- tags: Jenkins, 持续集成
- difficulty: medium
- prompt: Jenkins 中 Pipeline 和传统 Freestyle Job 有什么区别？为什么现在很多团队更偏向 Pipeline？
- answer: Freestyle 更像页面化配置，简单直接但可复用性和可版本化较弱；Pipeline 用代码描述流程，便于版本管理、复用、审计和复杂流程编排，所以更适合现代持续集成体系。

### 3. Docker 镜像和容器有什么区别
- tags: Docker, 环境管理
- difficulty: easy
- prompt: Docker 中镜像和容器分别是什么？它们的关系是什么？
- answer: 镜像是静态模板，包含应用运行所需环境；容器是镜像启动后的运行实例。可以理解为镜像是类比安装包或模板，容器是实际跑起来的进程实例。

### 4. Linux 中如何排查一个服务进程异常
- tags: Linux, 日志排查
- difficulty: medium
- prompt: 如果测试平台上的一个服务异常了，你一般会怎么在 Linux 上排查？
- answer: 一般先确认进程状态，再看端口占用、日志输出、资源使用和最近变更。常见会用 ps、top、grep、tail、netstat/ss、journalctl 等命令，从“进程、端口、日志、资源、依赖”几个维度排查。

### 5. SQL 里 left join 和 inner join 的区别
- tags: SQL, 数据校验
- difficulty: easy
- prompt: SQL 中 left join 和 inner join 的区别是什么？测试开发为什么要理解这个问题？
- answer: inner join 只保留两边能匹配上的记录；left join 会保留左表全部记录，即使右表匹配不到也会保留。测试开发经常需要做数据核对、结果校验和问题定位，所以 join 语义理解不准会直接影响排查结论。

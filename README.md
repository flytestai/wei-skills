# Wei Skills

OpenClaw / Hermes 技能集合，聚焦 **刷题、课程教学、业务分析、消息监控** 四类可复用技能。

## 技能列表

### 1. python-testdev-drill
Python 测试开发工程师面试刷题系统。

**能力特性**
- 支持多模块隔离：
  - Python基础手写代码题
  - Python编程基础理论面试题
  - 自动化测试题
  - 测试开发面试题
- 支持一次刷多题
- 支持按模块刷题 / 随机刷题
- 支持错题集刷题 / 收藏题库刷题 / 自建题库刷题
- 刷题历史自动沉淀，模块内优先去重
- 每题可带参考答案
- 支持收藏题目、保存自建题目、持久化进度

**典型用法**
- `刷 3 道 Python基础手写代码题`
- `刷 5 道 自动化测试题`
- `随机刷 4 道题`
- `刷错题集`
- `刷收藏题`
- `保存这道题到 测试开发面试题`

---

### 2. chat-course-coach
聊天式课程教学系统。

**能力特性**
- 自然语言描述学习目标，自动生成课程目录
- 微信聊天风格逐课教学
- 细粒度进度跟踪（模块 → 课 → 段）
- 掌握度分层、复盘机制、回顾机制
- 项目主线贯穿
- 支持系统模式 / 面试模式 / 实战模式
- 支持跨会话续学

**典型用法**
- `我想系统学 FastAPI`
- `继续学习 FastAPI`
- `查看当前学习进度`

---

### 3. caipiao-analyzer
大乐透分析 skill（逻辑封装型 wrapper）。

**能力特性**
- 依赖原 `flytestai/caipiao` FastAPI 后端
- 完整映射：
  - 历史查询
  - 数据分析
  - 梅花推算
  - AI 预测
  - 回测
  - 方案管理
- 不重新实现逻辑，原仓库代码作为唯一逻辑源
- 包含后端启动流程、健康检查、参数映射、错误处理规则

**典型用法**
- `最近开奖历史`
- `帮我推算号码`
- `回测最近100期`

---

### 4. feishu-vip-monitor
飞书群 VIP 关键词监控转发。轮询指定飞书群，识别带关键词的消息，连同配图转发到微信，并用消息水位杜绝重复消费。

**能力特性**
- 用 `message_position` 水位消费消息，重启、崩溃都不会重复推送
- 三档抖动轮询，避开飞书风控：交易期 27~47s / 白天 95~155s / 夜间 9~12min
- 多页回溯**按水位早停**——飞书 `has_more` 恒为 `true`，不能当停止条件
- 周期补偿 `sleep(max(5, target - elapsed))`，拉取耗时不会累积成轮询漂移
- cron 每分钟巡检，心跳分时段阈值（180s / 600s / 1200s），超时强杀重启
- token 保活常驻：`refresh_token` 只能用一次，必须提前轮换
- 推送重试、告警冷却持久化、日志轮转、配图缓存回收
- 文本气泡排版：标题 + 图标 + 浅色短虚线 + 正文，手机/电脑版微信均正确换行

**主要踩坑（已在实现中修复）**
- `HERMES_HOME` 未注入 → lark-cli 返回 `not_configured`，进程在跑但一条收不到
- `pgrep -f '[w]u2198'` 方括号被当字面字符类，既防不了自匹配也匹配不到进程
- `flock -n || exit 0` 导致：持锁者正是本脚本拉起的进程时误判为"已在运行"
- `RotatingFileHandler` + `StreamHandler` + `nohup` 同文件，每条日志写两遍

**典型用法**
- `监控这个飞书群，有真爱粉可见的消息就转发给我`
- `看看监控进程是不是假死了`
- `飞书 token 快过期了，帮我保活`

---

## 安装方式

```bash
git clone https://github.com/flytestai/wei-skills.git
cp -r wei-skills/python-testdev-drill ~/.openclaw-autoclaw/skills/
cp -r wei-skills/chat-course-coach ~/.openclaw-autoclaw/skills/
cp -r wei-skills/caipiao-analyzer ~/.openclaw-autoclaw/skills/
cp -r wei-skills/feishu-vip-monitor ~/hermes/shared/skills/
```

> `feishu-vip-monitor` 是 Hermes skill，装到 Hermes 的 skills 目录；其余三个装到 OpenClaw。

## 使用说明

安装后直接在对话中调用对应能力，无需额外命令前缀。

### 刷题
- `继续 Python基础手写代码题`
- `刷 3 道 Python基础手写代码题`
- `刷 5 道 自动化测试题`
- `刷错题集`
- `刷收藏题`

### 学习课程
- `我想系统学 FastAPI`
- `继续学习 FastAPI`
- `查看学习进度`

### 大乐透分析
> 使用前需先启动 `caipiao` 后端

- `最近开奖历史`
- `帮我推算号码`
- `回测最近100期`

### 飞书群监控
> 依赖已授权的 `lark-cli`，且必须注入 `HERMES_HOME`

- `监控这个飞书群，有 VIP 消息就转发给我`
- `监控进程还在跑吗`

## 仓库定位

这个仓库主要维护可复用的 OpenClaw / Hermes skills，强调：
- 可持久化
- 可续用
- 面向真实工作流
- 兼顾说明文档与可直接使用的技能结构

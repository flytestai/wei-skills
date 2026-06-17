# Wei Skills

OpenClaw / Hermes 技能集合，聚焦 **刷题、课程教学、业务分析** 三类可复用技能。

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

## 安装方式

```bash
git clone https://github.com/flytestai/wei-skills.git
cp -r wei-skills/python-testdev-drill ~/.openclaw-autoclaw/skills/
cp -r wei-skills/chat-course-coach ~/.openclaw-autoclaw/skills/
cp -r wei-skills/caipiao-analyzer ~/.openclaw-autoclaw/skills/
```

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

## 仓库定位

这个仓库主要维护可复用的 OpenClaw / Hermes skills，强调：
- 可持久化
- 可续用
- 面向真实工作流
- 兼顾说明文档与可直接使用的技能结构

# Wei Skills

OpenClaw / Hermes 技能集合。

## 已包含技能

### python-testdev-drill
Python 测试开发工程师面试刷题系统。
- 支持多模块隔离（基础手写代码、理论面试、自动化测试、测试开发）
- 一题一题推进，自动评分
- 错题集自动记录
- 模块内题目不重复
- 进度持久化，随时续练

### chat-course-coach
聊天式课程教学系统。
- 自然语言描述学习目标，自动生成课程目录
- 微信聊天风格逐课教学
- 细粒度进度跟踪（模块 → 课 → 段）
- 掌握度分层、复盘机制
- 项目主线贯穿
- 多模式教学（系统模式 / 面试模式 / 实战模式）

## 安装方式

```bash
# 克隆仓库
git clone https://github.com/flytestai/wei-skills.git

# 复制技能到 OpenClaw / Hermes 的 skills 目录
cp -r wei-skills/python-testdev-drill ~/.openclaw-autoclaw/skills/
cp -r wei-skills/chat-course-coach ~/.openclaw-autoclaw/skills/

# 或 Windows
xcopy wei-skills\python-testdev-drill %USERPROFILE%\.openclaw-autoclaw\skills\python-testdev-drill\ /E /I
xcopy wei-skills\chat-course-coach %USERPROFILE%\.openclaw-autoclaw\skills\chat-course-coach\ /E /I
```

## 使用方式

安装后直接在对话中使用：

刷题：
- `继续 Python基础手写代码题`
- `开始 自动化测试题`

课程：
- `我想系统学 FastAPI`
- `继续学 FastAPI`
- `查看 FastAPI 当前进度`

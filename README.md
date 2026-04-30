# CodeScan — AI Code Review Agent

<div align="center">

![CodeScan Banner](https://img.shields.io/badge/CodeScan-AI%20Code%20Review-7c6aff?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyek0xMSAxN3YtNkg5bDMtNCAzIDRoLTJ2NmgtMnoiLz48L3N2Zz4=)
[![](https://img.shields.io/badge/LICENSE-MIT-green)](./LICENSE)
![DeepSeek](https://img.shields.io/badge/Powered%20by-DeepSeek%20API-blue?style=for-the-badge)

**多维度 AI 代码审查 Agent，支持所有主流编程语言**

🚀 [在线体验 Demo](https://clydennke.github.io/codescan/)

</div>

---

## ✨ 项目简介

CodeScan 是一个运行在浏览器中的 AI 代码审查工具，基于 **DeepSeek API** 构建。它采用两阶段 Agent 架构，自动识别代码语言，从**安全性**、**性能**、**可读性**三个维度进行深度分析，输出结构化评分报告，并支持多轮追问。

整个工具为**纯静态网页**，无需服务器，部署在 GitHub Pages 上即可使用。

---

## 🎯 核心功能

| 功能 | 说明 |
|---|---|
| 🔍 **语言自动识别** | 自动检测 Python、Java、Kotlin、JS/TS、Go、C/C++、PHP、Rust 等 |
| 🔒 **安全性分析** | SQL 注入、XSS、不安全加密算法、未校验输入等漏洞检测 |
| ⚡ **性能分析** | N+1 查询、无效循环、内存泄漏、缺少超时等性能问题 |
| 📖 **可读性分析** | 命名规范、注释质量、函数复杂度、代码结构评估 |
| 💡 **优化建议** | 具体可操作的改进方案，不只是指出问题 |
| 💬 **多轮追问** | 报告生成后可继续与 Agent 对话，例如要求重写某段代码 |

---

## 🤖 Agent 工作流

```
用户粘入代码
     │
     ▼
┌─────────────────┐
│  Step 1: 语言识别 │  → 识别语言、代码类型、复杂度
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Step 2: 多维分析 │  → 安全 / 性能 / 可读性三维同步分析
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  生成结构化报告   │  → 评分 + 问题列表 + 优化建议
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  追问模式        │  → 携带代码上下文的多轮对话
└─────────────────┘
```

---

## 🚀 在线使用

**直接打开 Demo 链接，填入你自己的 DeepSeek API Key 即可使用。**

> API Key 仅在浏览器本地使用，不会发送到任何第三方服务器，完全私密。

获取 DeepSeek API Key：[platform.deepseek.com](https://platform.deepseek.com)（新注册有免费额度，每次分析费用约 ¥0.01）

---

## 🛠️ 本地运行

本项目为纯静态网页，无任何依赖。

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/codescan.git
cd codescan

# 直接用浏览器打开
open index.html       # macOS
start index.html      # Windows
xdg-open index.html   # Linux
```

---

## 📦 部署到 GitHub Pages

```bash
git clone https://github.com/YOUR_USERNAME/codescan.git
cd codescan
# 把 index.html 放入仓库根目录
git add .
git commit -m "init: CodeScan AI Code Review Agent"
git push
```

然后在 GitHub 仓库 → **Settings** → **Pages** → Branch: `main` → **Save**，等约 1 分钟即可访问。

---

## 🖥️ 技术栈

- **纯 HTML / CSS / JavaScript**，零框架依赖，零构建步骤
- **DeepSeek Chat API**（`deepseek-chat` 模型）
- 两阶段 Prompt 链：结构化 JSON 输出 + 对话上下文管理
- 完全运行于客户端浏览器，隐私安全

---

## 📊 评分说明

| 等级 | 分数 | 含义 |
|---|---|---|
| S | 90-100 | 优秀，无明显问题 |
| A | 80-89 | 良好，有少量可优化点 |
| B | 70-79 | 中等，有若干需注意的问题 |
| C | 60-69 | 较差，存在明显问题 |
| D | 0-59 | 需要大幅重构 |

---

## 💬 追问示例

报告生成后，你可以这样追问 Agent：

- `帮我修复所有安全漏洞，给出修改后的完整代码`
- `把性能最差的函数重写一遍`
- `这段代码有没有内存泄漏？`
- `用更现代的写法重构这个类`
- `解释一下你发现的 SQL 注入漏洞`

---

## 👨‍💻 关于作者

这是我独立开发的一个 AI 工具项目，用于探索 LLM Agent 在开发者工具领域的落地应用。

---

## 📄 License

MIT License — 欢迎 fork 和二次开发

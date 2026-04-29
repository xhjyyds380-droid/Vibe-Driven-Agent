# Vibe-Driven-Agent

实现从“自然语言需求”到“完整 Git 仓库”的端到端自动化。该工具将项目初始化与基础框架搭建的时间从数小时缩短至 5 分钟以内。目前已成功自动化构建了多个具备高度一致性的技术原型，代码规范达标率提升了 90% 以上，极大提升了开发者在“Vibe Coding”模式下的生产效率。

## 🏗 核心架构

```mermaid
graph LR
  A[用户意图/Vibe] --> B[Vibe Analyzer]
  B --> C[Agent Architect]
  C --> D[Git Repo Generation]
  D --> E[CI/CD Verification]


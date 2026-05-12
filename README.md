# deepseek-chat-analysis

对 [chat.deepseek.com](https://chat.deepseek.com/) 页面结构的分析记录。

## 📋 说明

这是一份**学习笔记**，记录了作者在使用 DeepSeek 过程中对前端页面结构的一些探索。

### 包含内容

- **`structure.json`** — 页面零件树及状态字典的完整 JSON 数据
- **`page-structure.md`** — 可读性更好的页面结构文档（由 `render_structure.py` 生成）
- **`结构数据说明.md`** — structure.json 的字段说明文档
- **`render_structure.py`** — 将 structure.json 渲染为 Markdown 的脚本
- **`auto_test.py`** — 基于 Playwright 的自动化状态检测脚本
- **`prompt-but-dont-read.txt`** — 原始 prompt

### 关于标签（Tag）

本地仓库的 tag 中包含了与 DeepSeek v4 Flash 愉快合作的方式，感兴趣的朋友可以看看。

### ⚠️ 注意事项

本项目仅作为学习和技术交流，**不对 chat.deepseek.com 进行任何过分的自动化控制或爬虫行为**。请合理使用，尊重网站服务。

## 🚀 使用

```bash
# 查看结构文档
cat page-structure.md

# 渲染最新的 Markdown（需要 structure.json）
python render_structure.py

# 运行自动化测试（需要安装 playwright）
pip install playwright
playwright install
python auto_test.py detect
```
# HW02：论文导读 + DeepSeek/OpenAI 兼容 Chatbot 示例

本目录为本次作业的实现目录，包含：

- ✅ **任务一**：论文导读（Segment Anything）与配图
- ✅ **任务二**：可运行的 Chatbot 示例（DeepSeek / OpenAI 兼容 API）

---

## 任务一：论文导读（导读/配图）

### 1. 论文来源
- 论文：**Segment Anything**
- 来源：Meta AI Research（arXiv 2023）

### 2. 导读生成方式
- 本文档的正文由**大模型（OpenAI GPT-4）生成**。
- 生成后由作者进行编辑润色，保证内容准确、结构清晰。

### 3. 配图方式
- 本项目手动从 Segment Anything 官方仓库中获取配图（`assets/model_diagram.png`）。
- 图片已保存至 `sam_reading/assets/`，并在导读文档中手动插入，并附有图注说明。

---

## 任务二：Chatbot 示例（DeepSeek / OpenAI 兼容接口）

本目录中提供一个可运行的简单 Chatbot 示例脚本：`chatbot_deepseek.py`。

### 运行环境
- Python 3.8+
- 建议在虚拟环境中运行（`python -m venv .venv`）

### 依赖安装
```bash
python -m pip install -r requirements.txt
```

### API Key / 环境变量配置
1) **OpenAI 兼容接口（推荐）**
```bash
set OPENAI_API_KEY=你的_api_key_here
```

2) **如果使用 DeepSeek / VolcEngine 等自定义 OpenAI 兼容 API**
```bash
set OPENAI_API_KEY=你的_api_key_here
set OPENAI_API_BASE=https://api.your-provider.com/v1
```

> 注意：如果你使用的是火山引擎等平台，请参考该平台官方文档，填写正确的 Endpoint/Key。

### 运行命令
```bash
python chatbot_deepseek.py
```

### 示例输入/输出
```
> 你好，请用一句话解释什么是 Segment Anything 模型？

=== Response ===
Segment Anything 是一个可 prompt 的视觉分割基础模型，它可以根据用户给出的点、框或文本提示生成图像中的目标掩码。
===============
```

---

## 课程任务说明（简要）

- **任务一**：在本仓库中生成了一份论文导读文档 `导读_Segment_Anything.md`，内容包括论文背景、方法、结果、小结，以及手动插入的图示。
- **任务二**：在本目录提供了 `chatbot_deepseek.py`，用于演示如何调用 DeepSeek/OpenAI 兼容接口。

如需扩展（例如增加“图像输入 + SAM 掩码可视化”示例），可以继续提问。

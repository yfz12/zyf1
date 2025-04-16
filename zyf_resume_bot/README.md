
# 张宇峰 自我介绍机器人

这是一个基于 Streamlit + OpenAI 的智能简历问答机器人，支持你在浏览器中提问关于张宇峰的经历、项目等内容。

## 使用方法

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 设置 OpenAI API Key
设置环境变量或在 .streamlit/secrets.toml 中添加：
```toml
OPENAI_API_KEY = "your-key-here"
```

### 3. 运行项目
```bash
streamlit run app.py
```

打开浏览器访问 http://localhost:8501 开始使用

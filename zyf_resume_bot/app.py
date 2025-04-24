
import streamlit as st
from openai import OpenAI
from utils import get_context_from_resume
import os

st.set_page_config(page_title="张宇峰自我介绍机器人", page_icon="🤖")
st.title("🤖 张宇峰的自我介绍机器人")
st.write("欢迎提问关于我个人工作经历、项目、技能等方面的问题~")

openai_api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.warning("请设置 OpenAI API 密钥")
    st.stop()

question = st.text_input("请输入你的问题")

if question:
    resume_context = get_context_from_resume("resume.md", question)

    prompt = f"""
你是一个AI机器人，专门回答关于“张宇峰”的个人履历问题。以下是他的简历片段，你需要基于这些内容回答问题：

简历内容：
{resume_context}

用户提问：
{question}

请基于简历内容简洁专业地回答：
"""

    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=600,
    )
    st.markdown("### 回答：")
    st.write(response.choices[0].message.content)

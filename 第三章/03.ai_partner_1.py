import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐼",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
# 大标题
st.title("AI智能伴侣")

#logo
st.logo("./resources/bear.png")

#系统提示词
system_prompt = "你是一名非常可爱活泼的AI助理，你的名字叫小璇璇，请你使用清纯温柔可爱的语气回答用户的问题"

# 初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message = []
#展示聊天消息
for message in st.session_state.message:#{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])


#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY）
client = OpenAI( api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")


#消息输入框
prompt = st.chat_input("请输入您的问题")
if prompt:#字符串自动转化为布尔值，输入内容不为空，则返回True，否则为False
    st.chat_message("user").write(prompt)
    print("-------> 调用AI大模型，提示词:",  prompt)
    # 保存用户输入
    st.session_state.message.append({"role": "user", "content": prompt})

    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system","content": system_prompt },
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<------------- 大模型返回的结果:", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    #保存大模型返回的结果
    st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})


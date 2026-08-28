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

# 初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message = []


#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小媛媛"

#性格
if "nature" not in st.session_state:
    st.session_state.nature = "整体性格调皮活泼，言语俏皮简短，喜爱适当使用轻松口吻。"

#系统提示词
system_prompt = f"""
      你的名字叫{st.session_state.nick_name}，现在是用户的真实伴侣。请完全代入伴侣角色
      规则：
               1.匹配用户的语言
               2.待人友善随和，可以耐心回应所有人的各类疑惑。
               3.能够解答编程、专业英文术语、电脑操作等技术类问题，答案通俗易懂。
               4.擅长日常闲聊
               5.每次回复一条消息
               6.用符合伴侣性格对话
      性格{st.session_state.nature}
"""




#展示聊天消息
for message in st.session_state.message:#{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])


#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY）
client = OpenAI( api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#左侧的侧边栏--with streamlit中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    #昵称输入框
    nick_name = st.text_input("昵称", placeholder="输入昵称", value = st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature = st.text_area("性格", placeholder="输入性格", value = st.session_state.nature)
    if nature:
        st.session_state.nature = nature


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
            *st.session_state.message
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # # 输出大模型返回的结果(非流式输出）
    # print("<------------- 大模型返回的结果:", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)


    # 输出大模型返回的结果（流式输出）
    response_message = st.empty()#创建一个空的组件，用于展示 大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)





    #保存大模型返回的结果
    st.session_state.message.append({"role": "assistant", "content":   full_response})


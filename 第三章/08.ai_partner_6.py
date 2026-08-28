import streamlit as st
import os
from openai import OpenAI
import json
from datetime import datetime

#设置页面配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐼",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
#生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")



#保存会话信息函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 如果sessions不存在，则创建一个
        if not os.path.exists("./第三章/sessions"):
            os.mkdir("./第三章/sessions")
        # 保存会话数据
        with open(f"./第三章/sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#加载所有的会话列表信息
def load_sessions():
    session_list = []
    #加载sessions目录下的文件
    if os.path.exists("./第三章/sessions"):
       file_list =  os.listdir("./第三章/sessions")
       for filename in file_list:
           if filename.endswith(".json"):
               session_list.append(filename[:-5])
    session_list.sort(reverse=True)#排序，降序排序
    return session_list

#加载指定会话信息函数
def load_session(session_name):
    try:
        if os.path.exists(f"./第三章/sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"./第三章/sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_data["current_session"]
                st.session_state.messages = session_data["messages"]
    except Exception:
      st.error("加载会话失败")
#删除会话信息函数
def delete_session(session_name):
    try:
        if os.path.exists(f"./第三章/sessions/{session_name}.json"):
            #删除文件
             os.remove(f"./第三章/sessions/{session_name}.json")
            #如果删除的是当前会话，则需要更新消息列表
             if session_name == st.session_state.current_session:
                 st.session_state.messages = []
                 st.session_state.current_session = generate_session_name()
    except Exception:
      st.error("删除会话失败")


# 大标题
st.title("AI智能伴侣")

#logo
st.logo("第三章/resources/bear.png")

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []


#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小媛媛"

#性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼可爱温柔"

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

#系统提示词
system_prompt = f"""
      你的名字叫{st.session_state.nick_name}，现在是用户的真实伴侣。请完全代入伴侣角色
      规则：
               1.匹配用户的语言
               2.待人友善随和，可以耐心回应所有人的各类疑惑。
               3.擅长日常闲聊
               4.每次回复一条消息
               5.用符合伴侣性格对话
      性格{st.session_state.nature}
"""




#展示聊天消息
st.text(f"会话信息:{st.session_state.current_session}")
for message in st.session_state.messages:#{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])


#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY）
client = OpenAI( api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#左侧的侧边栏--with streamlit中上下文管理器
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")
    # 新建会话
    if st.button("新建会话", width = "stretch", icon = "🗡️"):
        #1.保存当前会话信息
        save_session()


        #2.创建新的会话
        if st.session_state.messages:#如聊天信息非空，True;否则为False
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()# 重新运行页面
    #会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4,1])
        # 加载会话信息
        # 三元运算符：如果条件为真，返回第一个表达式的值，否则返回第二个表达式的值 -->语法：值1 if 条件表达式 else 值2
        with col1:
            if st.button(session, width="stretch", icon="🗒️", key =f"load_{session}", type = "primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        # 删除会话信息
        with col2:
            if st.button("", width="stretch", icon="❌️", key =f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 分隔线
    st.divider()





    # 伴侣信息
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
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system","content": system_prompt },
            *st.session_state.messages
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
    st.session_state.messages.append({"role": "assistant", "content":   full_response})

    # 保存会话信息
    save_session()




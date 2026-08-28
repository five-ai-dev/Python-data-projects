import streamlit as st

st.set_page_config(
    page_title="streamlit入门测试",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "#  这是一个streamlit入门页面"
    }
)
#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")


#段落文字
st.write("螳螂这个名字，源于它标志性的姿态。它平时喜欢把一对粗壮的前足弯曲着举在胸前，就像在合掌祈祷一样，因此古人在造字时用了“螳”字，而在西方，它也被直接称为“祈祷者”（Mantis）。不过这个虔诚的姿态完全是假象，它其实是在随时准备捕猎。")
st.write("螳螂的外形极具辨识度。它的身体通常呈翠绿色或褐色，体表光滑，能完美融入草丛和树叶之间。最显眼的是它那对镰刀状的捕捉足，内侧长有一排坚硬的锯齿，是它捕食的致命武器。它的头部呈三角形，非常灵活，可以自由转动观察四周，一双大复眼异常突出，赋予了它极佳的视力。")
st.write("螳螂是纯粹的肉食性昆虫，也是自然界中顶级的伏击猎手。它的食物范围很广，主要以苍蝇、蝗虫、蝴蝶等小型昆虫为食，大型螳螂甚至能捕食小鸟和蜥蜴。捕猎时，它会一动不动地潜伏，一旦猎物进入攻击范围，前足便会以极快的速度弹射而出，牢牢钳住猎物。此外，螳螂还有着残忍的繁殖习性，雌性螳螂有时会在交配过程中吃掉雄性，以获取充足的营养来产卵。")


#图片
st.image("./resources/mantis.jpg", width=300)

#音频
st.audio("./resources/cricket chirping.mp3")

#视频
st.video("./resources/mantis hunting.mp4")


#logo
st.logo("./resources/bear.png")


#表格
insect_data ={
    "name":["mantis", "beetle", "weta", "butterfly"],
    "body_score": [60, 90, 80, 60],
    "combat_score": [85, 95, 85, 40],
    "defense_score": [70, 100, 80, 20],
    "beauty_score": [90, 100, 80, 95]
}
st.table(insect_data)
#输入框
#普通输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名是{name}")

#密码输入框
password = st.text_input("请输入密码", type = "password")
st.write(f"您输入的密码是{password}")


#单选按钮
gender = st.radio("请输入您的性别",["男", "女", "未知"])
st.write(f"您的性别是{gender}")

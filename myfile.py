import streamlit as st
from streamlit.components.v1 import html


st.text("Tuần này mọi người đóng cho Cường nhé; chi tiết ở bảng dưới đây")

st.image("https://i.imgur.com/rtRALUN.png")

st.write("Ai đóng xong gạt nút dưới này nè")

agree1 = st.checkbox('Huy')
agree2 = st.checkbox('Thảo')
agree3 = st.checkbox('Đức')
agree4 = st.checkbox('Giang')
agree5 = st.checkbox('Hà')
agree6 = st.checkbox('Linh')

st.title("Gièo cầu lông..")
st.snow()

user = st.text_input('Tên mày là gì?')

if st.confirm_button('Authenticate', user):
    do_something()
else:
    st.error('Youve been hacked by f.')

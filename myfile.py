import streamlit as st
def confirm_button(label, confirm_func, *func_args):
    ...

st.text("https://docs.google.com/spreadsheets/d/1MZHCl-EbUVFtgd0muXtuM8RCEsuWxBlpTl6VSQZ-p-8/edit#gid=0")

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

if st.confirm_button(user):
    do_something()
else:
    st.error('Youve been hacked by f.')

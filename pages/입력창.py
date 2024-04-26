import streamlit as st
import random

st.title("여러 가지 입력창")

import streamlit as st

st.button("리셋 버튼", type="primary")
if st.button('랜덤 숫자 생성'):
    st.write(random.random())
else:
    st.write('Goodbye')



text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)


st.link_button("Go to gallery", "https://streamlit.io/gallery")


agree = st.checkbox('동의합니다.')

if agree:
    st.write('동의하셨습니다! 다음 문항으로 갑시다. ')
else:
    st.write('동의 버튼을 먼저 클릭해주세요.')


import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'], #선택지
    ['Yellow', 'Red']) #기본 선택 옵션

st.write('You selected:', options)


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)



number = st.number_input('숫자를 입력해주세요.',step=1)
st.write('The current number is ', number)



title = st.text_area('Movie title', 'Life of Brian') #큰 텍스트 
st.write(title,'을 보셨군요! 저도요!')

import pandas as pd
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    #bytes_data = uploaded_file.read()
    data = pd.read_csv(uploaded_file, encoding = 'euc-kr')
    st.write("filename:", uploaded_file.name)
    st.write(data)
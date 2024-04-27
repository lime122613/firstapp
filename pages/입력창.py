import streamlit as st
import random

st.title("여러 가지 입력창")

st.write("<h4>1.랜덤 숫자 생성</h4>", unsafe_allow_html=True)

st.button("리셋 버튼", type="primary")
if st.button('랜덤 숫자 생성'):
    st.write(random.random())
else:
    st.write('Goodbye')



st.write("<h4>2.하이퍼링크</h4>", unsafe_allow_html=True)
st.link_button("세화여고 리로스쿨 바로가기", "https://sehwags.riroschool.kr/")


st.write("<h4>3.체크박스</h4>", unsafe_allow_html=True)
st.write("<개인정보 동의서>")
agree = st.checkbox('동의합니다.')

if agree:
    st.write('동의하셨습니다! 다음 문항으로 갑시다. ')
else:
    st.write('동의 버튼을 먼저 클릭해주세요.')

st.write("<h4>4.여러 선택지</h4>", unsafe_allow_html=True)
options = st.multiselect(
    '가장 좋아하는 색깔은?',
    ['Green', 'Yellow', 'Red', 'Blue'], #선택지
    ['Yellow', 'Red']) #기본 선택 옵션

st.write('당신의 선택은:', options)

st.write("<h4>5.객관식 선택</h4>", unsafe_allow_html=True)
genre = st.radio(
    "가장 좋아하는 영화 장르를 선택해주세요",
    [":rainbow[로맨틱코미디]", "***액션***", "다큐멘터리 :movie_camera:"],
    index=None,
)

st.write("당신은", genre,"장르를 좋아하시는군요!")


st.write("<h4>6.숫자 간격</h4>", unsafe_allow_html=True)
n = st.slider('숫자의 증/감 간격을 설정해주세요', 0, 100)
number = st.number_input('숫자를 선택해주세요.',step=n)
st.write('현재 숫자: ', number)


st.write("<h4>7.긴 글 입력창</h4>", unsafe_allow_html=True)
title = st.text_area('영화 제목 작성', 'Life of Brian') #큰 텍스트 
st.write(title,'을 보셨군요! 저도요!')

st.write("<h4>8.csv 파일 업로드</h4>", unsafe_allow_html=True)
import pandas as pd
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    #bytes_data = uploaded_file.read()
    data = pd.read_csv(uploaded_file, encoding = 'euc-kr')
    st.write("filename:", uploaded_file.name)
    st.write(data)
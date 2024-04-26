import streamlit as st

st.title("CSV 파일 인코딩 변환")
st.write("한글 csv파일을 열었을 때 깨진다면 인코딩 형식이 다르기 때문입니다! utf-8형식으로 변환합시다!")

import pandas as pd
uploaded_files = st.file_uploader("변환하고 싶은 CSV 파일을 업로드해주세요.", accept_multiple_files=True)
if uploaded_files:  # 파일이 업로드되었는지 여부 확인
    for uploaded_file in uploaded_files:
        data = pd.read_csv(uploaded_file, encoding='cp949')
        st.write("filename:", uploaded_file.name)
        st.write(data)

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(encoding='utf-8-sig').encode('utf-8-sig') #return df.to_csv().encode('utf-8')

    csv = convert_df(data)

    st.download_button(
        label="변환된 CSV파일 다운!",
        data=csv,
        file_name= '(utf-8)'+uploaded_file.name+'.csv',
        mime='text/csv',
    )
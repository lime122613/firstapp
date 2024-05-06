# import streamlit as st
# import pandas as pd

# st.title("CSV 파일 인코딩 변환")
# st.write("한글 csv파일을 열었을 때 깨진다면 인코딩 형식이 다르기 때문입니다! utf-8형식으로 변환합시다!")

# uploaded_files = st.file_uploader("변환하고 싶은 CSV 파일을 업로드해주세요.", accept_multiple_files=True)
# if uploaded_files:  # 파일이 업로드되었는지 여부 확인
#     for uploaded_file in uploaded_files:
#         data = pd.read_csv(uploaded_file, encoding='cp949')
#         st.write("filename:", uploaded_file.name)
#         st.write(data)

#     def convert_df(df):
#         # IMPORTANT: Cache the conversion to prevent computation on every rerun
#         return df.to_csv(encoding='utf-8-sig').encode('utf-8-sig') #return df.to_csv().encode('utf-8')

#     csv = convert_df(data)

#     st.download_button(
#         label="변환된 CSV파일 다운!",
#         data=csv,
#         file_name= '(utf-8)'+uploaded_file.name+'.csv',
#         mime='text/csv',
#     )


import streamlit as st
import pandas as pd
import chardet

st.title("CSV 파일 인코딩 변환")
st.write("CSV 파일을 불러왔을 때 에러가 난다면 인코딩 형식이 다를 수 있습니다. UTF-8 형식으로 변환합시다!")

uploaded_files = st.file_uploader("변환하고 싶은 CSV 파일을 업로드해주세요.", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        # 파일을 바이트 형식으로 읽기
        raw_data = uploaded_file.getvalue()
        # 파일의 인코딩 형식 추측
        result = chardet.detect(raw_data)
        # 추측된 인코딩으로 CSV 파일 읽기
        data = pd.read_csv(uploaded_file, encoding=result['encoding'])
        st.write("파일명:", uploaded_file.name)
        st.write(data.head(5))

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(encoding='utf-8-sig').encode('utf-8-sig') #return df.to_csv().encode('utf-8')

    csv = convert_df(data)

    st.download_button(
        label="변환된 CSV 파일 다운로드!",
        data=csv,
        file_name='(utf-8)' + uploaded_file.name + '.csv',
        mime='text/csv',
    )

import streamlit as st
import requests
import pandas as pd

st.title("공공데이터 API 호출")

response = requests.get("http://127.0.0.1:8000/data", timeout=10)
data_1 = response.json()  # ✅ 핵심 수정

df = pd.DataFrame(data_1["response"]["body"]["items"]["item"])  # ✅ 표로 만들기

st.subheader("데이터 목록")
st.dataframe(df)

import requests  #http 요청
import os
from fastapi import FastAPI
import streamlit as st
import pandas as pd
from fastapi import FastAPI

SERVICE_KEY = os.getenv("SERVICE_KEY")

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

params = { 
            "serviceKey" : SERVICE_KEY,
            "pageNo" : 1,
            "numOfRows" : 10,
            "dataType" : "JSON",

            "base_date": "20260219",
            "base_time": "1900",
            "nx": 63,
            "ny": 89,
            }

res = requests.get(url, params=params, timeout=10)

#-----------------------------------------------------------------------------------------------------------------

app = FastAPI()

@app.get("/data")  #정의 부분
def read_root():    # res 리턴하는 함수? 이게뭐지
    return res


# data = {
#     'fruit': 'apple',
#     'book': 'maths',
#     'game': 'football',
#     'details': {
#         'level1': {'level2': {'level3': {'a': 'b'}}}
#     }
# }



# st.json(data)

print(res.status_code)
print(res.text)

#json형식 저장하기?
# with open('res.json', 'w', encoding='utf-8') as f:

#--------------------------------------------------------------------------------------------------------위는 백 아래부터 프론트

st.title("공공데이터 API 호출")
response = requests.get("/data")
data_1 = response.json

#데이터프레임 변환
df = pd.DataFrame(data_1) #시각화 쉽게
st.subheader("데이터 목록") 
st.dataframe(df)  #표 띄우기
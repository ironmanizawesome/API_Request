import requests  # http 요청
from fastapi import FastAPI
import os  #파일이동
from dotenv import load_dotenv  #.env로

load_dotenv() #아 얘때메 진짜 개고생했네
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

app = FastAPI()

@app.get("/data")
def read_root():
    return res.json()  # ✅ 핵심 수정(이부분 때문에 막힘)

print(res.status_code)
print(res.text)

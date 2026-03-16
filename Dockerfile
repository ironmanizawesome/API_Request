FROM python:3.11

# 작업 디렉토리 생성
WORKDIR /Users/ironm/dev

# 의존성 설치 + 필요한 파일 복사(COPY)
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY final.py final.py
COPY .env .env
#처음에  final.py 안넣음...
CMD [ "streamlit","run", "final.py", "--server.port=8000","server.adress=0.0.0.0" ]

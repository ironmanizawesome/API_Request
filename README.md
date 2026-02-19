# API_Request

main.py, app.py는 끄적끄적 실험해보다가..
프론트 백 서로 분리를 안해서 꼬인 바람에 서로 분리해서 다시 정리해보았음. 

python -m uvicorn backend:app --reload --port 8000 #백엔드
streamlit run frontend.py #프론트


#######기능 upgrade 하기 위해 실시간으로 현재 시간에 맞게 설정 하는 부분도 있ㄹ으면 좋을것
#######코드값정보에 맞에 단위도 변환하면 좋을 것
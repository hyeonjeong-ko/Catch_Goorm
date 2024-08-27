# 베이스 이미지 설정
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 애플리케이션 파일 복사
COPY . .

# Flask 애플리케이션 실행
CMD ["python", "app.py"]

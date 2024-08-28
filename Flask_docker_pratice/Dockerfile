# Dockerfile
# 1. Python 베이스 이미지 사용
FROM python:3.9

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 파일을 컨테이너에 복사하고, 필요한 패키지 설치
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 4. 애플리케이션 코드 복사
COPY . .

# 5. Flask 애플리케이션 실행
CMD ["python", "app.py"]

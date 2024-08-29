# Python 3.9 이미지를 베이스로 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 요구 사항 파일을 컨테이너에 복사
COPY requirements.txt requirements.txt

# 의존성 설치
RUN pip install --no-cahche-dir -r requirements.txt

# 애플리케이션 소스 코드를 컨테이너에 복사
COPY . .

# 컨테이너가 시작될 때 실행될 명령어
CMD ["python", "app.py"]

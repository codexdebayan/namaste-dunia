From python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

cmd ["python", "-m", "pytest","appTest.py"]
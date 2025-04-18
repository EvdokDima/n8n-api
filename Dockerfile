FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    libavif-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./main.py"]
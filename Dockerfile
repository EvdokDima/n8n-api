FROM python:3.12-alpine3.21

WORKDIR /app

RUN apk add --no-cache build-base python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./main.py"]
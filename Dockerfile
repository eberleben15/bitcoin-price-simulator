# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY web ./web

# Ensure all files in the web directory are readable
RUN chmod -R 644 ./web

CMD ["python", "src/main.py"]
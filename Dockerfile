# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY web ./web


# Ensure all files are accessible
RUN chmod -R 644 ./web \
    && adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app

USER appuser

CMD ["python", "src/main.py"]
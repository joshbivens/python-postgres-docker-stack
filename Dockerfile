FROM python:3.11-slim

RUN apt-get update; apt-get install -y libpq-dev gcc; rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install psycopg2-binary

COPY app.py .

CMD ["python", "app.py"]

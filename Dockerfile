FROM python:3.11-slim

WORKDIR /fastapi-app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY alembic.ini .
COPY migrations migrations

COPY src src

CMD ["uvicorn", "src:app", "--host", "0.0.0.0", "--port", "8000"]


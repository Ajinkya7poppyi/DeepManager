FROM python:3.8.10 as build

WORKDIR /usr/src/app


COPY requirements.txt .
COPY app/ ./app/
RUN ls -la ./app/*

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

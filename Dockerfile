FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip wheel
RUN pip install --no-cache-dir -r requirements.txt


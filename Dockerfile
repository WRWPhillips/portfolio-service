FROM python:3.10-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./


CMD ["python", "app.py"]

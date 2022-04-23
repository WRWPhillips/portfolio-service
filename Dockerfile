FROM python:3.10-slim

RUN apt-get update && apt-get install -y build-essential

RUN useradd -m heroku-user

WORKDIR /app 

RUN chown -R heroku-user:heroku-user /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./


CMD ["python", "app.py"]

FROM python:3.10-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

ENV FLASK_APP=server.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

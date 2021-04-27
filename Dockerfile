FROM tiangolo/meinheld-gunicorn-flask:latest
WORKDIR /app/
COPY ./requirements.txt ./requirements.txt
RUN [ "pip", "install", "-r", "requirements.txt" ]
COPY . .

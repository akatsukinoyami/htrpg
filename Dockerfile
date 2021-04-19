FROM tiangolo/meinheld-gunicorn-flask:latest
WORKDIR /app/
COPY . .

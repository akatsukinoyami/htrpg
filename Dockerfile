FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
WORKDIR /app/
COPY . .
CMD ["python3", "app.py"]

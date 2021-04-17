FROM python:3.8-slim-buster
WORKDIR /app/
RUN ["pip3", "install", "flask"]
ENV FLASK_APP=start
COPY . .
CMD ["python3", "app.py"]

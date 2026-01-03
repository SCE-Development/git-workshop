FROM python:3.10.2-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY server.py .

EXPOSE 3000

ENTRYPOINT ["python3","server.py"]
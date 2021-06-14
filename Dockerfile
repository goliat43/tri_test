# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY tri_test tri_test

ENV FLASK_APP=tri_test

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
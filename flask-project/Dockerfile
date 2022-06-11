FROM python:3.10.4-slim-bullseye

#make and change to a working directory inside the container
WORKDIR /usr/src/flask-project

#copy all the files into this directory including requirements.txt
COPY . .

RUN python -m venv venv
RUN venv/bin/pip3 install -r requirements.txt
RUN venv/bin/ipi3 install gunicorn

ENV FLASK_APP app.py

CMD gunicorn -w 3 -b 0.0.0.0:8080 ./wsgi.py --reload

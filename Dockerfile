FROM python:3.10

RUN mkdir /api

WORKDIR /api

COPY libraries.txt .

RUN pip install -r libraries.txt

COPY . .

#WORKDIR APIvenv

#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
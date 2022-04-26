FROM python:3.9.6-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY requirements.txt .
COPY requirements_local.txt .
RUN pip install -r requirements.txt -r requirements_local.txt


CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
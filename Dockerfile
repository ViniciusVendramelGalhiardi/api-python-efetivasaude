# FROM python:3.9
FROM --platform=linux/amd64 python:3.9

WORKDIR /app

ADD requirements.txt .

USER root

RUN apt-get update \
  && apt-get -y install curl

RUN apt-get update \
  && apt-get -y install unixodbc unixodbc-dev

RUN apt-get update \
  && apt-get -y install gcc gnupg2 \
  && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update \
  && ACCEPT_EULA=Y apt-get -y install msodbcsql17 \
  && ACCEPT_EULA=Y apt-get -y install mssql-tools

RUN apt-get update \ 
  && pip install pyodbc

RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
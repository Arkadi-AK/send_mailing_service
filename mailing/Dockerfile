FROM python:2.7
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app/mailing

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="/usr/local/bin"


COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

ENTRYPOINT ["sh", "entrypoint.sh"]
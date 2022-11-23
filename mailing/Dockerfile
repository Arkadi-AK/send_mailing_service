FROM python:2.7
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app/mailing

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV PYTHONPATH="$PWD/venv"
ENV VIRTUAL_ENV "/venv"
#RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
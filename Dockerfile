FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py loaddata initial_data.json

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
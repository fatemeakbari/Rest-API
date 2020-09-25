
FROM python:3.6.1


RUN pip install flask flask-sqlalchemy flask-restplus flask-admin  redis openpyxl psycopg2-binary gunicorn flask-restful

RUN mkdir -p /flaskapp/app
WORKDIR /flaskapp/app/
COPY . /flaskapp/app
CMD [ "gunicorn", "--bind", "0.0.0.0:5008","wsgi:flask_app" ]

FROM python:3.8

RUN apt-get update && apt-get install -y nginx vim curl net-tools

RUN mkdir -p /home/proj
WORKDIR /home/proj

COPY . .
RUN cp /home/proj/nginx/default /etc/nginx/sites-enabled/default
RUN cp /home/proj/index.html /var/www/html/index.html

RUN pip3 install -r requirements.txt

ENTRYPOINT /etc/init.d/nginx restart && python3 /home/proj/webapp/manage.py runserver 0.0.0.0:8000 && /bin/bash


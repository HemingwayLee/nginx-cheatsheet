FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  man \
  vim \
  net-tools

WORKDIR /etc/nginx/sites-enabled
RUN rm -f default
COPY default /etc/nginx/sites-enabled/default

COPY index.html /var/www/html/index.html

RUN mkdir -p /var/www/html/static/
COPY main.css /var/www/html/static/main.css


ENTRYPOINT /etc/init.d/nginx restart && /bin/bash


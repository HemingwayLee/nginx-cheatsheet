FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  vim \
  net-tools

COPY . .
RUN cp default /etc/nginx/sites-enabled/default
RUN cp index.html /var/www/html/

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash


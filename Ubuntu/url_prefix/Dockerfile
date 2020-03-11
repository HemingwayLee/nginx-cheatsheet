FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  man \
  vim \
  net-tools

RUN mkdir -p /var/www/html/abc
WORKDIR /var/www/html/
RUN mv index.nginx-debian.html /var/www/html/abc/index.nginx-debian.html

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash


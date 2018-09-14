FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  man \
  vim \
  net-tools

WORKDIR /etc/nginx/sites-enabled
RUN rm -f default
COPY default /etc/nginx/sites-enabled/default

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash


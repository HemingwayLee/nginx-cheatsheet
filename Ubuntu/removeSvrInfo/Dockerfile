FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  man \
  vim \
  net-tools \
  nginx-extras

RUN sed -i '11i        more_clear_headers Server;' /etc/nginx/nginx.conf

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash


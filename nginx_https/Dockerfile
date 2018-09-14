FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  man \
  vim \
  net-tools \
  openssl

RUN mkdir -p /etc/nginx/ssl
WORKDIR /etc/nginx/ssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -subj '/C=JP/ST=Fukuoka/L=Fukuoka/CN=www.kenny.com'

WORKDIR /etc/nginx/sites-enabled
RUN sed -i 's/# listen 443 ssl default_server;/listen 443 ssl;/g' default
RUN sed -i 's/server_name _/server_name www.kenny.com/g' default
RUN sed -i "42i ssl_certificate /etc/nginx/ssl/nginx.crt;" default
RUN sed -i "43i ssl_certificate_key /etc/nginx/ssl/nginx.key;" default

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash

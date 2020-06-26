FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  net-tools

COPY default /etc/nginx/sites-enabled/default

ENTRYPOINT nginx && /bin/bash

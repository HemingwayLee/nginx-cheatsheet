FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  net-tools \
  vim

WORKDIR /var/www/html
RUN mv index.nginx-debian.html index.html

RUN mkdir -p /home/my_abc
RUN mkdir -p /srv/my_xyz

RUN echo "<h1>ABC folder</h1>" >> /home/my_abc/index.html
RUN echo "<h2>XYZ is here...</h2>" >> /srv/my_xyz/index.html

COPY default /etc/nginx/sites-enabled/default

ENTRYPOINT nginx && /bin/bash

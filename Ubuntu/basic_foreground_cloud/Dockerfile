FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  nginx \
  man \
  vim \
  net-tools

WORKDIR /var/www/html
COPY focus.html /var/www/html/focus.html

CMD ["nginx", "-g", "daemon off;"]


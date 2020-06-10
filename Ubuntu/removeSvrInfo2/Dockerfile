FROM nginx

RUN apt-get update && apt-get install -y \
  man \
  vim \
  net-tools \ 
  nginx-extras

RUN sed -i '17i        more_clear_headers Server;' /etc/nginx/nginx.conf
RUN cat /etc/nginx/nginx.conf

ENTRYPOINT /etc/init.d/nginx restart && /bin/bash


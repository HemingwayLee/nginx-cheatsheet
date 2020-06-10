FROM nginx

RUN apt-get update && apt-get install -y \
  man \
  vim \
  net-tools 

RUN sed -i '2s/80/8888/' /etc/nginx/conf.d/default.conf

RUN touch /var/run/nginx.pid && \
  chown -R www-data:www-data /var/run/nginx.pid && \
  chown -R www-data:www-data /var/cache/nginx && \
  chown -R www-data:www-data /etc/nginx/conf.d

EXPOSE 8888

USER www-data

ENTRYPOINT nginx -g 'daemon off;' && /bin/bash


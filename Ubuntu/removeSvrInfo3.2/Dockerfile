FROM nginx

RUN apt-get update && apt-get install -y \
  man \
  vim \
  net-tools \ 
  nginx-extras

RUN which vim

RUN sed -i '2s/80/8888/' /etc/nginx/conf.d/default.conf
RUN cat /etc/nginx/conf.d/default.conf
RUN cp /etc/nginx/conf.d/default.conf /etc/nginx/sites-enabled/default

RUN sed -i '17i        more_clear_headers Server;' /etc/nginx/nginx.conf
RUN cat /etc/nginx/nginx.conf

RUN touch /var/run/nginx.pid && \
  chown -R www-data:www-data /var/run/nginx.pid && \
  chown -R www-data:www-data /var/lib/nginx && \
  chown -R www-data:www-data /etc/nginx/conf.d && \
  chown -R www-data:www-data /etc/nginx/sites-enabled

EXPOSE 8888

USER www-data

ENTRYPOINT nginx -g 'daemon off;' && /bin/bash

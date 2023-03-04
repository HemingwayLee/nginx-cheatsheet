FROM tensorflow/tensorflow:latest-jupyter

RUN apt-get update && apt-get install -y \
  nginx \
  vim \
  net-tools

RUN mkdir -p /home/myapp
WORKDIR /home/myapp
COPY . /home/myapp
RUN cp default /etc/nginx/sites-enabled/default 
RUN cp jupyter_notebook_config.py ~/.jupyter/

ENTRYPOINT /etc/init.d/nginx restart && /home/myapp/run.sh && /bin/bash
# ENTRYPOINT /bin/bash


FROM centos:7

RUN yum -y update && yum install -y \
  sudo \
  vim \
  net-tools \
  yum-utils
  
RUN yum -y install epel-release
RUN yum -y update && yum -y install nginx 

WORKDIR /usr/share/nginx/html

ENTRYPOINT nginx && /bin/bash

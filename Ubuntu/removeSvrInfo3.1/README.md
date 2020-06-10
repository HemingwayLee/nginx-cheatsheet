# Tips
* it must be 8888, it can not be 80. The port under 1024 without root account will get the following error:
```
nginx: [emerg] bind() to 0.0.0.0:80 failed (13: Permission denied)
```

* it looks like after installing `nginx-extras`, nginx is pointing to `/etc/nginx/sites-enabled/default` instead of `/etc/nginx/conf.d/default.conf`

# How to run
```
docker run -it --rm -p8888:8888 my_nginx /bin/bash
```

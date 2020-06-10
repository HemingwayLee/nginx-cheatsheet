# Tips
* it must be 8888, it can not be 80. The port under 1024 without root account will get the following error:
```
nginx: [emerg] bind() to 0.0.0.0:80 failed (13: Permission denied)
```


# How to run
```
docker run -it --rm -p8888:8888 my_nginx /bin/bash
```

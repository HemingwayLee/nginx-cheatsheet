# How to use

```
docker build -t my-nginx .
docker run -it --rm -p 8899:80 my-nginx
```

# Note
The nginx is running in the background inside docker container. It is okay to use `-it` option, but it will be in `Exited(0)` status if we run it in `-d` mode

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                              PORTS               NAMES
26d4849fe5ed        mynginx             "/bin/sh -c '/etc/in…"   4 seconds ago       Exited (0) Less than a second ago                       clever_mirzakhani
``` 

Run the nginx in foreground (e.g., `CMD ["nginx", "-g", "daemon off;"]`) so that we can run it with `-d` option and it works correctly on the cloud (both AWS and Azure)



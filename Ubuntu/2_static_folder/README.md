# How to use

```
docker build -t my-nginx .
docker run -it --rm -p 8088:8088 my-nginx
```

## Run in detach mode

```
docker run -itd -p 8088:8088 my-nginx
```

## Stop

```
docker stop <container_id>
```
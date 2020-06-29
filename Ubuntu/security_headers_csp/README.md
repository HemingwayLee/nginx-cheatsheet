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

## Use `shcheck` to check headers

https://github.com/meliot/shcheck


## CSP Header
```
add_header Content-Security-Policy "default-src 'self' data:; style-src 'self' 'unsafe-in    line'"
```

`data:` is needed, and `unsafe-inline` is needed as well to show nginx default index.html


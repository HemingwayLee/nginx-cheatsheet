# Remove Server information from response header

# How to use

```
docker build -t my-nginx .
docker run -it --rm -p 80:80 my-nginx
```

# Tips
1. add `nginx-extras` to `apt-get install` 
2. add `more_clear_headers Server;` to `/etc/nginx/nginx.conf`


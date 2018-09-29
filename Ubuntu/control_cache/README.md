# How to use

```
docker build -t my-nginx .
docker run -it --rm -p 8899:80 my-nginx
```

# Test

If you change main.css on the server
```
vim /var/www/html/static/main.css
```

The browser load main.css from cache, the user can not see the changes.


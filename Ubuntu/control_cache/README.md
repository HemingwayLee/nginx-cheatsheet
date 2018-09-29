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
![from disk cache](https://user-images.githubusercontent.com/8428372/46242703-c6441a80-c406-11e8-99fa-0f7a231084c0.png)


# How to use

```
docker build -t my-nginx .
docker run -it --rm -p 8899:80 my-nginx
```

# Test

If you change main.css on the server,
```
vim /var/www/html/static/main.css
```

users will not able to see those changes you made because the browser loads main.css from cache (as shown below)

![from disk cache](https://user-images.githubusercontent.com/8428372/46242703-c6441a80-c406-11e8-99fa-0f7a231084c0.png)


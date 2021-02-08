# Run
```
docker build -t mynginx .
docker run -it --rm -p80:80 mynginx
```

# Note
* it does not work with browser
* use the following command to test
```
$ curl --http2-prior-knowledge localhost:80
```

We will get
```
<h2>I love nginx</h2>
```



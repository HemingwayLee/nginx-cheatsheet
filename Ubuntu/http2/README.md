# What
* http2 is faster than http1.1
* With nginx, it only supports h2c (which is what HTTP/2 without HTTPS is called), so you can not connect using HTTP/1.1

* Use the following command to connect
```
curl --http2-prior-knowledge localhost:80
```



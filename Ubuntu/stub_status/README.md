# Run
```
docker build -t mynginx .
docker run -it --rm -p80:80 mynginx
```

# Check does it support
```
nginx -V 2>&1 | grep --color -- --with-http_stub_status_module
```

# Test it
```
$ curl http://127.0.0.1/nginx_status
Active connections: 1 
server accepts handled requests
 3 3 3 
Reading: 0 Writing: 1 Waiting: 0
```

# Ref
https://www.nginx.com/blog/monitoring-nginx/


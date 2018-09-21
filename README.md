# nginx-cheatsheet

* Use nginx in any linux distribution
```
nginx 
nginx -s stop
nginx -s reload
```

## Ubuntu
* config file path:
```
/etc/nginx/sites-enabled/default
```

* default working folder
```
/var/www/html
```

## Centos
* config file path:
```
/etc/nginx/nginx.conf
```

* default working folder
```
/usr/share/nginx/html
```

## Log
* Error Log
We can set path and level:
```
error_log /var/log/nginx/error.log;
```

* Access Log
NGINX writes information about client requests in the access log right after the request is processed. 

```
http {
  log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

  access_log  /var/log/nginx/access.log  main;
}
```


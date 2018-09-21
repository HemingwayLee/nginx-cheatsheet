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
error_log logs/error.log warn;
```

* Access Log
NGINX writes information about client requests in the access log right after the request is processed. 


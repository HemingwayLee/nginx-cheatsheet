# nginx-cheatsheet

* Use nginx in any linux distribution
```
nginx 
nginx -s stop
nginx -s reload
```

* Run nginx in foreground
```
nginx -g 'daemon off;'
```

or in dockerfile
```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```

## Reasons
If we the nginx in the background inside docker container, it is okay to use `-it` option, but it will be in `Exited(0)` status if we run it in `-d` mode

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                              PORTS               NAMES
26d4849fe5ed        mynginx             "/bin/sh -c '/etc/in…"   4 seconds ago       Exited (0) Less than a second ago                       clever_mirzakhani
``` 

Run the nginx in foreground so that we can run it with `-d` option and it works correctly on the cloud (both AWS and Azure)

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

## Misc.

* Change web root to new location:

```
root /home/ubuntu;
```

* Redirect 404 to index page:

```
error_page 404 /index.html;
```

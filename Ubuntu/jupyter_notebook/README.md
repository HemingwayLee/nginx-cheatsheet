# What
Running jupyter notebook with nginx 

# How to run
```
docker build -t mynginx .
docker run -it --rm -p80:80 mynginx
```

# Issues
* Blocking Cross Origin API request
    * We need to put `jupyter_notebook_config.py` into `~/.jupyter/` folder
* Replacing stale connection
    * We need to add web socket part into `nginx default` file
* [413 Request Entity Too Large](https://github.com/jupyterlab/jupyterlab/issues/4214)
    * Add `client_max_body_size 0` into `nginx default` file

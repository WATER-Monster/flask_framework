# -*- coding=utf-8 -*-

from gevent import monkey
monkey.patch_all()
import gevent
import os


bind = "localhost:8000"
workers = os.cpu_count() * 2 + 1
threads = 1
timeout = 6000
backlog = 2048
worker_class = "gevent"
debug = False
proc_name = "gunicorn"
# pidfile = os.path.join(API_LOG_DIRNAME, "gunicorn.pid")
# logfile = os.path.join(API_LOG_DIRNAME, "gunicorn.log")
loglevel = "error"
# accesslog = os.path.join(API_LOG_DIRNAME, "gun_access.log")
# errorlog = os.path.join(API_LOG_DIRNAME, "gun_error.log")

# -*- coding=utf-8 -*-

import os
from gevent import monkey
monkey.patch_all()


bind = "localhost:8000"
workers = os.cpu_count() * 2 + 1
threads = 1
timeout = 60*10
backlog = 2048
worker_class = "gevent"

debug = False
daemon = True

proc_name = "gunicorn"

loglevel = "error"
accesslog = "log/access.log"
errorlog = "log/debug.log"
x_forwarded_for_header = 'X-FORWARDED-FOR'

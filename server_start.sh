#!/usr/bin/env bash

echo "starting server"
START="gunicorn -c gunicorn.py server:app"
eval $START
echo "done."
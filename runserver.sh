#!/bin/bash

exec ./manage.py runserver 0.0.0.0:$PORT

chmod +x runserver
./runserver
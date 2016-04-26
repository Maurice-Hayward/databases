#!/bin/bash

if [ -d "env" ]; then
	source env/bin/activate
	python manage.py runserver 0.0.0.0:8095
fi 

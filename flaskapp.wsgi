#!/usr/bin/python3
import sys
import logging

activate_this = '/var/www/red_dog__emachleder_mhathaway/app/env/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(),dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/red_dog__emachleder_mhathaway/")
sys.path.append("/var/www/red_dog__emachleder_mhathaway/app/")

from app import app as application
application.secret_key = '1234secretkey'


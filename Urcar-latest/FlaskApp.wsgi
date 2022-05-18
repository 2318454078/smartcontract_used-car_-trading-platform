#!/usr/bin/python3.8

# from solcx import install_solc
# install_solc(version='latest')


import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")
sys.path.insert(0,"/var/www/FlaskApp/FlaskApp")

from FlaskApp import app
application = app.server

# from FlaskApp import server as application
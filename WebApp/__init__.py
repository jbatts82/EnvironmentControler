###############################################################################
# File Name  : __init__.py
# Date       : 08/24/2020
# Description: Package
###############################################################################

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from WebApp import routes
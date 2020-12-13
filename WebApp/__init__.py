###############################################################################
# File Name  : __init__.py
# Date       : 08/24/2020
# Description: Init the Package
#            : the package is called WebApp, the app variable is app
###############################################################################

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)


from WebApp import routes
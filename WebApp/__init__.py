###############################################################################
# File Name  : __init__.py
# Date       : 08/24/2020
# Description: Init the Package
#            : the package is called WebApp, the app variable is app
###############################################################################

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app = Flask(__name__)
#app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#from WebApp import routes, models
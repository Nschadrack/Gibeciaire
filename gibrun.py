from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

gibapp = Flask(__name__)
gibapp.config['SECRET_KEY'] = '9cfa152b3e9f74b69c93e3ac4d7cce22'
gibapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gibeciaire_database.db'

db = SQLAlchemy(gibapp)
bcrypt = Bcrypt(gibapp)
login_manager = LoginManager(gibapp)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from engroutes import *
from freroutes import *
from adminroutes import *

if __name__ == "__main__":
	gibapp.run(debug=True)
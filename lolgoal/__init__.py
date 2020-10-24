from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import engine

load_dotenv()


def create_db_engine(config):
    engine = create_engine(config.DB_URL)
    return engine


app = Flask(__name__)



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from lolgoal import routes

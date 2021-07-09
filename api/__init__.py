__version__ = '0.1.0'
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from api import models


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jqtisjfg:hNubXmAytSdPyz8ZxvA3-WJlSJvyVvJq@batyr.db.elephantsql.com/jqtisjfg"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'My first API'


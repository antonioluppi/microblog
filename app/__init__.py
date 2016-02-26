import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask_restful import Resource, Api, fields, marshal
from config import basedir
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

test_fields = {
	'sn': fields.String,
	'status': fields.Boolean,
	'test_data': fields.String,
	'test_type': fields.Integer,
	'test_begin': fields.DateTime(dt_format='iso8601'),
	'test_conclusion': fields.DateTime(dt_format='iso8601'),	
	'uri': fields.Url('teste')
}

from app import views, models




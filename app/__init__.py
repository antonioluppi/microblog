import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.restful import Api, Resource, fields, marshal
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

test_fields = {
	'sn': fields.String,
	'status': fields.Boolean,
	'test_data': fields.String,
	'test_type': fields.Integer,
	'test_begin': fields.Datetime,
	'test_conclusion': fields.Datetime,	
	'uri': fields.Url('teste')
}

class TestListAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('sn', type = str, required = True,
			help = 'Não foi dado um número de série', location = 'json')
		self.reqparse.add_argument('status', type = bool, required = True, location = 'json')
		self.reqparse.add_argument('test_type', type = int, required = True, location = 'json')
		self.reqparse.add_argument('test_data', type = str, location = 'json')
		self.reqparse.add_argument('test_begin')
		self.reqparse.add_argument('test_conclusion')
		super(TestListAPI, self).__init__()		

	def get(self):
		pass

	def put(self):
		pass

class TestAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('sn', type = str, location = 'json')
		self.reqparse.add_argument('status', type = bool, location = 'json')
		self.reqparse.add_argument('test_data', type = str, default = "", location = 'json')
		self.reqparse.add_argument('test_begin')
		self.reqparse.add_argument('test_conclusion')
		self.reqparse.add_argument('test_type')
		super(TestAPI, self).__init__()		

	def get(self,id):
		pass
	
	def put(self,id):
		test = filter(lambda t: t['id'] == test_id, testes)
		if len(teste) == 0
			abort(404)
		test = test[0]
		args = self.reqparse.parse_args()
		for k, v in argg.iteritems():
			if v != None:
				test[k] = v
		return { 'test': marshal(test, test_fields) } 
	
api.add_resource(TestListAPI, '/serverlogs/api/v0.1/testes', endpoint = 'testes')
api.add_resource(TestAPI, '/serverlogs/api/v0.1/testes/<int:id>', endpoint = 'teste')


from app import views, models



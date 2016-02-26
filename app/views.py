from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask_httpauth import HTTPBasicAuth
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User, Test
auth = HTTPBasicAuth()

api = Api(app)
users = {
	"Antonio": "v2com",
	"MCCtester": "v2com"
}

@auth.get_password
def get_password(username):
	if username in users:
		return users.get(username)
	return None

@app.route('/')
@app.route('/index')
@auth.login_required
def index():
#	return "Hellow, %s!" % auth.username()
	posts = [  # fake array of posts
		{ 
	            'author': {'nickname': 'John'}, 
	            'body': 'Beautiful day in Portland!' 
	        },
	        { 
	            'author': {'nickname': 'Susan'}, 
	            'body': 'The Avengers movie was so cool!' 
	        }
			]
	return render_template("index.html",
				title='Home',
	                        user="Usuario",
	                        posts=posts)

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
		if len(teste) == 0:
			abort(404)
		test = test[0]
		args = self.reqparse.parse_args()
		for k, v in argg.iteritems():
			if v != None:
				test[k] = v
		return { 'test': marshal(test, test_fields) } 
	
api.add_resource(TestListAPI, '/serverlogs/api/v0.1/testes', endpoint = 'testes')
api.add_resource(TestAPI, '/serverlogs/api/v0.1/testes/<int:id>', endpoint = 'teste')



"""
@app.route('/login', methods=['GET', 'POST'])

@app.before_request
def before_request():
	g.user = current_user

@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['nickname','email'])
	return render_template('login.html',
				title='Sign In',
				form=form,
				providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
	if resp.email is None or resp.email == "":
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email=resp.email).first()
	if user is None:
		nickname = resp.nickname
		if nickname is None or nickname == "":
			nickname = resp.email.split('@')[0]
		user = User(nickname=nickname, email=resp.email)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/serverlogs/api/v0.1/testes/<int:test_id>', methods = ['PUT']) # talvez mudar para POST
@auth.login_required #habilitar quando se tiver um sistema de login pronto
def update_test(test_id)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

"""

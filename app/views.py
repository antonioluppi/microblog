from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask_httpauth import HTTPBasicAuth
from flask.ext.restful import Api, Resource
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User, Test
auth = HTTPBasicAuth()


users = {
    "Antonio": "v2com",
    "MCCtester": "v2com"
}

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@auth.get_password
def get_pw(username):
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

#@app.route('/serverlogs/api/v0.1/testes/<int:test_id>', methods = ['PUT']) # talvez mudar para POST
#@auth.login_required #habilitar quando se tiver um sistema de login pronto
#def update_test(test_id):

	

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class testtype(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True)

	def __repr__(self):
		return '<Test Name %r>' % (self.name)
	
class Test(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	sn = db.Column(db.String(25), index=True)	# poderia ser um int
	test_begin = db.Column(db.DateTime)
	test_conclusion = db.Column(db.DateTime)
	status = db.Column(db.Boolean) # poderia ser um enum
	test_data = db.Column(db.String(2048))
	test_type = db.Column(db.Integer, db.ForeignKey('testtype.id'))

	def __repr__(self):
			return '<SN %r status %r TestData %r  >' % (self.sn, self.status, self.test_data)
	

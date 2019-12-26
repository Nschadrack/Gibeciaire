from gibrun import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return Admins.query.get(int(user_id))

class Admins(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(), nullable = False)
	username = db.Column(db.String(15), nullable = False, unique=True)
	password = db.Column(db.String(), nullable = False)
	date_created = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<Admins %r %r>" %(self.email, self.username)


class current_images_food(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	curee = db.Column(db.String(50))
	date_posted = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<current_images_food %r>" %(self.curee)

class current_images_food_check(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	curee = db.Column(db.String(50))
	date_posted = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<current_images_food_check %r>" %(self.curee)

class current_images_shop(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	curee = db.Column(db.String(50))
	date_posted = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<current_images_shop %r>" %(self.curee)


class current_images_shop_check(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	curee = db.Column(db.String(50))
	date_posted = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<current_images_shop_check %r>" %(self.curee)

class current_images_others(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	curee = db.Column(db.String(50))
	date_posted = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<current_images_others %r>" %(self.curee)


class current_images_others_check(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	curee = db.Column(db.String(50))
	date_posted = db.Column(db.DateTime, default = datetime.now)

	def __repr__(self):
		return "<current_images_others_check %r>" %(self.curee)


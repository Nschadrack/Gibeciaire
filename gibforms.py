from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, EqualTo, DataRequired, Length, ValidationError
from models import*


class RegisterForm(FlaskForm):

	email  = StringField('Your Email', validators = [Email(),DataRequired()])

	username = StringField('Username', validators = [Length(min=4, max=15),DataRequired()])

	password = PasswordField('Password', validators = [DataRequired()])

	confirm_password = PasswordField('Confirm Password', validators = [EqualTo('password'), DataRequired()])

	submit = SubmitField('Create Account')

	def validate_username(self, username):
		user = Admins.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("That username has been used")


class LoginForm(FlaskForm):

	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')


class UpdateForm(FlaskForm):

	imagefile = FileField('Upload Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
	submit = SubmitField('Upload')

	


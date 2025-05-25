from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, BooleanField, validators, SubmitField
from wtforms.validators import Email, DataRequired, InputRequired

class LoginForm(FlaskForm):
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), Email(message='Invalid email address'), DataRequired()])
 password = PasswordField('Password', [validators.length(min=12, message='Not long enough'), DataRequired()])
 submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
 first_name = StringField('First Name', [validators.length(min=2, max=25), DataRequired()])
 last_name = StringField('Last Name', [validators.length(min=2, max=25), DataRequired()])
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), Email(message='Invalid email address'), DataRequired()])
 password = PasswordField('Password', [validators.length(min=10), validators.EqualTo('confirm_password', message='Passwords do not match'), DataRequired()])
 confirm_password = PasswordField('Reenter Password', [validators.length(min=10), DataRequired()])
 submit = SubmitField('Submit')

class ProfileForm(FlaskForm):
 first_name = StringField('First Name', [validators.length(min=2, max=25), InputRequired()])
 last_name = StringField('Last Name', [validators.length(min=2, max=25), InputRequired()])
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), Email(message='Invalid email address'), DataRequired()])
 password = PasswordField('Password', [validators.length(min=10), validators.EqualTo('confirm_password', message='Passwords do not match'), DataRequired()])
 confirm_password = PasswordField('Reenter Password', [validators.length(min=10), validators.InputRequired()])
 submit = SubmitField('Submit')
 

class WordForm(FlaskForm):
 name = StringField('Name of Word', [validators.InputRequired()]),
 definition = StringField("Definiton of Word", [validators.InputRequired()])
 pronunciation = StringField("Word pronunciation")
 etymology = StringField("Word origin")
 usage = StringField("Usage Examples")
 image_url = StringField("Image of Word")
 audio_url = StringField("Audio Link")
 parts_of_speech = StringField("Part of Speech")
 difficulty = StringField("Difficulty Level")
 submit = SubmitField('Submit') 

 class TestForm(FlaskForm):
  name = StringField("Test name")


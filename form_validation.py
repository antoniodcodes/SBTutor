from wtforms import Form, EmailField, PasswordField, StringField, BooleanField, validators

class LoginForm(Form):
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), validators.Email(message='Invalid email address'), validators.InputRequired()])
 password = PasswordField('Password', [validators.length(min=12, message='Not long enough'), validators.InputRequired()])


class RegistrationForm(Form):
 first_name = StringField('First Name', [validators.length(min=2, max=25), validators.InputRequired()])
 last_name = StringField('Last Name', [validators.length(min=2, max=25), validators.InputRequired()])
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), validators.Email(message='Invalid email address'), validators.InputRequired()])
 password = PasswordField('Password', [validators.length(min=10), validators.EqualTo('confirm_password', message='Passwords do not match'), validators.InputRequired()])
 confirm_password = PasswordField('Reenter Password', [validators.length(min=10), validators.InputRequired()])

class ProfileForm(Form):
 first_name = StringField('First Name', [validators.length(min=2, max=25), validators.InputRequired()])
 last_name = StringField('Last Name', [validators.length(min=2, max=25), validators.InputRequired()])
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), validators.Email(message='Invalid email address'), validators.InputRequired()])
 password = PasswordField('Password', [validators.length(min=10), validators.EqualTo('confirm_password', message='Passwords do not match'), validators.InputRequired()])
 confirm_password = PasswordField('Reenter Password', [validators.length(min=10), validators.InputRequired()])
 

class WordForm(Form):
 name = StringField('Name of Word', [validators.InputRequired()]),
 definition = StringField("Definiton of Word", [validators.InputRequired()])
 pronunciation = StringField("Word pronunciation")
 etymology = StringField("Word origin")
 usage = StringField("Usage Examples")
 image_url = StringField("Image of Word")
 audio_url = StringField("Audio Link")
 parts_of_speech = StringField("Part of Speech")
 difficulty = StringField("Difficulty Level")


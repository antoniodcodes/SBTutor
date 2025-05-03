from wtforms import Form, EmailField, PasswordField, StringField, BooleanField, validators

class LoginForm(Form):
 email = EmailField('Email Address', [validators.length(min=10, max=25, message='Invalid email length'), validators.Email(message='Invalid email address'), validators.InputRequired()])
 password = PasswordField('Password', [validators.length(min=12, message='Not long enough'), validators.InputRequired()])


class RegistrationForm(Form):
 first_name = StringField('First Name:', [validators.length(min=2, max=25), validators.InputRequired()])
 last_name = StringField('Last Name:', [validators.length(min=2, max=25), validators.InputRequired()])
 email = EmailField('Email Address: ', [validators.length(min=10, max=25, message='Invalid email length'), validators.Email(message='Invalid email address'), validators.InputRequired()])
 password = PasswordField('Password: ', [validators.length(min=10), validators.EqualTo('confirm_password', message='Passwords do not match'), validators.InputRequired()])
 confirm_password = PasswordField('Reenter Password', [validators.length(min=10), validators.InputRequired()])




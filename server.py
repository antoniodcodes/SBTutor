from flask import Flask, session, flash, request, render_template, redirect, jsonify
from form_validation import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import crud
import os

app = Flask('__name__')
app.config('SQLALCHEMY_DATABASE_URI') = f"""
  postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@/{os.environ.get('DB_NAME')}?host=/cloudsl/{os.environ.get('INSTANCE_CONNECTION_NAME')}
  """

db = SQLAlchemy(app)

app['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/', methods=['GET'])
@app.route('/home')
@app.route('/index')
def get_index():
  return render_template("index.html")


@app.route('/login', methods=['GET'])
def login():
  return render_template("login.html")


@app.route('/register', methods=['GET'])
def register():
  return render_template("register.html")


@app.route("/user_dashboard", methods=['POST'])
def userdashboard():
  # Get user
  email = request.form.get("email")
  password = request.form.get("password")
  user = crud.get_user_by_email(email)
  
  #validate user and check that passwords match
  if user:
    
    return render_template("user_dashboard.html", user=user)
  else:
    flash("User not found")
    return redirect("/"), 404 


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='5051')
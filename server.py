from flask import Flask, session, flash, request, render_template, redirect, jsonify
from form_validation import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
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



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='5051')
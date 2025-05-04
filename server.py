from flask import Flask, session, flash, request, render_template
from form_validation import RegistrationForm, LoginForm
import os

app = Flask('__name__')

app['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/', methods=['GET'])
def get_index():
  return render_template("index.html")



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='5051')
from flask import Flask, session, flash, request, render_template, redirect, jsonify
from flask_bcrypt import Bcrypt
from form_validation import RegistrationForm, LoginForm
from models import db, UserSchema
import crud
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask('__name__')
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
user_schema = UserSchema()

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

@app.route('/profile', methods=['GET'])
def user_profile():
  email = session['user_email']
  user = crud.get_user_by_email(email)
  if user:
    return render_template("user_profile.html")
  else:
    return redirect("/")

@app.route("/user_dashboard", methods=['POST'])
def userdashboard():
  # Get user
  email = request.form.get("email")
  password = request.form.get("password")
  user = crud.get_user_by_email(email)
  
  #validate user and check that passwords match
  if user and bcrypt.check_password(user.hashed_password, password):
    return render_template("user_dashboard.html", user=user_schema.dump(user))
  else:
    flash("User not found")
    return redirect("/"), 404 
  
  #TODO: add as a protected route
  @app.route('/users')
  def get_all_users():
    # get current user

    # Determine if current user is an admin
    # if admin, return list of users
    # if not admin, return 403 and redirect to user dashboardm
    users = crud.get_users()
    return user_schema.dump(users)
  
  @app.route('/users', methods=['POST'])
  def create_account():
    #TDDO: get values from request form

    #TODO: check if a user with that given email already exists and give warning if user is found


    #TODO: if user not in database, add user and then redirect to user dashboard

    pass


  #TODO: add as a protected route
  @app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
  def user_details(user_id):
    user = crud.get_user_by_id(user_id)
    if user:
      if request.method == 'GET':
        return user_schema.dump(user)
      elif request.method == 'PUT':
        # get user info from form
        #TODO
        pass
      elif request.method == 'DELETE':
        crud.delete_user(user_id)
        flash("User successfully deleted")
    else:
      return jsonify(message="User not found"), 404
  


# Connect to database
def connect_to_db(app):
  app.config('SQLALCHEMY_DATABASE_URI') = f"""
  postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@/{os.environ.get('DB_NAME')}?host=/cloudsl/{os.environ.get('INSTANCE_CONNECTION_NAME')}
  """
  app.config["SQLALCHEMY_ECHO"] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.app = app
  db.init_app(app)

if __name__ == '__main__':
 
  connect_to_db(app)
  with app.app_context():
    db.create_all()
  app.run(debug=True, host='0.0.0.0', port='5051')
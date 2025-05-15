from flask import Flask, session, flash, request, render_template, redirect, jsonify
from flask_bcrypt import Bcrypt
from form_validation import RegistrationForm, LoginForm, ProfileForm
from models import db, UserSchema, TestSchema, QuestionSchema
import crud
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask('__name__')
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
user_schema = UserSchema()
test_schema = TestSchema()
question_schema = QuestionSchema()

@app.route('/', methods=['GET'])
@app.route('/home')
@app.route('/index')
def get_index():
  return render_template("index.html")


@app.route('/login', methods=['GET'])
def login():
  form = LoginForm(request.form)
  return render_template("login.html", form=form)


@app.route('/register', methods=['GET'])
def register():
  form = RegistrationForm(request.form)
  return render_template("register.html", form=form)

# @jwt_required()
@app.route('/profile', methods=['GET'])
def user_profile():
  email = session['user_email']
  user = crud.get_user_by_email(email)
  if user:
    form = ProfileForm()
    return render_template("user_profile.html", form=form, user=user)
  else:
    return redirect("/")

# @jwt_required()
@app.route("/user_dashboard", methods=['POST'])
def userdashboard():
  # Get user
  email = request.form.get("email")
  password = request.form.get("password")
  user = crud.get_user_by_email(email)
  
  #validate user and check that passwords match
  if user and bcrypt.check_password(user.hashed_password, password):
    if user.is_admin:
      return render_template('admin_dashboard.html', admin_user=user_schema.dump(user))
    return render_template("user_dashboard.html", user=user_schema.dump(user))
  else:
    flash("User not found")
    return redirect("/"), 404 

@app.route("/tests")
def tests():
  
  # get User's level
  user_level = crud.get_user_level_by_id(session['user_id'])
  test_difficulty = crud.get_tests_by_difficulty(user_level) 
  
  # get tests by difficulty level
  tests = crud.get_tests_by_difficulty(test_difficulty)
  return render_template("tests.html", tests=test_schema.dump(tests))    
  
@app.route('/study_session')
def study_session():

  return render_template('study_session.html')

@app.route('/simulation')
def simulation():
  return render_template('simulation.html')

@app.route('/games')
def games():
  render_template('games.html')

@app.route('/videos')
def videos():
  return render_template('/videos')

@app.route('/flashcards')
def flashcards():
  return render_template('flashcards.html')


  """ SB Tutor API Documentation
      calls:
      GET /api/users - Protected route - Admin call to get then entire list of users
      POST /api/users - Creates a new user
      GET /api/users/user_id - Protected route that gets a single user with user_id
      PUT /api/users/user_id - Protected route that updates a user with user_id
      DELETE /api/users/user_id = Protected route that deletes a user account with user_id

      GET /api/words - Gets all flashcard data
      GET /api/words/word_id - Gets a single word
      POST /api/words/ - Protected route that allows the admin to add a new word
      PUT /api/words/word_id - Protected route that allows the admin to update a word
      DELETE /api/words/word_id - Protected route that deletes a word

      GET /api/tests - Protected route that gets all tests
      GET /api/tests/test_id - Gets a single test
      POST /api/tests - Protected route that allows the admin to create a new test
      PUT /api/tests/test_id - Protected route that allows the admin to update a test
      DELETE /api/tests/test_id - Protected route that allows the admin to delete a test

  
  """
 
 # User API Calls
  #TODO: add as a protected route
  @jwt_required()
  @app.route('/api/users')
  def get_all_users():
    # get current user

    # Determine if current user is an admin
    # if admin, return list of users
    # if not admin, return 403 and redirect to user dashboardm
    users = crud.get_users()
    return user_schema.dump(users)
  
  @app.route('/api/users', methods=['POST'])
  def create_account():
    #TDDO: get values from request form

    #TODO: check if a user with that given email already exists and give warning if user is found


    #TODO: if user not in database, add user and then redirect to user dashboard

    pass


  #TODO: add as a protected route
  # @jwt_required()
  @app.route("/api/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
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
  

# Words API Calls




# Tests API Calls





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
from flask_sqlalchemy import SqlAlchemy
from flask_marshmallow import Marshmallow
from server import app

db = SqlAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):

  __tablename__ = "users"

  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), unique=True, nullable=False)
  hashed_password = db.Column(db.String(128), nullable=False)
  level = db.Column(db.String(10), nullable=False, default='Novice')
  state = db.Column(db.String(2))
  country = db.Column(db.String(20))
  _created_at = db.Column(db.DateTime)
  imageUrl = db.Column(db.Text, nullable=True, default='default.png')

  #TODO: Add relationships


class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User

class Test(db.Model):
  __tablename__ = "tests"
  #TODO: add fields
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  test_name = db.Column(db.String(50), nullable=False)
  test_description = db.Column(db.Text, nullable=False)
  difficulty = db.Column(db.Integer, nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)

  #TODO: add relationships


class TestSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Test

class TestQuestion(db.Model):
  __tablename__ = "testquestion"
  test_id = db.Column(db.Integer, db.ForeignKey('test.id'), primary_key=True)
  question_id = db.Column(db.Integer, db.ForeignKey('questionbank.id'), primary_key=True)
    
class Question(db.Model):
  __tablename__ = "questionbank"
  #TODO: add fields
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.Integer, db.ForeignKey('questiontype.id'), nullable=False)
  question_prompt =db.Column(db.Text, nullable=False)
  correct_aswer = db.Column(db.Text, nullable=False)


  #TODO: add relationships


class QuestionSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Question

class QuestionType(db.Model):
  __table_name__ = 'questiontype'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)

  #TODO: add relationships


  class Scoreboard(db.Model):
    __tablename__ = "scoreboard"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    round_completed = db.Column(db.Integer, nullable=False)  
    highest_score = db.Column(db.Integer, nullable=False)
    
    #TODO: add relationships
    user = db.relationship('User', back_populates='scoreboard')

class ScoreboardSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Scoreboard
  
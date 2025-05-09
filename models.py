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
  state = db.Column(db.String(2))
  country = db.Column(db.String(20))
  _created_at = db.Column(db.DateTime)

  #TODO: Add relationships


class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User

class Test(db.Model):
  __tablename__ = "tests"
  #TODO: add fields




  #TODO: add relationships


class TestSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Test

    
    

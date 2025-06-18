from extensions import db
from datetime import datetime

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
  _created_at = db.Column(db.DateTime, default=datetime.now)
  imageUrl = db.Column(db.Text, nullable=True, default='default.png')

  scores = db.relationship('TestScore', back_populates='user')

  def __repr__(self):
    return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name} email={self.email} level={self.level} state={self.state} country={self.country} _created_at={self._created_at} imageUrl={self.imageUrl}>"


class Test(db.Model):
  __tablename__ = "tests"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  test_name = db.Column(db.String(50), nullable=False)
  test_description = db.Column(db.Text, nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)

  #TODO: add relationships
  scores = db.relationship('TestScore', back_populates='test')

  def __repr__(self):
    return f"<Test test_name={self.test_name} test_description={self.test_description} difficulty={self.difficulty} date_created={self.date_created}>"
9
    
class TestScore(db.Model):
  __tablename__ = "testscores"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  score = db.Column(db.Integer, nullable=False, default=0)
  timestamp = db.Column(db.DateTime, nullable=False, default=datetime)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  test_id = db.Column(db.Integer, db.ForeignKey('tests.id'), nullable=False)

  user = db.relationship('User', back_populates='scores')
  test = db.relationship('Test', back_populates='scores')

  def __repr__(self):
    return f"<TestScore score={self.score} timestamp={self.timestamp} user_id={self.user_id} test_id={self.test_id}>"


class Question(db.Model):
  __tablename__ = "questionbank"
 
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.Integer, db.ForeignKey('questiontype.id'), nullable=False)
  question_prompt =db.Column(db.Text, nullable=False)
  correct_answer = db.Column(db.Text, nullable=False)


  #TODO: add relationships
  

  def __repr__(self):
    return f"<Question question_prompt={self.question_prompt} correct_answer={self.correct_answer}>"

class QuestionType(db.Model):
  __tablename__ = 'questiontype'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
 
  def __repr__(self):
    return f"<QuestionType name={self.name}>"


class TestQuestion(db.Model):
  __tablename__ = "testquestion"
  test_id = db.Column(db.Integer, db.ForeignKey('tests.id'), primary_key=True)
  question_id = db.Column(db.Integer, db.ForeignKey('questionbank.id'), primary_key=True)
  

  def __repr__(self):
    return f"<TestQuestion test_id={self.test_id} question_id={self.question_id}>"
  

class Word(db.Model):
  __tablename__ = "words"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
  name = db.Column(db.String(30), nullable=False)
  definition = db.Column(db.Text, nullable=False)
  image_url = db.Column(db.Text, nullable=False, default='/default.png')
  audio_url = db.Column(db.Text, nullable=False, default='/default.mp3')
  pronunciation = db.Column(db.String(20), nullable=False)
  etymology = db.Column(db.Text, nullable=False)
  parts_of_speech = db.Column(db.String(20), nullable=False)
  difficulty_level = db.Column(db.Integer, nullable=False)
  usage = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f"<Word {self.name} {self.definition} {self.difficulty_level}>'"





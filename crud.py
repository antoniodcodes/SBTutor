from extensions import db
from models import User, Test, Word, TestScore


def get_user_by_email(email):
  return db.session.query(User).filter(User.email == email).first()

def get_user_by_id(id: int):
  return db.session.query(User).filter(User.id == id).first()

def get_user_level_by_id(id: int):
  user = get_user_by_id(id)
  return user.level

def get_user_level(user: User):
  return user.level

def get_users():
  return db.session.query(User).all()

def add_user(user: User):
  db.session.add(user)
  db.commit()

def update_user(id, user_object: User):
  pass

def delete_user(id):
  user = get_user_by_id(id)
  return db.session.delete(user)

def get_tests():
  return db.session.query(Test).all()

def get_tests_by_difficulty(user_level: str):
  level = 0
  if user_level == 'Novice':
    level = 1
  elif user_level == 'Apprentice':
    level = 2
  elif user_level == 'Master':
    level = 3
  return db.session.query(Test).filter(Test.difficulty == level).all()
  
def get_tests_by_id(id):
  return db.session.query(Test).filter(Test.id == id).first()

def add_test(test: Test):
  db.session.add(test)
  db.session.commit()

def update_test(id, updated_test: Test):
  test = get_tests_by_id(id)
  if test:
    test.test_name = updated_test.test_name
    test.test_description = updated_test.test_description
    test.difficulty = updated_test.difficulty
    db.session.commit()
  else:
    return None

def delete_test(id):
  test = get_tests_by_id(id)
  if test:
    db.session.delete(test)
    db.session.commit()
  else:
    return None


def add_word(word: Word):  
  db.session.add(word)
  db.session.commit()
  return word

def get_word_by_id(id: int):
  return db.session.query(Word).filter(Word.id == id).first()

def get_words_by_difficulty(difficulty_level: int):
    return db.session.query(Word).filter(Word.difficulty_level == difficulty_level).all()

def get_words():
  return db.session.query(Word).all()

def update_word(id: int, updated_word: Word):
  word = get_word_by_id(id)
  if word:
    word.name = updated_word.name
    word.definition = updated_word.definition
    word.difficulty_level = updated_word.difficulty_level
    word.imageUrl = updated_word.imageUrl
    word.audioUrl = updated_word.audioUrl
    word.difficulty_level = updated_word.level
    word.etymology = updated_word.etymology
    word.proununciation = updated_word.pronunciation
    word.parts_of_speech = updated_word.parts_of_speech
    db.session.commit()
  else: 
    return None

def delete_word(id: int):
  word = get_word_by_id(id)
  if word:
    db.session.delete(word)
    db.session.commit()
  else:
    return None
  
def get_user_scoreboard(id: int):
  pass

def get_master_scoreboard():
  pass


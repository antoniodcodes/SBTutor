from models import db, User, Test


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
  pass

def update_test(test: Test):
  pass

def delete_test(id):
  pass
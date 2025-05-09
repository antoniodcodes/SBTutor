from models import db, User, Test


def get_user_by_email(email):
  return db.session.query(User).filter(User.email == email).first()

def get_user_by_id(id: int):
  return db.session.query(User).filter(User.id == id).first()

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
  pass

def get_tests_by_difficulty():
  pass
def get_tests_by_id(id):
  pass

def add_test(test):
  pass

def update_test(test):
  pass

def delete_test(test):
  pass
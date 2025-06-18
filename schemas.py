from extensions import ma
from models import User, Test, Question, Word

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User

class TestSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Test

class QuestionSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Question

class WordSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Word


# Schema declarations
user_schema = UserSchema()
users_schema = UserSchema(many=True)
test_schema = TestSchema()
tests_schema = TestSchema(many=True)
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
word_schema = WordSchema()
words_schema = WordSchema(many=True)
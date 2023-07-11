from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
# Таблица пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    phone_number = db.Column(db.String, unique = True)
    reg_date = db.Column(db.DateTime, default = datetime.now())

# Таблица вопросов
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    level = db.Column(db.String, default = 'Easy')
    main_question = db.Column(db.String, nullable = False, unique = True)
    answer_1 = db.Column(db.String, nullable = False)
    answer_2 = db.Column(db.String, nullable = False)
    answer_3 = db.Column(db.String, nullable = True)
    answer_4 = db.Column(db.String, nullable = True)
    correct_answer = db.Column(db.Integer, nullable = False)
    timer = db.Column(db.Integer, nullable = False)

# Таблица результатов/лидеров
class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    user_answer = db.Column(db.String, nullable = False)
    correctness = db.Column(db.Boolean, default = True)
    level = db.Column(db.String)
    answer_time = db.Column(db.DateTime)

    user_fk = db.relationship((User))
    question_fk = db.relationship(Question)

class Raiting(db.Model):
    __tablename__ = 'ratings'
    id= db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_correct_answers = db.Column(db.Integer, default = 0)
    level = db.Column(db.String)

    user_fk = db.relationship(User)
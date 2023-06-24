import random

from DATABASE.models import Question, db

# Получить вопросы
def get_questions_db(level):
    # Если уровень не указан
    if level == 'all':
        questions = []
        all_questions = Question.query.all()
        for i in range(20):
            questions.append(random.choice(all_questions))
        return questions
    # если указал сложность, то включаем фильтр по сложности в вопросах
    questions_from_level = Question.query.filter_by(level=level).all()
    questions = [random.choice(questions_from_level) for i in range(20)]
    return questions

# Проверка ответа пользователя
def check_user_answer_db(question_id, user_answer):
    current_question = Question.query.get(question_id)
    # Проверка ответа пользователя с реальным ответом в ДБ
    if current_question.correct_answer == user_answer:
        return True
    return False

# Добавление вопросов базу (домашняя работа)!!!!!!!!!!
def add_questions_db(level, main_question, answer1, answer2, answer3, answer4, current_answer, timer):
    new_question = Question(level = level, main_question=main_question, answer1=answer1, answer2=answer2,
                            answer3=answer3, answer4=answer4, current_answer=current_answer, timer=timer)
    db.session.add(new_question)
    db.session.commit()
    return new_question.id

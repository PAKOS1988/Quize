from DATABASE.models import Result, db, Raiting

# Получить рейтинг пользователей
def get_raiting_db(level):
    user_position = Raiting.query.order_by(Raiting.user_correct_answer.desc()).filter_by(level=level)
    user_ids = [{i.user_id : i.user_correct_answers} for i in user_position]
    return user_ids[:5]

# Добавление ответов пользователя
def add_user_answer_db(user_id, user_answer, correctness, level):
    user_answer = Result(user_id=user_id, user_answer=user_answer, correctness=correctness, level=level)
    db.session.add(user_answer)
    db.session.commit()


#Добавление в рейтинг
def add_user_raiting_db(user_id, correct_answers, level):
    #Проверка, есть ли пользователь в таблице
    user_raiting = Raiting.query.filter_by(user_id=user_id, level=level).first()
    if user_raiting:
        user_raiting.user_correct_answer += correct_answers
    else:
        user_raiting = Raiting(user_id=user_id, level=level, user_correct_answer=correct_answers)
        db.session.add(user_raiting)
    db.session.commit()

#Получение позиции пользователя в топе
def get_user_position(user_id, level, correct_answer):
    register_user_rating = add_user_raiting_db(user_id,correct_answer,level)
    user_position = Raiting.query.order_by(Raiting.user_correct_answer.desc()).filter_by(level=level)
    user_ids = [i.user_id for i in user_position]
    return user_ids.index(user_id)+1


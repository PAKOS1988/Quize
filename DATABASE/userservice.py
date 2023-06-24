from DATABASE.models import User, db

# Регистрация пользователя
def register_user_db(name, phone_number):
    cheker = check_user_db(phone_number)
    if cheker:
        return cheker
    new_user = User(name = name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id

# Проверка
def check_user_db(phone_number):
    cheker = User.query.filter_by(phone_number=phone_number).first()
    if cheker:
        return True
    return False

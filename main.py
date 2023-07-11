from flask import Flask
from DATABASE.models import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Задать конфигурации для базы данных
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///quiz.db'

# СОздаем приложение
db.init_app(app)
from API import leaders, registration, test_process
#Регистрация компонентов
app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registartion_bp)
app.register_blueprint(test_process.test_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

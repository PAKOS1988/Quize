from flask import Blueprint
from typing import Dict, List
from DATABASE.userservice import register_user_db

registartion_bp = Blueprint('registration', __name__)

# Запрос на регистрацию
@registartion_bp.route('/register/<string:name>/<int:number>', methods=['post'])
def register_user(name:str, number:int)-> Dict[str,int]:
    user_id = register_user_db(name, number)
    return {'status':1, 'user_id':user_id}
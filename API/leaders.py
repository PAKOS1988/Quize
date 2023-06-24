from flask import Blueprint
from typing import Dict, List
from DATABASE.stateservice import get_raiting_db
leaders_bp = Blueprint('leaders', __name__)

#Запрос на получение списков лидеров
@leaders_bp.route('/leaders/<string:level>', methods=['GET'])
def get_top_5_leaders(level:str = 'all')->Dict[str, List[Dict[int,int]]]:
    top_5_users = get_raiting_db(level)
    return {'level':level, 'leaders':top_5_users}

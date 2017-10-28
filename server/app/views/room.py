from flask import Blueprint, jsonify, make_response
from flask_login import current_user, login_required
from app.models import ChatLog, Room, User

bp = Blueprint('room', __name__, url_prefix='/room')


@bp.route('/')
@login_required
def room_list():
    user: User = current_user
    result = []
    for room in user.rooms:
        last_log: ChatLog = room.last_log
        result.append({
            'id': room.id,
            'users': [u.nickname for u in room.users],
            'last_log': last_log and last_log.message,
            'last_log_at': room.last_log_at.timestamp(),
        })
    result.sort(key=lambda d: -d['last_log_at'])
    return jsonify(result)
from flask import Blueprint, jsonify, make_response, request
from flask_jwt import jwt_required, current_identity

from app.models import ChatLog, Room, User
from app.utils import make_room


bp = Blueprint('room', __name__, url_prefix='/room')


@bp.route('/')
@jwt_required()
def room_list():
    result = []
    for room in current_identity.rooms:
        last_log: ChatLog = room.last_log
        result.append({
            'id': room.id,
            'users': [u.nickname for u in room.users],
            'last_log': last_log and last_log.message,
            'last_log_at': room.last_log_at.timestamp(),
        })
    result.sort(key=lambda d: -d['last_log_at'])
    return jsonify(result)


@bp.route('/make', methods=['POST'])
@jwt_required()
def _make_room():
    usernames = list(set(u for u in request.form.getlist('usernames') if u != current_identity.username))
    if len(usernames) <= 0:
        return make_response(jsonify(), 400)

    users = User.query.filter(User.username.in_(usernames)).all()
    if len(usernames) != len(users) or len(users) <= 0:
        return make_response(jsonify(), 400)  # TODO

    for room in current_identity.rooms:
        room_usernames = [u.username for u in room.users if u != current_identity]
        if set(usernames) == set(room_usernames):
            return make_response(jsonify({
                'room_id': room.id,
            }), 301)

    try:
        room = make_room(current_identity, *users)
    except:
        return make_response(jsonify(), 500)  # TODO

    #  TODO: send signal to invited users(or not?)

    return make_response(jsonify({
        'room_id': room.id,
        'users': [u.nickname for u in room.users],
        'created_at': room.last_log_at,
    }), 200)
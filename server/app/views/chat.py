import asyncio
import json
from typing import List

from flask import request
from flask_jwt import current_identity
from flask_socketio import emit, send, Namespace, SocketIO

from app.utils import ChatLog, User
from app.utils import authenticated_only, add_chat


socketio = SocketIO()


class Socket:
    def __init__(self, sid, user_id, rooms):
        self.sid = sid
        self.connected = True
        self.user_id = user_id
        self.rooms = rooms
    
    def emit(self, event, data):
        socketio.emit(event, data, room=self.sid)

    def on_receive_message(self, room_id: int, writer: User, chat: ChatLog):
        self.emit('receive_message', json.dumps({
            'room_id': room_id,
            'writer': {
                'username': writer.username,
                'nickname': writer.nickname,
            },
            'message': chat.message,
            'created_at': chat.created_at.timestamp(),
        }))


sockets: List[Socket] = []


class ChatNamespace(Namespace):
    @authenticated_only
    def on_connect(self):
        if len([s for s in sockets if s.sid == request.sid]) == 0:
            sockets.append(
                Socket(request.sid, current_identity.id, current_identity.room_ids)
            )

    def on_disconnect(self):
        global sockets
        sockets = [s for s in sockets if s.sid != request.sid]

    @authenticated_only
    def on_send_message(self, msg):
        try:
            data = json.loads(msg)
        except:
            data = msg
        room_id, message = int(data['room_id']), data['message']
        try:
            chat = add_chat(current_identity, room_id, message)
        except:
            send(json.dumps({'succeed': False}), json=True)
            return

        send(json.dumps({'succeed': True}), json=True)

        [socket.on_receive_message(room_id, current_identity, chat) for socket in sockets]


socketio.on_namespace(ChatNamespace('/chat'))
import json

from flask import session

from app import create_app
from app.utils import create_user, make_room
from app.views.chat import socketio
from tests import  ServerTestCase


class ChatTestCase(ServerTestCase):

    def populate_db(self):
        with self.app.app_context():
            user1 = create_user('user1', 'pass1', 'nick1')
            user2 = create_user('user2', 'pass2', 'nick2')
            user3 = create_user('user3', 'pass3', 'nick3')
            make_room(user1, user2)
            make_room(user1, user2, user3)
            make_room(user2, user3)

    def setUp(self):
        super().setUp()
        self.populate_db()

    def login(self, username, password):
        rv = self.test_app.post('/user/login', data=json.dumps({
            'username': username,
            'password': password,
        }), content_type='application/json')
        return json.loads(rv.data)['access_token']

    def test_add_chat(self):
        token1 = self.login('user1', 'pass1')
        token2 = self.login('user2', 'pass2')
        token3 = self.login('user3', 'pass3')
        client1 = socketio.test_client(self.app, namespace='/chat', query_string='token=' + token1)
        client2 = socketio.test_client(self.app, namespace='/chat', query_string='token=' + token2)
        client3 = socketio.test_client(self.app, namespace='/chat', query_string='token=' + token3)

        client1.get_received('/chat')
        client1.emit('send_message', {'room_id': 1, 'message': 'message1'}, namespace='/chat')
        received = client2.get_received('/chat')
        assert len(received) == 1
        assert received[0]['args'][0]['room_id'] == 1
        assert received[0]['args'][0]['writer']['username'] == 'user1'
        assert received[0]['args'][0]['writer']['nickname'] == 'nick1'
        assert received[0]['args'][0]['message'] == 'message1'
        assert received[0]['args'][0].get('created_at') is not None

        assert len(client3.get_received('/chat')) == 0
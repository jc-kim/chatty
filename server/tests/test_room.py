import json

from app.utils import add_chat, create_user, make_room
from tests import ServerTestCase


class RoomTest(ServerTestCase):

    def populate_db(self):
        with self.app.app_context():
            self.user1 = create_user('user1', 'pass1', 'user1')
            self.user2 = create_user('user2', 'pass2', 'user2')
            self.user3 = create_user('user3', 'pass3', 'user3')
            self.user4 = create_user('user4', 'pass4', 'user4')
            self.room1_id = make_room(self.user1, self.user2).id
            self.room2_id = make_room(self.user1, self.user3).id
            self.room3_id = make_room(self.user2, self.user3).id
            self.room4_id = make_room(self.user3, self.user4).id
            add_chat(self.user1, self.room1_id, 'message1')
            add_chat(self.user1, self.room1_id, 'message2')
            add_chat(self.user2, self.room1_id, 'message3')
            add_chat(self.user3, self.room2_id, 'message4')

    def login(self, client, username, password):
        rv = client.post('/user/login', data=json.dumps({
            'username': username,
            'password': password,
        }), content_type='application/json')
        return json.loads(rv.data)['access_token']

    def setUp(self):
        super().setUp()
        self.populate_db()

    def get(self, test_app, url, token=None):
        return test_app.get(url, headers={'authorization': 'JWT ' + token} if token else None)

    def post(self, test_app, url, data, token=None):
        return test_app.post(url, data=data, headers={'authorization': 'JWT ' + token} if token else None)

    def test_room_list(self):
        token = self.login(self.test_app, 'user3', 'pass3')
        rv = json.loads(self.get(self.test_app, '/room/', token).data)
        assert len(rv) == 3
        assert rv[0]['id'] == self.room2_id
        assert rv[0]['users'] == ['user1', 'user3']
        assert rv[1]['id'] == self.room4_id
        assert rv[1]['users'] == ['user3', 'user4']

    def test_failed_room_list(self):
        rv = self.test_app.get('/room/')
        assert rv.status_code == 401

    def test_make_room(self):
        token = self.login(self.test_app, 'user1', 'pass1')
        rv = self.post(self.test_app, '/room/make', {
            'usernames': ['user2', 'user3', 'user4'],
        }, token)
        assert rv.status_code == 200
        d = json.loads(rv.data)
        assert d['room_id'] == 5
        assert d['users'] == ['user1', 'user2', 'user3', 'user4']

        rv = json.loads(self.get(self.test_app, '/room/', token).data)
        assert len(rv) == 3
        assert rv[0]['id'] == 5

    def test_redirect_make_room(self):
        token = self.login(self.test_app, 'user1', 'pass1')
        rv = self.post(self.test_app, '/room/make', {
            'usernames': ['user2'],
        }, token)
        assert rv.status_code == 301
        assert json.loads(rv.data)['room_id'] == 1

    def test_failed_make_room(self):
        token = self.login(self.test_app, 'user1', 'pass1')
        rv = self.post(self.test_app, '/room/make', {
            'usernames': ['user1'],
        }, token)
        assert rv.status_code == 400  # TODO: Do I need to implement feature chat with myself?
        
        rv = self.post(self.test_app, '/room/make', {
            'usernames': []
        }, token)
        assert rv.status_code == 400
    
    def test_get_chat_log(self):
        token = self.login(self.test_app, 'user1', 'pass1')
        rv = self.get(self.test_app, f'/room/{self.room1_id}/logs', token)
        assert rv.status_code == 200
        assert len(json.loads(rv.data)) == 3
        assert json.loads(rv.data)[0]['message'] == 'message3'
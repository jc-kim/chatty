import json

from app.utils import create_user, make_room
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

    def login(self, client, username, password):
        client.post('/user/login', data={
            'username': username,
            'password': password,
        })

    def setUp(self):
        super().setUp()
        self.populate_db()

    def test_room_list(self):
        self.login(self.test_app, 'user3', 'pass3')
        rv = json.loads(self.test_app.get('/room/').data)
        assert len(rv) == 3
        assert rv[0]['id'] == self.room4_id
        assert rv[0]['users'] == ['user3', 'user4']
        assert rv[1]['id'] == self.room3_id
        assert rv[1]['users'] == ['user2', 'user3']

    def test_failed_room_list(self):
        rv = self.test_app.get('/room/')
        assert rv.status_code == 401

    def test_make_room(self):
        self.login(self.test_app, 'user1', 'pass1')
        rv = self.test_app.post('/room/make', data={
            'usernames': ['user2', 'user3', 'user4'],
        })
        assert rv.status_code == 200
        d = json.loads(rv.data)
        assert d['room_id'] == 5
        assert d['users'] == ['user1', 'user2', 'user3', 'user4']

        rv = json.loads(self.test_app.get('/room/').data)
        assert len(rv) == 3
        assert rv[0]['id'] == 5

    def test_redirect_make_room(self):
        self.login(self.test_app, 'user1', 'pass1')
        rv = self.test_app.post('/room/make', data={
            'usernames': ['user2'],
        })
        assert rv.status_code == 301
        assert json.loads(rv.data)['room_id'] == 1

    def test_failed_make_room(self):
        self.login(self.test_app, 'user1', 'pass1')
        rv = self.test_app.post('/room/make', data={
            'usernames': ['user1'],
        })
        assert rv.status_code == 400  # TODO: Do I need to implement feature chat with myself?
        
        rv = self.test_app.post('/room/make', data={
            'usernames': []
        })
        assert rv.status_code == 400
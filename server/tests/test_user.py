import json

from app.utils import create_user
from tests import ServerTestCase


class UserTest(ServerTestCase):
    
    def test_succeed_register(self):
        rv = self.test_app.post('/user/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })
        assert rv.status_code == 200

    def test_failed_register(self):
        self.test_app.post('/user/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })

        rv = self.test_app.post('/user/register', data={
            'username': '',
            'password': '',
            'nickname': '',
        })
        assert rv.status_code == 400

        rv = self.test_app.post('/user/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })
        assert rv.status_code == 400
        rv = self.test_app.post('/user/register', data={
            'username': 'user2',
            'password': 'pass2',
        })
        assert rv.status_code == 400

    def test_succeed_login(self):
        self.test_app.post('/user/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })

        rv = self.test_app.post('/user/login', data={
            'username': 'user1',
            'password': 'pass1',
        })
        rv.status_code == 200
    
    def test_failed_login(self):
        self.test_app.post('/user/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })

        rv = self.test_app.post('/user/login', data={
            'username': 'user1',
            'password': 'pass2',
        })
        assert rv.status_code == 400
    
    def test_logout(self):
        self.test_app.post('/user/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })
        rv = self.test_app.post('/user/logout')
        assert rv.status_code == 200
        rv = self.test_app.post('/user/logout')
        assert rv.status_code == 200
    
    def test_user_list(self):
        with self.app.app_context():
            create_user('user1', 'pass1', 'nick1')
            create_user('user2', 'pass2', 'nick2')
            create_user('user3', 'pass3', 'nick3')

        self.test_app.post('/user/login', data={
            'username': 'user1',
            'password': 'pass1',
        })
        rv = self.test_app.get('/user/list')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert len(data) == 2
        assert set([u['username'] for u in data]) == set(['user2', 'user3'])

        self.test_app.post('/user/login', data={
            'username': 'user2',
            'password': 'pass2',
        })
        rv = self.test_app.get('/user/list')
        assert set([u['username'] for u in json.loads(rv.data)]) == set(['user1', 'user3'])
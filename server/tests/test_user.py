from tests import ServerTestCase


class UserTest(ServerTestCase):
    
    def test_succeed_register(self):
        rv = self.test_app.post('/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })
        assert rv.status_code == 200

    def test_failed_register(self):
        self.test_app.post('/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })

        rv = self.test_app.post('/register', data={
            'username': '',
            'password': '',
            'nickname': '',
        })
        assert rv.status_code == 400

        rv = self.test_app.post('/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })
        assert rv.status_code == 400
        rv = self.test_app.post('/register', data={
            'username': 'user2',
            'password': 'pass2',
        })
        assert rv.status_code == 400

    def test_succeed_login(self):
        self.test_app.post('/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })

        rv = self.test_app.post('/login', data={
            'username': 'user1',
            'password': 'pass1',
        })
        rv.status_code == 200
    
    def test_failed_login(self):
        self.test_app.post('/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })

        rv = self.test_app.post('/login', data={
            'username': 'user1',
            'password': 'pass2',
        })
        assert rv.status_code == 400
    
    def test_logout(self):
        self.test_app.post('/register', data={
            'username': 'user1',
            'password': 'pass1',
            'nickname': 'nick1',
        })
        rv = self.test_app.post('/logout')
        assert rv.status_code == 200
        rv = self.test_app.post('/logout')
        assert rv.status_code == 200
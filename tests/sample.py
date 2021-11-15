from flask import url_for
from flask_testing import TestCase
from flask_login import current_user
from application import app, db
from application.models import Users, Tasks
    
    # def test_new_task(self):
    #     response = self.client.post(url_for('new_task'),
    #     data = dict(title='Write Song', content='I need to write a song about a girl named Billie Jean'),
    #     follow_redirects = True
    #     )


    def test_login(self):
        response = self.client.post(url_for('login'),
        data = dict(username='HeeHee', password='thriller'),
        follow_redirects = True
        )


    def test_logout(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Seiri', response.data)




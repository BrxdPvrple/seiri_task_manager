from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Users, Tasks

# =========== 12 TEST CASES NEEDED ============


class TestBase(TestCase):
    
    # Creates config for testing
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False,
            LOGIN_DISABLED=True
        )
        return app


    # Creates tables and inserts test data
    def setUp(self):

        db.create_all()

        sample_user = Users(first_name='John', surname='Smith', username='SmithyBoy', email='jsmith@email.com', password='testpassword1')
        sample_task = Tasks(title='School Run', content='We need to drop the kids off at school today at 8am.')

        db.session.add(sample_user, sample_task)
        db.session.commit()


    # Deletes tables 
    def tearDown(self):

        db.session.remove()
        db.drop_all()



class TestViews(TestBase):
     
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Seiri', response.data)


    # def test_load_user(self):
        # pass
  

    
    def test_signup(self):
        response = self.client.post(url_for('signup'),
        data = dict(first_name='Michael', surname='Jackson', username='HeeHee', email='kingofpop@email.com', password='thriller'),
        follow_redirects = True
        )



   

    def test_login(self):
        response = self.client.post(url_for('login'),
        data = dict(username='HeeHee', password='thriller'),
        follow_redirects = True
        )
    




    def test_dashboard_get(self):
        response = self.client.get(url_for('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Head to the tasks tab', response.data)





    def test_logout(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Seiri', response.data)





    def test_show_tasks(self):
        response = self.client.get(url_for('show_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task Management Hub', response.data)





    def test_new_task(self):
        response = self.client.post(url_for('new_task'),
        data = dict(title='Write Song', content='I need to write a song about a girl named Billie Jean'),
        follow_redirects = True
        )



  

    def test_edit_task(self):
        response = self.client.post(url_for('edit_task'),
        data = dict(title='Change Song', content='The song is now called Do You Remember The Time'),
        follow_redirects = True
        )
    
   


    
    def test_delete_task(self):
        with self.client:
            response = self.client.delete(url_for('delete_task'),
            data = dict(title='School Run', content='We need to drop the kids off at school today at 8am.'),
            follow_redirects = True
            )

        assert len(Tasks.query.all()) == 0



    def test_account(self):
        response = self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Coming Soon...', response.data)


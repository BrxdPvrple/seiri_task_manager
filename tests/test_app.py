from flask_testing import TestCase


# =========== 12 TEST CASES NEEDED ============


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests

    def setUp(self):
        # Will be called before every test

    def tearDown(self):
        # Will be called after every test
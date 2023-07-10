"""
BaseTest class

This class should be the parent class for each non-unit test.
It allows for instantiation of the database dynamically and
makes sure that it is a new blank database each time.

"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self) -> None:
        # Make sure database exist
        # this will make an empty db file
        app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'
        # context manager - loads all app variable, app confic and pretens that
        # we have the real db
        with app.app_context():
            # let's initialize db with our app and initialize all the tables
            db.init_app(app)
            db.create_all()

        # Get a test client
        self.app = app.test_client()  # giving a test client of the app
        self.app_context = app.app_context  # allowing us to access to app contest later on our test
        # context is going to load everything that is imported for the app

    def tearDown(self) -> None:
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()

import unittest
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Frame, BOTH
import time as tm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, UserModel
from tracker import Application
import factory
import pytest

# Connect to the database and create the schema within a transaction
def setup_module():
    global transaction, connection, engine
    engine = create_engine('sqlite:///user_info_db.db')
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(connection)

#pytest fixture for database connection
@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close

#pytest fixture for database transaction, session yield, and session close
@pytest.fixture(scope='function')
def session(connection):
    transaction = connection.begin()
    UserFactory.meta.sqlalchemy_session = session
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()

# Roll back the top level transaction and disconnect from the database
def teardown_module():
    transaction.rollback()
    connection.close()
    engine.dispose()

# Test a database session
def test_a_transaction(db_session):
   row = db_session.query(Table).get(1) 
   row.name = 'testing'

   db_session.add(row)
   db_session.commit()

# Confirm session does not persist beyond body of the test
def test_transaction_doesnt_persist(db_session):
   row = db_session.query(Table).get(1) 
   assert row.name != 'testing'

#Test to make sure the application opens correctly
class applicationTest(unittest.TestCase):
    
    def testOpenApp(self):
        app = Application(master=None)
        self.assertIsInstance(app, Application)

#test query for every single instance expected to be found in the query
class TestQueryAlt(unittest.TestCase):


    def test_query_UserModel(self):
        expected = [
            ('Brennan', 'Luttrell', '1779 Broadway Ave', 
        'Grand Rapids', 'MI', 49504, 'luttrelb', 'testPass')
        ]
        successful = True
        # Check to make sure every expected item is in the query
        try:
            for category, platform, region in expected:
                self.session.query(UserModel).filter_by(
                        category=category, platform=platform,
                        region=region).one()
        except (NoResultFound, MultipleResultsFound):
            successful = False
        self.assertTrue(successful)
        # Check to make sure no unexpected items are in the query
        self.assertEqual(self.session.query(UserModel).count(),
                         len(expected))

class TestDatabase(unittest.TestCase):
    def setup(self):
        self.__transaction = connection.begin_nested()
        self.session = Session(connection)

    def teardown(self):
        self.session.close()
        self.__transaction.rollback()

#tests one instance of query creation to be used across all instances to be found in query
class TestQuery(unittest.TestCase):
    #Build
    def __init__(self):
        self.engine = create_engine('sqlite:///user_info_db.db')
        self.session = sessionmaker(bind=self.engine)
        self.Session = self.session()
        Base.metadata.create_all(self.engine)
        self.userModel = UserModel('Brennan', 'Luttrell', '1779 Broadway Ave', 
        'Grand Rapids', 'MI', 49504, 'luttrelb', 'testPass')
        self.Session.add(self.userModel)
        self.Session.commit()

    #Break down  
    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    #Query test that should return true if both user instances are the same element
    def test_query_User(self):
        expected = [self.userModel]
        result = self.Session.query(UserModel).all()
        self.assertEqual(result, expected)
    
    #function to add user data
    def add_user_data(self, usrnm):
        Session.query(UserModel).filter(UserModel.id).add()

    #function to delete user data
    def delete_usr_data(self, id):
        Session.query(UserModel).filter(UserModel.id).delete()

    #integration test that checks if data was deleted from database correctly
    def delete_user_test(self):
        expected = [self.userModel]
        assert Session.query(UserModel).one()
        delete_usr_data(session, expected.usrnm)
        result = Session.query(UserModel).one_or_none()
        assert result is None


# # test = TestQuery()
# # print(test.testQuery_User())
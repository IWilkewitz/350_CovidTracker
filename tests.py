import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, UserModel

class TestQuery(unittest.TestCase):

    def __init__(self):
        self.engine = create_engine('sqlite:///user_info_db.db')
        self.session = sessionmaker(bind=self.engine)
        self.Session = self.session()
        Base.metadata.create_all(self.engine)
        self.userModel = UserModel('Brennan', 'Luttrell', '1779 Broadway Ave', 
        'Grand Rapids', 'MI', 49504, 'luttrelb', 'testPass')
        self.Session.add(self.userModel)
        self.Session.commit()
        
    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_query_User(self):
        expected = [self.userModel]
        result = self.Session.query(UserModel).all()
        self.assertEqual(result, expected)

    def add_user_data(self, usrnm):
        Session.query(UserModel).filter(UserModel.id).add()


    def delete_usr_data(self, id):
        Session.query(UserModel).filter(UserModel.id).delete()

    def delete_user_test(self):
        expected = [self.userModel]
        assert Session.query(UserModel).one()
        delete_usr_data(session, expected.usrnm)
        result = Session.query(UserModel).one_or_none()
        assert result is None

        

test = TestQuery()
print(test.testQuery_User())
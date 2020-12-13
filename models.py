from sqlalchemy import (
        Column,
        Integer,
        String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'User_Info'

    f_name = Column(String, nullable=False)
    l_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zipCode = Column(Integer, nullable=False)
    usrnm = Column(String, nullable=False)
    pswd = Column(String, nullable=False)
    
    id = Column(Integer, primary_key=True)
    
    def __init__(self, f_name, l_name, address, city, state, zipCode, usrnm, pswd):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.usrnm = usrnm
        self.pswd = pswd
    
    def __repr__(self):
        return (
            "<UserModel('{self.f_name}', '{self.l_name}', "
            "'{self.address}', '{self.city}', '{self.state}',"
            " '{self.zipCode}', '{self.usrnm}', '{self.pswd}')>".format(self=self)
        )
from sqlalchemy import create_engine, String, ForeignKey, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///usinfo.db', echo=True)

Base = declarative_base()

#tables

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    user_id = Column(Integer)
    city = Column(String)
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"<User(firstname'{self.firstname}', lastname'{self.lastname}', age='{self.age}', city='{self.city}')>"
    

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    induser_id = Column(Integer, ForeignKey('users.user_id'))
    email = Column(String)

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address(email='{self.email}')>"

#table 3
class Lib(Base):
    __tablename__ = 'library'

    id = Column(Integer, primary_key=True)
    induser_id = Column(Integer, ForeignKey('users.user_id'))
    bookname = Column(String)
    totalamount = Column(Integer)

    user = relationship("User", back_populates="library")

def __repr__(self):
        return f"<Lib(bookname='{self.bookname}', userid='{self.userid}',totalamount='{self.totalamount}')>"
    
User.library = relationship("Lib", back_populates="user")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session = Session()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entry import User, Address, Lib


engine = create_engine('sqlite:///usinfo.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

#values to the table1

user1 = User(firstname='Alex', lastname='Ken', user_id=45895, city='Chennai')
user2 = User(firstname='Saravana', lastname='Kumar', user_id=56328, city='Tuticorin')
user3 = User(firstname='Gohula', lastname='Viji', user_id=78965, city='Tenkasi')
user4 = User(firstname='Prithvi', lastname='Shaw', user_id=12365, city='Chennai')
user5 = User(firstname='Janani', lastname='Ani', user_id=54613, city='Bangalore')
user6 = User(firstname='Arun', lastname='Kumar', user_id=30157, city='Tuticorin')

#values to the table2

address1 = Address(email='kansha25@gmail.com',  user=user1)
address2 = Address(email='sarkam@yahoo.com', user=user2)
address3 = Address(email='gohuvi256@hotmail.com', user=user3)
address4 = Address(email='shaw99@gmail.com', user=user4)
address5 = Address(email='janani302000@gmail.com', user=user5)
address6 = Address(email='arunus_90@gmail.com', user=user6)

#values to the table3

book1 = Lib(bookname='Python World', induser_id=45895, totalamount = 562, user=user1)
book2 = Lib(bookname='Html a guide', induser_id=56328, totalamount = 859,  user=user2)
book3 = Lib(bookname='Think like a Monk', induser_id=78965, totalamount = 450,  user=user3)
book4 = Lib(bookname='Quite', induser_id=12365, totalamount = 456,  user=user4)
book5 = Lib(bookname='Python World', induser_id=54613, totalamount = 896,  user=user5)
book6 = Lib(bookname='Become a Full Stack Developer', induser_id=30157, totalamount = 220,  user=user6)



session.add_all([user1, user2, user3, user4, user5, user6, address1, address2, address3, address4, address5, address6
                 , book1, book2, book3, book4, book5, book6])
session.commit()

session.close()



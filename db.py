from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, create_engine


engine = create_engine('sqlite:///books_data.sqlite', echo=True)

Base = declarative_base()


class Books(Base):
    __tablename__ = 'Books'

    book_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String())
    price = Column(Integer())
    stock_qty = Column(Integer())

    def __init__(self, name, price, stock_qty):
        self.name = name
        self.price = price
        self.stock_qty = stock_qty


Base.metadata.create_all(engine)

from sqlalchemy import Column, String, Integer, Date, DECIMAL

from .base import Base


class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    price = Column(String(50))
    date = Column(String(50))
    image = Column(String(350), nullable=False)

    def __init__(self, title, price, date, image):
        self.title = title
        self.price = price
        self.date = date
        self.image = image
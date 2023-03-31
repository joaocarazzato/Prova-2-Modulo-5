from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class Games(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    plataform = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    def __repr__(self) -> str:
        return f"\nGame(\n id = {self.id},\n name = {self.name},\n plataform = {self.plataform},\n price = {self.price},\n quantity = {self.quantity}\n)"

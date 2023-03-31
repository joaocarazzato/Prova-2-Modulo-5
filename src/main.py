from models.base import Base
from models.games import Games
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from assistant import assistantDatabase

assistantDatabase()

engine = create_engine("sqlite:///games.db", echo=True)

Base.metadata.create_all(engine)

session = Session(engine)

query = session.query(Games).all()

print(query)
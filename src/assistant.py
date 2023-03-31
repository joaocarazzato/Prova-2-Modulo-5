from models.base import Base
from models.games import Games
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def assistantDatabase():
    engine = create_engine("sqlite:///games.db", echo=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    dead_space = Games(
        name = "DEAD SPACE REMAKE",
        plataform = "PS5",
        price = 350.00,
        quantity = 10
    )
    forspoken = Games(
        name = "FORSPOKEN",
        plataform = "PC",
        price = 299.00,
        quantity = 8
    )
    dead_island = Games(
        name = "DEAD ISLAND 2",
        plataform = "PS5",
        price = 350.00,
        quantity = 10
    )
    hogwarts = Games(
        name = "HOGWARTS LEGACY",
        plataform = "PC",
        price = 219.00,
        quantity = 7
    )
    wild_hearts = Games(
        name = "WILD HEARTS",
        plataform = "Xbox Series",
        price = 350.00,
        quantity = 7
    )
    resident_evil = Games(
        name = "RESIDENT EVIL 4",
        plataform = "PS5",
        price = 289.00,
        quantity = 10
    )
    zelda = Games(
        name = "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",
        plataform = "Switch",
        price = 350.00,
        quantity = 10
    )

    session.add_all([dead_space, forspoken, dead_island, hogwarts, wild_hearts, resident_evil, zelda])

    session.commit()

if __name__ == '__main__':
    assistantDatabase()
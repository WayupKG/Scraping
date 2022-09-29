
from models.base import Base, Session, engine
from models.house import House

# сохраняет все данные в базу данных
def save(data) -> None:
    Base.metadata.create_all(engine)
    session = Session()
    for item in data:
        house = House(item[0], item[1], item[2], item[3])
        session.add(house)
    session.commit()
    session.close()
    print("\n---- Все данные сохранены на базу данных ----\n")
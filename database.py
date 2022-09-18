from sqlmodel import SQLModel,create_engine


engine = create_engine(url="sqlite:///database.db",echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)




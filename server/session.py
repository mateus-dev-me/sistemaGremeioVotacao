from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def retornaSession():
    BANCO = '../db/gremio.db'
    CONN = f'sqlite:///{BANCO}'
    engine = create_engine(CONN)
    Session = sessionmaker(bind=engine)
    return Session()
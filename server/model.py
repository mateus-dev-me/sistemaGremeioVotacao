from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BANCO = '../db/gremio.db'

CONN = f"sqlite:///{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Alunos(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    matricula = Column(String(50))
    senha = Column(String(50))
    nome = Column(String(50))

class AlunosVot(Base):
    __tablename__ = 'alunosvot'
    id = Column(Integer, primary_key=True)
    ID_aluno = Column(Integer, ForeignKey('alunos.id'))


class Chapas(Base):
    __tablename__ = 'chapas'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    ID_presidente = Column(Integer)
    ID_vice = Column(Integer)

class Votacao(Base):
    __tablename__ = 'votacao'
    id = Column(Integer, primary_key=True) 
    ID_chapa = Column(String, ForeignKey('chapas.id'))

Base.metadata.create_all(engine)
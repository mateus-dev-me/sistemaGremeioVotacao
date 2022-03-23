import sqlite3

connectDb = sqlite3.connect('./db/gremiovotacao.db')

cursor = connectDb.cursor()

cursor.execute("""
CREATE TABLE alunos (
    matricula VARCHAR,
    senha VARCHAR,
);
""")

cursor.execute("""
CREATE TABLE chapas (
    Numero INTERGER,
    President FK,
    Vice FK
)
"""
)

cursor.execute("""
CREATE TABLE votacao (
    Nome_Aluno FK,
    ID_CHAPA FK
)
""")

connectDb.commit()
connectDb.close()
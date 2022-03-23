import sqlite3

connectDb = sqlite3.connect('./db/gremiovotacao.db')

cursor = connectDb.cursor()


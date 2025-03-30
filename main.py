import sqlite3 
con = sqlite3.connect("tutorial.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
cur.execute("CREATE TABLE movie(title , year, score)")# CREATE INSERT UPDATE SELECT DELETE DROP
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

# data = cur.execute("SELECT * FROM movie ORDER BY year")

# for i in data:
#     print(i)
con.close()
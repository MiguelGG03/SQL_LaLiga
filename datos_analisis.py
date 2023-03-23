from pathlib import Path
import sqlite3
import pandas as pd

Path('tabla.db').touch()
con = sqlite3.connect('tabla.db')
cur = con.cursor()
df = pd.read_csv('datos.csv')
df.to_sql('tabla', con, if_exists='replace')

cur.execute("SELECT * FROM tabla WHERE Name='A. Remiro'")
print(cur.fetchall())

cur.execute("UPDATE tabla SET Name='Miguel Gonzalez' WHERE Name='Odriozola'")
cur.execute("UPDATE tabla SET Name='Salo Martinez' WHERE Name='Reguilón'")
con.commit()

cur.execute("DELETE FROM tabla WHERE Name='Yeray'")
con.commit()

cur.execute("INSERT INTO tabla VALUES (6, 'Athletic Club', 'Defender', 1.0, 'Yeray', 0.0, 0, '0.00%', 0, '0.00%', 0, '0.00%', 0, '0.00%', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0, 0, 0)")
con.commit()

cur.execute("""
            SELECT MIN(GamesWhereSubstituted)
            FROM tabla
            WHERE Team = 'Atlético de Madrid'
            """)
print(cur.fetchall())

cur.execute("""
            SELECT MAX(GamesWhereSubstituted)
            FROM tabla
            WHERE Team = 'Atlético de Madrid'
            """)
print(cur.fetchall())

cur.execute("""
            SELECT AVG(GamesWhereSubstituted)
            FROM tabla
            WHERE Team = 'Atlético de Madrid'
            """)
print(cur.fetchall())

cur.execute("""
            SELECT SUM(GamesWhereSubstituted)
            FROM tabla
            WHERE Team = 'Atlético de Madrid'
            """)
print(cur.fetchall())

cur.execute("""
            SELECT COUNT(GamesWhereSubstituted)
            FROM tabla  
            WHERE Team = 'Atlético de Madrid'
            """)
print(cur.fetchall())

cur.execute("SELECT * FROM tabla WHERE FullGamesPlayed BETWEEN 30 AND 100")
print(cur.fetchall())
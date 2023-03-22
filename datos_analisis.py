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

cur.execute("INSERT INTO tabla VALUES (87, 'Real Madrid', 'Goalkeeper', 1.0, 'Tupac', 0.0, 0, '0.00%', 0, '0.00%', 0, '0.00%', 0, '0.00%', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0, 0, 0)")
con.commit()

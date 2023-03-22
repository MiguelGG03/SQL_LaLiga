from pathlib import Path
import sqlite3
import pandas as pd

Path('tabla.db').touch()
con = sqlite3.connect('tabla.db')
cur = con.cursor()
df = pd.read_csv('datos.csv')
df.to_sql('tabla', con, if_exists='replace')

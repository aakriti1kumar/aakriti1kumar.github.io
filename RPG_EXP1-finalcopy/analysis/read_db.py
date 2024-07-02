import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('instance/conversations.db')
df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", cnx)
df = pd.read_sql_query("SELECT * FROM conversation", cnx)
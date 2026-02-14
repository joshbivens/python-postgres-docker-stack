import psycopg2
import os
import socket

dbname = os.getenv('POSTGRES_DB')
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')

conn = psycopg2.connect(host="db", dbname=dbname, user=user, password=password)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS greetings (id serial PRIMARY KEY, message varchar);")
cur.execute("INSERT INTO greetings (message) VALUES (%s)", (f"Hello from {socket.gethostname()}",))
conn.commit()

cur.execute("SELECT * FROM greetings;")
print(f"The database says: {cur.fetchone()}")

cur.close()
conn.close()


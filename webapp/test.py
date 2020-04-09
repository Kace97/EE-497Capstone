import sqlite3
import time
import datetime

conn = sqlite3.connect('testing.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS usernames(unix REAL, date TEXT, firstName TEXT, lastName TEXT, email TEXT)')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('&Y-%m-%d %H:%M:%S'))
    firstName = 'John'
    lastName = 'Doe'
    email = 'johndoe@gmail.com'
    c.execute("INSERT INTO usernames(unix, date, firstName, lastName, email) VALUES (?, ?, ?, ?, ?)",
              (unix, date, firstName, lastName, email)) #mySQL uses %s instead of ?
    conn.commit()

def read_from_db():
    c.execute('SELECT email FROM usernames')
    for row in c.fetchall():
        
    
c.close()
conn.close()
    


import sqlite3

connect_me = sqlite3.connect('database.db')
c = connect_me.cursor()
c.execute(""" CREATE TABLE passwords
    (website TEXT,
    username TEXT,
    password TEXT)""")
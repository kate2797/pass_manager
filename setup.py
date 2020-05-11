# setting up DB
import sqlite3
connect_me = sqlite3.connect('database.db')
print(connect_me)

# create the table
c = connect_me.cursor()
c.execute(""" CREATE TABLE passwords
<<<<<<< HEAD
<<<<<<< HEAD
    (website TEXT,
=======
    (id PRIMARY KEY,
>>>>>>> parent of 675882d... adding new files
=======
    (id PRIMARY KEY,
    website TEXT,
>>>>>>> parent of 340a262... final commit
    username TEXT,
    password TEXT)""")
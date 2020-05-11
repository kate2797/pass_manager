import sqlite3
import os 

def see_all():
    # connect to db 
    connect_to_db = sqlite3.connect('database.db')
    c = connect_to_db.cursor() 
    c.execute("SELECT * FROM passwords")
    # fetches all rows of a query result -> returns a list 
    my_table = c.fetchall()
    # show the id as well with enumerate()
    for i, row in enumerate(my_table):
        print(i, row)
    input("Press Enter to Exit")
    os.system('clear')
    connect_to_db.close()
    return 
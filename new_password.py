import sqlite3

def new_password():
    # connect to db 
    connect_to_db = sqlite3.connect('database.db')
    c = connect_to_db.cursor()  

    website = input("Enter website name: ")
    username = input("Enter your username or e-mail: ")
    password = input("Enter your password: ")

    c.execute("""INSERT INTO passwords 
        (website, username, password) VALUES
        (?, ?, ?)
        """, (website, username, password))
    connect_to_db.commit()
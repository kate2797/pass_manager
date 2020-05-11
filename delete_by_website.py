import sqlite3
import os

def delete():
    # connect to db 
    connect_to_db = sqlite3.connect('database.db')
    c = connect_to_db.cursor() 

    user_input = input("Password for which website you want to delete? ")
    print(">> WARNING <<")
    confirm = input("Whole database entry will be deleted, not just the password.\nDo you still want to continue? (y/n): ")

    if confirm == "y":
        c.execute("""DELETE FROM passwords
            WHERE website = ?
            """, (user_input,))
        connect_to_db.commit()
        connect_to_db.close()
        print("Your password was successfully deleted \n")
        input("Press Enter to Exit")
    else:
        input("Press Enter to Exit")
    return 

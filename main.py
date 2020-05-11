import sqlite3
import os 
from secrets import ADMIN_PASSWORD 
from new_password import new_password

# only 3 attempts 
attempts = 0

while attempts < 3:
    try_to_connect = input("Enter master password: ")
    if try_to_connect == ADMIN_PASSWORD:         
        print("Success")
        break 
    elif try_to_connect == "q":
        os.system('clear')
        break 
    else:
        attempts += 1
        print(f"Wrong, try again. You have {3 - attempts} attempts left.")      
# alert about the limit when it's reached
if attempts == 3:
    print("You have reached the password limit")

# now we need to create the menu for the sql connection
connect_to_db = sqlite3.connect('database.db')
c = connect_to_db.cursor()
print(connect_to_db)

while True:
    os.system('clear')
    print("Welcome to the Password Manager")
    print("COMMANDS:")
    print("s -> See all passwords")
    print("n -> Add new password")
    print("d -> Delete password")
    print("q -> Quit Password Manager")

    user_input = input("Enter a command: ")
    if user_input == "s":
        pass
    elif user_input == "n":
        new_password()
    elif user_input == "d":
        pass
    elif user_input == "q":
        break 




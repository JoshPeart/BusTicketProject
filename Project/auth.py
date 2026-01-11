# Holds all of the user login pages along with their respective menus
# The getting a number choice from a list function is also here

import sys

accounts = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "user1", "role": "customer"},
    {"username": "user2", "password": "user2", "role": "customer"},
    ]

def login():

    # Main login menu for the program.
    # Allows the user to log in, continue as a guest, or exit.
    
    print("""
======== MOBILE TICKETS ========
1. Log in
2. Continue as guest
3. Exit
""")


    # Loop until the user either logs in, continues as guest, or exits
    while True:
        
        # Use try/except to handle invalid input and prevent the program from crashing
        try:
            choice = int(input("Choose an option: "))

            if choice == 3:
                # Completley exits program
                print("\nGoodbye!")
                sys.exit()

            if choice == 2:
                # Guest users do not have a role or username
                print("\nContinuing as guest...")
                return None, None 

            elif choice == 1:
                username = input("\nEnter username: ")
                password = input("\nEnter password: ")

                
                # Check details against the stored dictionary
                for account in accounts:
                    if account["username"] == username and account["password"] == password:
                        print(f"\nLogin successful! Logged in as: {username}\n")
                        return account["role"], username

                print("\nInvalid username or password. Try again.\n")

            else:
                print("\nPlease enter 1 or 2.")

        except ValueError:
            print("\nInvalid input. Please enter a number.")

def userMenu():

    # User options
    
    print("""
======== USER MENU ========
1. View purchased tickets
2. Purchase a ticket
3. Log out
""")

def adminMenu():

    # Admin options
    
    print("""
======== ADMIN MENU ========
1. Purchase a ticket (test)
2. Add product
3. View purchased tickets
4. Clear purchase history
5. Log out
""")
    
def menu():

    # Main application welcome screen
    
    instructions = """
======== MAIN MENU ========
Welcome to the NCTX Bus Ticket Application
Pick one of the following options
Enter the Option Number
"""

    print(instructions)

def getChoice(aList):

    # Gets a valid menu choice from the user.
    # This function is reused for different menus in the program.
    
    while True:
        try:
            choice = int(input(f"\nEnter your option number (1 - {len(aList)}): "))
            if 1 <= choice <= len(aList):
                return choice
                break
            else:
                print(f"\nInvalid input. Please enter a number from 1 - {len(aList)}.")
        except ValueError:
            print(f"\nInvalid input. Please enter a number from 1 - {len(aList)}")

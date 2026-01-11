import sys

accounts = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "user1", "role": "customer"},
    {"username": "user2", "password": "user2", "role": "customer"},
    ]

def login():
    print("""
======== MOBILE TICKETS ========
1. Log in
2. Continue as guest
3. Exit
""")


    while True:
        try:
            choice = int(input("Choose an option: "))

            if choice == 3:
                print("\nGoodbye!")
                sys.exit()

            if choice == 2:
                print("\nContinuing as guest...")
                return None, None

            elif choice == 1:
                username = input("\nEnter username: ")
                password = input("\nEnter password: ")

                for account in accounts:
                    if account["username"] == username and account["password"] == password:
                        print(f"\nLogin successful! Logged in as: {username}\n")
                        return account["role"], username

                print("\nInvalid username or password. Try again.\n")

            else:
                print("\nPlease enter 1 or 2.")

        except ValueError:
            print("\nInvalid input. Please enter a number.")

def getChoice(aList):
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

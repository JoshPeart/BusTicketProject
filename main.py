import csv

class Category:
    def __init__(self, code, title, description):
        self.code = code
        self.title = title
        self.description = description
        
    def getCode(self):
        return self.code

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

class Product:
    def __init__(self, code, title, price_pence):
        self.code = code
        self.title = title
        self.price_pence = int(price_pence)

    def price_pounds(self):
        return self.price_pence / 100

# Accounts dictionary
accounts = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "user1", "role": "customer"},
    {"username": "user2", "password": "user2", "role": "customer"},
    ]

def login():
    print("""
========Mobile Tickets========
1. Log in
2. Continue as guest
""")


    while True:
        try:
            choice = int(input("Choose an option: "))

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

def userMenu():
    print("""
======== USER MENU ========
1. View purchased tickets
2. Purchase a ticket
3. Log out
""")

def adminMenu():
    print("""
======== ADMIN MENU ========
1. Purchase a ticket (test)
2. Add product
3. View purchased tickets
4. Clear purchase history
5. Log out
""")
    
def menu():
    instructions = """
========MAIN MENU========
Welcome to the NCTX Bus Ticket Application
Pick one of the following options
Enter the Option Number
"""

    print(instructions)

def createCategories():
    categoryList = []
    categoryObjectList = []
    code = 1

    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines["category_title"] not in categoryList:
                categoryList.append(lines["category_title"])
                thisCat = Category(code, lines["category_title"], lines["category_description"])
                categoryObjectList.append(thisCat)
                code += 1
    return categoryObjectList

def createProduct(chosenCat):
    
    productObjectList = []
    code = 1
    
    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines["category_title"] == chosenCat.title:
             
                thisProd = Product(code, lines["topup_title"], lines["topup_price_in_pence"])
                productObjectList.append(thisProd)
                code += 1
    return productObjectList
    
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

def ticketPurchase(products, role, username):
    while True:
        try:
            buy = int(input("\nWould you like to purchase a ticket? Enter the code: "))
            if 1 <= buy <= len(products):
                break
            else:
                print(f"\nInvalid input. Please enter a number from 1 - {len(products)}.")
        except ValueError:
            print(f"\nInvalid input. Please enter a number from 1 - {len(products)}")

    chosenProd = products[buy - 1]

    print(f"\nYou have chosen: {chosenProd.title} for £{chosenProd.price_pounds():.2f}")

    if role is None:
        print("\nYou must log in to complete this purchase.")
        role, username = login()

        if role is None:
            print("\nPurchase cancelled. Guest users cannot buy tickets.\n")
            return role, username
    
    confirm = input("\nConfirm your purchase: (y/n) ")

    if confirm == 'y':
        print("\n========TRANSACTION SUCCESSFUL========")
        print(f"Ticket: {chosenProd.title}")
        print(f"Price Paid: £{chosenProd.price_pounds():.2f}")
        print("Thank you for your purchase!\n")

        with open("purchases.csv", "a", newline ="") as file:
            writer = csv.writer(file)
            writer.writerow([username,
                             chosenProd.code,
                             chosenProd.title,
                             f"{chosenProd.price_pounds():.2f}"])
    
    else:
        print("\nPurchase Cancelled \n")
          
def viewTickets(username, role):
    try:
        with open("purchases.csv", "r") as file:
            reader = csv.reader(file)
            print("\n===== PURCHASED TICKETS =====")

            found = False
            
            for row in reader:

                if role == "admin":
                    print(f"User: {row[0]} | {row[2]} - £{row[3]}")
                    found = True

                elif role == "customer":
                    print(f"{row[2]} - £{row[3]}")
                    found = True

            if not found:
                print("\nNo tickets found.")
                
            print()
            
    except FileNotFoundError:
        print("\nNo tickets purchased yet.\n")

def clearPurchases():
    
    with open("purchases.csv", "w", newline="") as file:
            writer = csv.writer(file)

#main
role, username = login()

while True:

    if role == "customer":
        userMenu()
        try:
            user_choice = int(input("Choose an option: "))

            if user_choice == 1: # view ticket purchases
                viewTickets(username, role)
                continue

            elif user_choice == 2: # purchase ticket
                pass

            elif user_choice == 3: # log out
                print("\nLogged out successfully.\n")
                role = None
                continue

            else:
                print("\nInvalid option.")
                continue

        except ValueError:
            print("\nInvalid input.")
            continue

    if role == "admin":
        adminMenu()
        try:
            user_choice = int(input("Choose an option: "))

            if user_choice == 1: # purchase ticket
                continue

            elif user_choice == 2: # add product
                continue

            elif user_choice == 3: # view ticket purchases
                viewTickets(username, role)
                continue

            elif user_choice == 4: # clear purchases
                clearPurchases()
                continue

            elif user_choice == 5: # log out
                print("\nLogged out successfully.\n")
                role = None
                continue

            else:
                print("\nInvalid option.")
                continue

        except ValueError:
            print("\nInvalid input.")
            continue


    menu()
    categories = createCategories()

    for data in categories:
        print(data.getCode(), data.getDescription(), "\n")

    choice = getChoice(categories)
    chosenCat = categories[choice - 1]

    products = createProduct(chosenCat)

    print("\nViewing:", chosenCat.title, "\n")
    for prod in products:
        print(prod.code, prod.title, f"- £{prod.price_pounds():.2f}", "\n")

    #Ticket Purchasing section
        
    role = ticketPurchase(products, role, username)

    try:
        again = input("Would you like to return to the main menu? (y/n) ")

        if again == 'n':
            print("\nGoodbye!")
            break
        else:
            print("\nReturning to the main menu..")
    except ValueError:
            print(f"\nInvalid input.")



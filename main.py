import csv
import sys
import uuid

class Category:
    def __init__(self, code, category_id, title, description, entitlement_type):
        self.code = code
        self.category_id = category_id
        self.title = title
        self.description = description
        self.entitlement_type = entitlement_type
        
    def getCode(self):
        return self.code

    def getId(self):
        return self.category_id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getEntitlementType(self):
        return self.entitlement_type

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
======== MAIN MENU ========
Welcome to the NCTX Bus Ticket Application
Pick one of the following options
Enter the Option Number
"""

    print(instructions)

def createCategories():
    categoryList = []
    categoryObjectList = []
    subcategories = set()
    code = 1

    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:

            name = lines.get("topup_passenger_class_name")
            if name:
                subcategories.add(name)
                
            if lines["category_title"] not in categoryList:
                categoryList.append(lines["category_title"])
                
                thisCat = Category(
                    code,
                    lines["category_id"],
                    lines["category_title"],
                    lines["category_description"],
                    lines["topup_entitlement_type"])
                
                categoryObjectList.append(thisCat)
                code += 1

    return categoryObjectList, sorted(subcategories)

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
        print("\n======== TRANSACTION SUCCESSFUL ========")
        print(f"Ticket: {chosenProd.title}")
        print(f"Price Paid: £{chosenProd.price_pounds():.2f}")
        print("Thank you for your purchase!\n")

        with open("purchases.csv", "a", newline ="") as file:
            writer = csv.writer(file)
            writer.writerow([username,
                             chosenProd.code,
                             chosenProd.title,
                             f"{chosenProd.price_pounds():.2f}"])

        return role, username

    else:
        print("\nPurchase Cancelled \n")

        return role, username
          
def viewTickets(username, role):
    try:
        with open("purchases.csv", "r") as file:
            reader = csv.reader(file)
            print("\n======== PURCHASED TICKETS ========")

            found = False
            
            for row in reader:

                if role == "admin":
                    print(f"User: {row[0]} | {row[2]} - £{row[3]}")
                    found = True
                    
                elif role == "customer" and row[0] == username:
                        print(f"{row[2]} - £{row[3]}")
                        found = True

            if not found:
                print("\nNo tickets found.")
                
            print()
            
    except FileNotFoundError:
        print("\nNo tickets purchased yet.\n")

def clearPurchases():
    
    print("\nWARNING: This will permanently delete ALL purchase data.")
    confirm = input('\nType "DELETE ALL" to confirm: ')

    if confirm != "DELETE ALL":
        print("\nOperation cancelled.")
        return
    
    with open("purchases.csv", "w", newline="") as file:
            writer = csv.writer(file)

def addProduct():

    print("\n======== ADD PRODUCT ========")

    categories, subcategories = createCategories()

    print("\nSelect a category:\n")
    for cat in categories:
        print(f"{cat.code}. {cat.title}\n")

    choice = getChoice(categories)
    chosen_category = categories[choice - 1]

    if choice <= len(categories):
        chosen_category = categories[choice - 1]
        category_id = chosen_category.category_id 
        category_title = chosen_category.title 
        category_description = chosen_category.description
        entitlement_type = chosen_category.entitlement_type

    print(f"\nYou are adding a ticket to: {category_title}")

    topup_id = str(uuid.uuid4())
    topup_title = input("\nEnter ticket title: ")
    topup_description = input("Enter ticket description: ")

    while True:
        try:
            topup_price = int(input("Enter price in pence: "))
            if topup_price < 0:
                print("Price must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")


    print("\nSelect passenger class:\n")
    for i, subcat in enumerate(subcategories, start=1):
        label = f"{subcat} (Group booking)" if subcat.endswith("s") else subcat
        print(f"{i}. {label}")

    choice = getChoice(subcategories)
    passenger_class = subcategories[choice - 1]

    if passenger_class in ("Adults", "Under 19s"):
        while True:
            try:
                quantity = int(input("How many people will this group ticket accommodate: "))
                if quantity > 0:
                    break
                print("Quantity must be at least 1.")
            except ValueError:
                print("Enter a valid number.")
    else:
        quantity = 1

    print("\n======== CONFIRM NEW PRODUCT ========")
    print(category_id)
    print(category_title)
    print(category_description)
    print(topup_id)
    print(topup_title)
    print(topup_description)
    print(topup_price)
    print(entitlement_type)
    print(passenger_class)
    print(quantity)

    confirm = input("\nSave this product to CSV? (y/n): ")

    if confirm != "y":
        print("\nProduct NOT saved.\n")
        return

    with open("mobile_products.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            category_id,
            category_title,
            category_description,
            topup_id,
            topup_title,
            topup_description,
            topup_price,
            entitlement_type,
            passenger_class,
            quantity
        ])

    print("\nProduct added successfully!\n")
        
    

#main
role = None
username = None
logged_out = False

while True:
    
    if role is None:
        role, username = login()
    
    while role == "customer":
        userMenu()
        try:
            user_choice = int(input("Choose an option: "))

            if user_choice == 1: # view ticket purchases
                viewTickets(username, role)

            elif user_choice == 2: # purchase ticket
                break

            elif user_choice == 3: # log out
                print("\nLogged out successfully.\n")
                role = None
                logged_out = True
                break

            else:
                print("\nInvalid option.")

        except ValueError:
            print("\nInvalid input.")

    while role == "admin":
        adminMenu()
        try:
            user_choice = int(input("Choose an option: "))

            if user_choice == 1: # purchase ticket
                break

            elif user_choice == 2: # add product
                addProduct()

            elif user_choice == 3: # view ticket purchases
                viewTickets(username, role)

            elif user_choice == 4: # clear purchases
                clearPurchases()

            elif user_choice == 5: # log out
                print("\nLogged out successfully.\n")
                role = None
                logged_out = True
                break

            else:
                print("\nInvalid option.")

        except ValueError:
            print("\nInvalid input.")

    if logged_out:
        logged_out = False
        continue

    menu()
    categories, subcategories = createCategories()

    for data in categories:
        print(data.getCode(), data.getDescription(), "\n")

    choice = getChoice(categories)
    chosenCat = categories[choice - 1]

    products = createProduct(chosenCat)

    print("\nViewing:", chosenCat.title, "\n")
    for prod in products:
        print(prod.code, prod.title, f"- £{prod.price_pounds():.2f}", "\n")

    #Ticket Purchasing section
        
    role, username = ticketPurchase(products, role, username)

    try:
        again = input("Would you like to return to the main menu? (y/n) ")

        if again == 'n':
            print("\nGoodbye!")
            break
        else:
            print("\nReturning to the main menu..")
    except ValueError:
            print(f"\nInvalid input.")



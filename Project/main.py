import csv
from auth import login, getChoice
from csv_handler import createCategories, createProduct, viewTickets, clearPurchases
from product_manager import addProduct
from models import Product

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

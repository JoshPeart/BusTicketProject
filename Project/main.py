# Main program file
# Here is where everything is run
# The menus and 

import csv
from auth import login, userMenu, adminMenu, menu, getChoice
from csv_handler import createCategories, createProduct, viewTickets, clearPurchases, ticketPurchase
from product_manager import addProduct
from models import Product


# Track login state across the program
role = None
username = None
logged_out = False


# Main program loop
while True:

    # Force login if no user is logged in
    if role is None:
        role, username = login()

    # Customer loop and menu 
    while role == "customer":
        userMenu()
        try:
            user_choice = int(input("Choose an option: "))

            if user_choice == 1: # View ticket purchases
                viewTickets(username, role)

            elif user_choice == 2: # Purchase ticket
                break

            elif user_choice == 3: # Log out
                print("\nLogged out successfully.\n")
                role = None
                logged_out = True
                break

            else:
                print("\nInvalid option.")

        except ValueError:
            print("\nInvalid input.")

    # Admin loop and menu
    while role == "admin":
        adminMenu()
        try:
            user_choice = int(input("Choose an option: "))

            if user_choice == 1: # Purchase ticket
                break

            elif user_choice == 2: # Add product
                addProduct()

            elif user_choice == 3: # View ticket purchases
                viewTickets(username, role)

            elif user_choice == 4: # Clear purchases
                clearPurchases()

            elif user_choice == 5: # Log out
                print("\nLogged out successfully.\n")
                role = None
                logged_oukt = True
                break

            else:
                print("\nInvalid option.")

        except ValueError:
            print("\nInvalid input.")

    # Restart the main loop if the user is logged out
    if logged_out:
        logged_out = False
        continue

    # Main display of the avaliable categories and products
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

    # Ticket Purchasing section
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

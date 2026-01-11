# Here I have the functions that read, write or append to a CSV file
# Creating the categories and products
# Viewing the tickets
# Purchasing the tickets
# Wiping the purchase history

import csv
import uuid
from models import Category, Product
from auth import login

def createCategories():

    # Reads the mobile products CSV and creates Category objects
    # Also collects any subcategories (passenger class names) and returns them in a sorted list
    
    categoryList = []
    categoryObjectList = []
    subcategories = set()     # Use of set to avoid duplicate subcategories
    code = 1

    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            
            # Collect the passenger class names if they exist
            name = lines.get("topup_passenger_class_name")
            if name:
                subcategories.add(name)

            # Create new Category if it hasnt been added yet
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

    # Creates product objects for a selected category
    
    productObjectList = []
    code = 1
    
    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            # Match product data with the chosen category
            if lines["category_title"] == chosenCat.title:
             
                thisProd = Product(code,
                                   lines["topup_id"],
                                   lines["topup_title"],
                                   lines["topup_price_in_pence"])
                
                productObjectList.append(thisProd)
                code += 1
    return productObjectList

def viewTickets(username, role):

    # Displays purchased tickets
    # Admin users can see all purchases, customers only see their own
    
    try:
        with open("purchases.csv", "r") as file:
            reader = csv.reader(file)
            print("\n======== PURCHASED TICKETS ========")

            found = False
            
            for row in reader:
                
                # Admin sees:
                # User: username | Ticket - £00.00 | uuid code
                
                if role == "admin":
                    print(f"User: {row[0]} | {row[2]} - £{row[3]} | {row[1]}")
                    found = True

                # Customer sees:
                # Ticket - £00.00
                
                elif role == "customer" and row[0] == username:
                        print(f"{row[2]} - £{row[3]}")
                        found = True

            if not found:
                print("\nNo tickets found.")
                
            print()
            
    except FileNotFoundError:
        print("\nNo tickets purchased yet.\n")

def ticketPurchase(products, role, username):

    # Uses the users role and username to make sure they are logged in before purchasing

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

    # Prevents guest users from purchasing a ticket
    if role is None:
        print("\nYou must log in to complete this purchase.")
        role, username = login()

        if role is None:
            print("\nPurchase cancelled. Guest users cannot buy tickets.\n")
            return role, username

    while True:
        confirm = input("\nConfirm your purchase: (y/n) ")
        if confirm in ('y', 'n'):
            break
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")
        

    if confirm == 'y':
        print("\n======== TRANSACTION SUCCESSFUL ========")
        print(f"Ticket: {chosenProd.title}")
        print(f"Price Paid: £{chosenProd.price_pounds():.2f}")
        print("Thank you for your purchase!\n")

        # Save that purchase to the CSV
        with open("purchases.csv", "a", newline ="") as file:
            writer = csv.writer(file)
            writer.writerow([username,
                             chosenProd.topup_id,
                             chosenProd.title,
                             f"{chosenProd.price_pounds():.2f}"])

        return role, username

    else:
        print("\nPurchase Cancelled \n")

        return role, username

def clearPurchases():

    # Admins can delete all purchase data
    # Clears purchases.csv after confirmation
    
    print("\nWARNING: This will permanently delete ALL purchase data.")
    confirm = input('\nType "DELETE ALL" to confirm: ')

    if confirm != "DELETE ALL":
        print("\nOperation cancelled.")
        return

    # Overwrites the file to remove all stored purchases
    with open("purchases.csv", "w", newline="") as file:
            writer = csv.writer(file)

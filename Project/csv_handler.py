import csv
import uuid
from models import Category, Product

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

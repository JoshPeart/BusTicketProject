import csv
import uuid
from csv_handler import createCategories
from models import Category
from auth import getChoice

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

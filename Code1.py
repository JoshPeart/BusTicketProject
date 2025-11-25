class Product:
    def __init__(self, code, title, description, price_pence, category):
        self.code = code
        self.title = title
        self.description = description
        self.price_pence = int(price_pence)
        self.category = category

    def price_pounds(self):
        return self.price_pence / 100


# Importing module(s)
import csv

# CSV filename
filename = 'mobile_products.csv'


def readFile(filename):
    # Lists for CSV data
    fields = []
    rows = []

    # Open and read the CSV file
    with open(filename, mode = 'r') as csv_file:
        # Create DictReader object
        csv_reader = csv.DictReader(csv_file)

        # Get field names (column headers)
        fields = csv_reader.fieldnames

        # Loop through each row in the CSV file
        for row in csv_reader:
            rows.append(row)

    return fields, rows

# Get values from readFile function
fields, rows = readFile(filename)

# List of ticket options
options = ["1 Academic Year Tickets",
           "2 Single Tickets",
           "3 24 Hour Tickets",
           "4 Group Tickets",
           "5 Season Tickets",
           "6 Network Tickets",
           "7 NCT Partners"
           ]

instructions = """
Welcome to the NCTX Bus Ticket Application
Pick one of the following options
Enter the Option Number
"""

print(instructions)

# Printing the options
for option in options:
    print(option)

while True:
    try:
        choice = int(input("\nEnter your option number: "))
        if 1 <= choice <= 7:
            break
        else:
            print("\nInvalid input. Please enter a number from 1 - 7.")
    except ValueError:
        print("\nInvalid input. Please enter a number from 1 - 7")

# Option 1 - 7 - show tickets by category
if 1 <= choice <= 7:
    # Map numbers to category titles
    category_map = {
        1: "Academic Year Tickets",
        2: "Single Tickets - City Zone",
        3: "24 Hour Tickets - City Zone",
        4: "Group Tickets",
        5: "Season Tickets - City Zone",
        6: "Network Tickets",
        7: "NCT Partners"
    }

    # Match the selected category to the map
    selected_category = category_map[choice]
    print("\nYou selected:", selected_category, "\n")

    # List for subcategories
    available_subcats = []

    # Get subcategory values and add them to the list
    for row in rows:
        if row["category_title"] == selected_category:
            available_subcats.append(row["topup_passenger_class_name"])

    print("Available subcategories for your selection:\n")
    
    # Gather unique values and add them to a new list
    unique_subcats = list(dict.fromkeys(available_subcats)) # Dictionary keys can not repeat, so duplicates are removed

    # Print unique values in a numbered list
    for i, subcat in enumerate(unique_subcats, start = 1): 
        print(i, subcat) # enumerate returns pairs of (index, value)

    # User chooses a subcategory option
    while True:
        try:
            subcat_choice = int(input(f"\nWhich subcategory would you like to choose? (1-{len(unique_subcats)}) "))
            if 1 <= subcat_choice <= len(unique_subcats):
                subcat = unique_subcats[subcat_choice - 1]
                break
            else:
                print(f"\nInvalid input. Please enter a number from 1 - {len(unique_subcats)}.")
        except ValueError:
            print(f"\nInvalid input. Please enter a number from 1 - {len(unique_subcats)}.")

    print("\nMatching Tickets:\n")

    found = False

    # Go through all rows and print matching tickets
    for row in rows:
        if row["category_title"] == selected_category and row["topup_passenger_class_name"] == subcat:

            found = True
            
            print("Ticket:", row["topup_title"])
            print("Description:", row["topup_description"])
            # Pence to Pound conversion
            price_in_pounds = int(row["topup_price_in_pence"]) / 100
            print(f"Price: £{price_in_pounds:.2f}\n")

    if not found:
        print("No tickets found for that category + subcategory")

# Error if value isnt within the field
else:
    print("\nPlease choose a valid option from 1 to 7.")

# Importing module(s)
import csv

# List of ticket options
options = ["1 Academic Year Tickets",
           "2 Single Tickets", "3 24 Hour Tickets", "4 Group Tickets",
           "5 Season Tickets", "6 Network Tickets", "7 NCT Partners"]

instructions = """
Welcome to the NCTX Bus Ticket Application
Pick one of the following options
Enter the Option Number
"""

print(instructions)

# Printing the options
for option in options:
    print(option)

# User Input
choice = int(input("\nEnter your option number: "))

# CSV filename
filename = 'mobile_products.csv'

def readFile(filepath):
    # Lists for CSV data
    fields = []
    rows = []

    # Open and read the CSV file
    with open(filepath) as csv_file:
        # Create DictReader object
        csv_reader = csv.DictReader(csv_file)

        # Get field names (column headers)
        fields = csv_reader.fieldnames

        # Loop through each row in the CSV file
        for row in csv_reader:
            rows.append(row)
    return fields, rows

# Run readFile function
fields, rows = readFile(filename)

# Option 1 - 7 - show tickets by category
if choice >= 1 and choice <= 7:
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

    # Go through all rows and print matching tickets
    for row in rows:
        if row["category_title"] == selected_category:
            print("Ticket:", row["topup_title"])
            print("Description:", row["topup_description"])
            # Pence to Pound conversion
            price_in_pounds = int(row["topup_price_in_pence"]) / 100
            print(f"Price: £{price_in_pounds:.2f}\n")

# Error if value isnt within the field
else:
    print("\nPlease choose a valid option from 1 to 7.")
    

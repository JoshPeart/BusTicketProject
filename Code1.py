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

    subcat_options = ['Here are the Filter options for you:', '1 Student', '2 Under 19', '3 Under 19 (Group booking)',
                      '4 Under 22', '5 Under 22 (Group booking)', '6 Adult', '7 Adult (Group booking)']
    
    for subcat in subcat_options:
        print(subcat)

    subcat_decision = int(input("\nWhich subcategory would you like to choose? (1-7): "))
    print()

    subcat_map =  {
        1: 'Student',
        2: 'Under 19',
        3: 'Under 19s',
        4: 'Under 22',
        5: 'Under 22s',
        6: 'Adult',
        7: 'Adults'
    }

    subcat = subcat_map[subcat_decision]

    # Go through all rows and print matching tickets
    for row in rows:
        if row["category_title"] == selected_category and row["topup_passenger_class_name"] == subcat:
            print("Ticket:", row["topup_title"])
            print("Description:", row["topup_description"])
            # Pence to Pound conversion
            price_in_pounds = int(row["topup_price_in_pence"]) / 100
            print(f"Price: £{price_in_pounds:.2f}\n")

# Error if value isnt within the field
else:
    print("\nPlease choose a valid option from 1 to 7.")

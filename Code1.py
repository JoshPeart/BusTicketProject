# Importing module(s)
import csv

# List of ticket options
options = ["0 View file data","1 Academic Year Tickets",
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
with open(filename) as csv_file:
    # Create DictReader object
    csv_reader = csv.DictReader(csv_file)

    # Get field names (column headers)
    fields = csv_reader.fieldnames

    # Loop through each row in the CSV file
    for row in csv_reader:
        rows.append(row)

# Option 0 - showing the basic file info
if choice == 0:
    print("\nField names:", fields)
    print("\nFirst row of data:", rows[0])

# Option 1 - 7 - show tickets by category
elif choice >= 1 and choice <= 7:
    # Map numbers to category titles
    category_map = {
        1: "1 Academic Year Tickets",
        2: "Single Tickets",
        3: "24 Hour Tickets",
        4: "Group Tickets",
        5: "Season Tickets",
        6: "Network Tickets",
        7: "NCT Partners"
    }

    selected_category =  category_map[choice]
    print("\nYou selected:", selected_category)

# Error if value isnt within the field
else:
    print("Please choose a valid option from 1 to 7.")

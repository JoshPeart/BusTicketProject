#importing module(s)
import csv

#List of ticket options
options = ["0 Choose a ticket type:","1 Academic Year Tickets",
           "2 Single Tickets", "3 24 Hour Tickets", "4 Group Tickets",
           "5 Season Tickets", "6 Network Tickets", "7 NCT Partners"]

instructions = """
Welcome to the NCTX Bus Ticket Application
Pick one of the following options
Enter the Option Number
"""

print(instructions)

#printing the options
for option in options:
    print(option)

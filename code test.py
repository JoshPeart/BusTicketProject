class Category:
    def __init__ (self, category, code):
        self.category = category
        self.code = code

    def getCat (self):
        return self.category

    def getCode(self):
        return self.code

import csv

listOfCategories = []
listOfCodes = []

filename = "mobile_products.csv"

with open(filename, mode = 'r') as file:
    csvFile = csv.DictReader(file)
    code = 0
    for lines in csvFile:
        category = lines["category_title"]
        if category not in listOfCategories:
            listOfCategories.append(category)
            listOfCodes.append(code)
            #cat1 = Category(category, code)
            #print(cat1.getCat())
            code += 1

for code, cat in zip(listOfCodes, listOfCategories):
    print(code, cat)

userChoice = int(input())
catChoice = listOfCategories[userChoice]
print("You have chosen: ", catChoice, "\n")

with open(filename, mode = 'r') as file:
    csvFile = csv.DictReader(file)
    print(f"the types of {catChoice} we have are:")
    for lines in csvFile:
        if catChoice == lines["category_title"]:
            print(lines['topup_title'])

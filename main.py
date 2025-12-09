import csv

class Category:
    def __init__(self, code, title, description, price_pence):
        self.code = code
        self.title = title
        self.description = description
        self.price_pence = int(price_pence)

    def price_pounds(self):
        return self.price_pence / 100

    def getCode(self):
        return self.code

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

class Product:
    def __init__(self, code, title):
        self.code = code
        self.title = title



def menu():
    instructions = """
    Welcome to the NCTX Bus Ticket Application
    Pick one of the following options
    Enter the Option Number
    """

    print(instructions)

def createCategories():
    categoryList = []
    categoryObjectList = []
    code = 1

    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines["category_title"] not in categoryList:
                categoryList.append(lines["category_title"])
                thisCat = Category(code, lines["category_title"], lines["category_description"], lines["topup_price_in_pence"])
                categoryObjectList.append(thisCat)
                code += 1
    return categoryObjectList

def createProduct(chosenCat):
    
    productObjectList = []
    code = 1
    
    with open('mobile_products.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines["category_title"] == chosenCat.title:
             
                thisProd = Product(code, lines["topup_title"])
                productObjectList.append(thisProd)
                code += 1
    return productObjectList
    
def getChoice(aList):
    while True:
        try:
            choice = int(input("\nEnter your option number: "))
            if 1 <= choice <= len(aList):
                return choice
                break
            else:
                print(f"\nInvalid input. Please enter a number from 1 - {len(aList)}.")
        except ValueError:
            print(f"\nInvalid input. Please enter a number from 1 - {len(aList)}")
    

#main

menu()
categories = createCategories()

for data in categories:
    print(data.getCode(), data.getDescription(), "\n")

choice = getChoice(categories)
choice -=1
chosenCat = categories[choice]

products = createProduct(chosenCat)

for prod in products:
    print(prod.title, "\n")

choice = getChoice(products)

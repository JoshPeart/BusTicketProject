# Holds all of the classes

class Category:
    def __init__(self, code, category_id, title, description, entitlement_type):
        self.code = code
        self.category_id = category_id
        self.title = title
        self.description = description
        self.entitlement_type = entitlement_type
        
    def getCode(self):
        return self.code

    def getId(self):
        return self.category_id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getEntitlementType(self):
        return self.entitlement_type

class Product:
    def __init__(self, code, topup_id, title, price_pence):
        self.code = code
        self.topup_id = topup_id
        self.title = title
        self.price_pence = int(price_pence)

    def price_pounds(self):
        return self.price_pence / 100

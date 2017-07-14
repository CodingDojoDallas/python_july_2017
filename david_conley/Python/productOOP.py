class Product(object):
    def __init__(self, price, name, weight, brand, cost, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        taxamount = float(self.price) * tax
        priceaftertax = float(self.price) + taxamount
        print "Price after tax is", priceaftertax
        return self


    def returnProduct(self, returnReason):
        if returnReason == "defective":
            self.status = "defective"
            defective = "0"
            print "Price:", defective
            return self
        elif returnReason == "in box":
            self.status = "for sale"
            return self
        elif returnReason == "box opened":
            self.status = "used"
            boxopened = float(self.price) * .8
            print "New price:", boxopened
            return self


    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)
        print "____________________________________"

pen = Product("5", "pen", "1oz", "bic", ".05")
markers = Product("3.50", "markers", "5oz", "sharpie", ".50")
notebook = Product("5.00", "notebook", "8oz", "five star", ".10")
ruler = Product("2.25", "ruler", "1oz", "staples", ".01")
crayons = Product("4.50", "crayons", "6oz", "crayola", ".30")

pen.addTax(.08).returnProduct("box opened").displayInfo()
markers.displayInfo()
notebook.displayInfo()
ruler.displayInfo()
crayons.displayInfo()

class Product(object):
    def __init__(self, price, name, weight, brand, cost, status='for sale'):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = 'sold'
        return self

    def addTax(self, tax):
        taxamount = float(self.price) * tax 
        priceaftertax = float(self.price) + taxamount       
        print "Price after tax", priceaftertax
        return self

    def returnProduct(self, returnReason):
        if returnReason == 'defective':
            self.status = 'defective'
            defective = '0'
            print 'Price:', defective
            return self
        elif returnReason == 'in box':
            self.status = 'for sale'
            return self    
        elif returnReason == 'box opened':
            self.status = 'used'
            boxopened = float(self.price) * .8
            print 'New price:', boxopened
            return self

    def displayInfo(self):
        print 'Price:' + str(self.price)
        print 'Item Name:' + str(self.name)
        print 'Weight:' + str(self.weight)
        print 'Brands:' + str(self.brand)
        print 'Cost;' + str(self.cost)
        print 'Status:' + str(self.status)
        print '__________________________________' 

pen = Product("5", "pen", "1oz", "bic", ".05")
markers = Product("3.50", "markers", "5oz", "sharpie", ".50")
notebook = Product("5.00", "notebook", "8oz", "five star", ".10")
ruler = Product("2.25", "ruler", "1oz", "staples", ".01")
crayons = Product("4.50", "crayons", "6oz", "crayola", ".30")

pen.addTax(.08).returnProduct("box opened").displayInfo()
markers.displayInfo()
notebook.displayInfo()
ruler.displayInfo()
crayons.displayInfo()
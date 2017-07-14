class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .10
        self.display_all()

    def display_all(self):
        print 'Price: $' + str(self.price)
        print 'Speed: ' + str(self.speed) + ' MPH'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage) + ' MPG'
        print 'Tax: ' + str(self.tax)


mustang = Car(25000, 50, 'Full', 20)
challenger  = Car(12000, 65, 'Half-Full', 15)
firebird = Car(5000, 105, 'Empty', 11)
corvette = Car(7000, 112, '1/4 Tank Remaining', 12)
tesla = Car(70000, 75, 'Hey! I\'m Electric', 200)
fiat = Car(10000, 35, 'Full', 25)

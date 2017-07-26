class Bike (object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print 'Price for this bike is $' + str(self.price)
        print 'The max speed for the bike is ' + str(self.max_speed) + ' mph'
        print 'The total miles for the bike is ' + str(self.miles) + ' miles'

    def ride(self):
        print 'Riding'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5
bike1 = Bike(100, 12)
bike1.ride()
bike1.reverse()
bike1.displayinfo()

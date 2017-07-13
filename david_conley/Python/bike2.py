class Bike(object):
	#initialize method
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayinfo(self):
		print "Bike's price" + str(self.price)	
		print "maximum speed" + str(self.max_speed) + "mph"
		print "Total miles" + str(self.miles) + "miles"

	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -= 5
			return self
			
bike1 = Bike(99.99, 12)
bike2 = Bike(450, 50)
bike3 = Bike(150, 30)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike1.reverse().reverse().reverse().displayinfo()
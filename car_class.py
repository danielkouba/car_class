class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = "15%"
		else:
			self.tax = "12%"
		self.display_all()

	def display_all(self):
		print "Max Speed:\t\t", self.speed
		print "Fuel:\t\t\t", self.fuel
		print "Mileage:\t\t", self.mileage
		print "Price:\t\t\t", self.price
		print "Tax:\t\t\t", self.tax

acura = Car(2000, 88, "Full", 22)
print "\n"
honda = Car(2000, 140, "Full", 22)
print "\n"
ford = Car(1000, 88, "Full", 10)
print "\n"
chevy = Car(20000, 88, "Full", 10)
print "\n"
lincoln = Car(200000, 88, "Full", 8)
print "\n"
volkswagon = Car(100, 50, "Empty", 100)

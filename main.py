

class CarInfo:
	def __init__(self):
		self.symbol = 0
		self.maker = ""
		self.doors = ""
		self.weight = 0.0
		self.horsepower = 0.0
		self.city_mpg = 0.0
		self.price = 0.0
		return

	def parse(self, line):

		items = line.strip().split(",")
		for item in items:
			item = item.strip()
			if item == "?":
				return False

		
		self.symbol = int(items[0])
		self.maker = items[2].strip()
		self.doors = items[5].strip()
		self.weight = float(items[13])
		self.horsepower = float(items[21])
		self.city_mpg = float(items[23])
		self.price = float(items[25])
		return True

	def toString(self):
		line = "%s: %.2f, %.1f" % (self.maker, self.price, self.horsepower)
		return line

def loadCarInfo(fname):
	result = []
	fin = open(fname, 'r')
	for line in fin:
		car = CarInfo()
		if car.parse(line):
			result.append(car)

	fin.close()
	return result

def printCars(cars):
	for car in cars:
		print("%s" % (car.toString()))
	return

def main():
	fname = './data/imports-85.csv'
	cars = loadCarInfo(fname)
	printCars(cars)
	return

if __name__ == "__main__":
	main()

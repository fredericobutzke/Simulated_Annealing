class Cell():
	"This class implements a cell object"
	
	def __init__(self, number, status=None, x=None, y=None):
		if status is None :
			self.status = 'free'
		else :
			self.status = status

		if x is None :
			self.x = int()
		else :
			self.x = x

		if y is None :
			self.y = int()
		else :
			self.y = y

		self.number = number


	def getNumber(self) :
		return self.number

	def setNumber(self, arg) :
		self.number = arg

	def getStatus(self) :
		return self.status

	def setStatus(self, arg) :
		self.status = arg

	def getX(self) :
		return self.x

	def setX(self, arg) :
		self.x = arg

	def getY(self) :
		return self.y

	def setY(self, arg) :
		self.y = arg
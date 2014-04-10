class Grid():
	"This class implements a hash table that"
	"is a Grid."
	def __init__(self):
		self.grid = dict()
		
	def getGrid(self):
		return self.grid

	def addCell(self, cell, x, y):
		self.grid[cell] = [x, y]

	def updateCell(self, cell, x, y):
		self.grid[cell] = [x, y]

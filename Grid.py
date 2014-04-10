class Grid():
	"This class implements a hash table that"
	"is a Grid."
	def __init__(self):
		self.grid = list()
		
	def getGrid(self):
		return self.grid

	def addCell(self, cell, x, y):
		self.grid.insert(cell, [x, y])

	def updateCell(self, cell, x, y):
		self.grid[cell] = [x, y]

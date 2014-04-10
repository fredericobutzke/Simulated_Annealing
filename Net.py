class Nets():
	"This class implements the netlist structure"
	def __init__(self):
		self.Nets = list()

	def addNet(self, cells):
		self.Nets.append(cells)

	def removeNet(self, cells):
		self.Nets.remove([c for c in cells])

	def getNets(self):
		return self.Nets 
		
from Net import Nets
from Cell import Cell

class FileRead():
	"This class read the data input file"
	def __init__ (self, file_name, permission) :
		fo = open(file_name, permission)
		self.lines = fo.readlines()
		self.heigh = 0
		self.width = 0
		self.nets  = Nets()
		self.cells = list()
		self.cells_set = set()

	def getData(self) :
		for i, line in enumerate(self.lines) :
			if ".grid" in line :
				self.option = 0
				continue
			elif ".netlist" in line :
				self.option = 1
				continue
			elif ".cells" in line :
				self.option = 2
				continue
			elif ".end" in line :
				fixed_cells = {x.getNumber() for x in self.cells}
				tmp = sorted(list(self.cells_set.difference(fixed_cells)))
				map(lambda c : self.cells.insert(int(c)-1, Cell(int(c))), [c for c in tmp])
				return self.heigh, self.width, self.nets, self.cells

			if self.option == 0 :
				self.width, self.heigh = [int(v) for v in line.split()]
		
			elif self.option == 1 :
				cells = [int(c.lstrip('c')) for c in line.split()]
				self.nets.addNet(cells)
				map(lambda c : self.cells_set.add(c), [c for c in cells])

			elif self.option == 2 :
				pos, x, y = line.lstrip('c').split();
				self.cells.insert(int(pos)-1, Cell(int(pos), 'fixed', int(x), int(y)))
	
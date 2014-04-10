from Net import Nets

class FileRead():
	"This class read the data input file"
	def __init__ (self, file_name, permission) :
		fo = open(file_name, permission)
		self.lines = fo.readlines()
		self.gridx = 0
		self.gridy = 0
		self.nets  = Nets()
		self.fixed_cells = dict()
		self.cells = set()

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
				return self.gridx, self.gridy, self.nets, self.fixed_cells, sorted(list(self.cells))


			if self.option == 0 :
				self.gridx, self.gridy = [int(v) for v in line.split()]
		
			elif self.option == 1 :
				cells = [c for c in line.split()]
				self.nets.addNet(cells)
				map(lambda c : self.cells.add(c), [c for c in cells])

			elif self.option == 2 :
				name, x, y = line.split();
				self.fixed_cells[name] = [x, y]

	
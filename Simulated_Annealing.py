from FileRead import FileRead
import Utilities
from Cell import Cell

def printCells() :
	print "\n# status x y"
	for cell in cells :
		print cell.getNumber(), cell.getStatus(), ' ', cell.getX(), cell.getY()

fl = FileRead("hw3.data", "r")
width, height, nets, cells = fl.getData() 

print "x: ", width
print "y: ", height
print "\nnets:", [net for net in nets.getNets()]
print "\ncells:" 
printCells()

cells = Utilities.genInitialGrid(cells, width, height) 
printCells()

cells = Utilities.genNeighbor(cells)

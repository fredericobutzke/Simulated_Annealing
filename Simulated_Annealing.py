from FileRead import FileRead
from Grid import Grid
import Utilities
from Cell import Cell

fl = FileRead("hw3.data", "r")
width, height, nets, cells = fl.getData() 

print "x: ", width
print "y: ", height
print "\nnets:", [net for net in nets.getNets()]
print "\ncells:" 
for cell in cells :
	print cell.getNumber(), cell.getStatus(), cell.getX(), cell.getY()
#grid = Utilities.genInitialGrid(fixed_cells, cells, gridx, gridy) 
#print grid.getGrid()


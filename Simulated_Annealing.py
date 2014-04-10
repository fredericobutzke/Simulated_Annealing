from FileRead import FileRead

fl = FileRead("hw3.data", "r")
gridx, gridy, nets, fixed_cells, cells = fl.getData() 

print "x: ", gridx
print "y: ", gridy
print "nets: \n", [net for net in nets.getNets()]
print "cells: \n", cells
print "fixed cells: \n", fixed_cells
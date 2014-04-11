from FileRead import FileRead
import Utilities
from Cell import Cell
import math
import copy
import random

def printCells(cs) :
	print "\n# status x y"
	for cell in cs :
		print cell.getNumber(), cell.getStatus(), ' ', cell.getX(), cell.getY()

def Metropolis(S, T, M) :
	while M != 0 :
		NewS = Utilities.genNeighbor(copy.deepcopy(S))
		deltaH = Utilities.cost(NewS, nets) - Utilities.cost(S, nets)
		exp = -deltaH/T 
		if deltaH < 0 :
			S = NewS;
		elif random.random() < math.exp(exp) :
		 	S = NewS;
		M = M - 1;
	return S

def Simulated_annealing(S0, T0, alpha, beta, M) :
	T = T0
	S = S0
	Time = 0
	while T >= 0.1 :
		S = Metropolis(S, T, copy.copy(M))
		Time += M
		T *= alpha
		M *= beta
	return S 


##### 
#Main
fl = FileRead("hw3.data", "r")
width, height, nets, cells = fl.getData() 

cells = Utilities.genInitialGrid(cells, width, height) 
printCells(cells)
print Utilities.cost(cells, nets)

cells = Simulated_annealing(cells, 10, 0.9, 1, 10)
printCells(cells)
print Utilities.cost(cells, nets)
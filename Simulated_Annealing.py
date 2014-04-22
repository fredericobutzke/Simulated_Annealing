#!/usr/bin/python

from FileRead import FileRead
import Utilities
from Cell import Cell
import math
import copy
import random
import time
import getopt
import sys

def printCells(cs) :
	print "# status x y"
	for cell in cs :
		print cell.getNumber(), cell.getStatus(), ' ', cell.getX(), cell.getY()

def Metropolis(S, T, M) :
	hill_climbing = int()
	while M != 0 :
		NewS = Utilities.genNeighbor(copy.deepcopy(S))
		deltaH = Utilities.cost(NewS, nets) - Utilities.cost(S, nets)
		exp = -deltaH/T 
		if deltaH < 0 :
			S = NewS;
		elif random.random() < math.exp(exp) :
		 	S = NewS;
		 	hill_climbing += 1
		M = M - 1;
	return S, hill_climbing

def Simulated_annealing(S0, T0, alpha, beta, M, X) :
	T = T0
	S = S0
	Time = 0
	Hills = int()
	while T >= X :
		S, hill_climbing = Metropolis(S, T, copy.copy(M))
		Time += M
		T *= alpha
		M *= beta
		Hills += hill_climbing
	return S, Hills


##### 
#Main

try:
	values, arguments = getopt.getopt(sys.argv[1:], "i:ht:a:b:m:x:")
	if values == [] or "i" not in [i[0].strip('-') for i in values] :
		values = [('-h','')]
except getopt.GetoptError :
	print 'parsing.py -i <inputfile>'	
for opt, value in values :
	if opt == "-h" :
		print 'Usage:'
		print 'Required Arguments:'
		print '-i <inputfile>'
		print '-t <initial temperature>'
		print '-a <cooling rate, alpha>'
		print '-b <constant beta>'
		print '-m <time until next parameter update in Metropolis>'
		print '-x <the value t should be to finish the execution>'
		print 'Optional Arguments:'
		print '-h help(display this msg)'
		sys.exit()
	elif opt == "-i" :
		input_file = value
	elif opt == "-t" :
		T0 = float(value)
	elif opt == "-a" :
		alpha = float(value)	
	elif opt == "-b" :
		beta = float(value)
	elif opt == "-m" :
		M = float(value)
	elif opt == "-x" :
		X = float(value)

fl = FileRead(input_file, "r")
width, height, nets, cells = fl.getData() 

print "\nInitial Placement: "
cells = Utilities.genInitialGrid(cells, width, height) 
printCells(cells)
print "Initial Cost:", Utilities.cost(cells, nets)

print "\nSolution: "
time_init = time.time()
cells, hills = Simulated_annealing(cells, T0, alpha, beta, M, X)
time_end = time.time()
printCells(cells)
print "Final Cost:", Utilities.cost(cells, nets)
print "\"Hills Climbed\": ", hills
print "Time: ", round(time_end - time_init, 2), " s"
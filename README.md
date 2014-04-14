This project performs a placement of the netlist described in the file 
"hw3.data". It has nine cells and it creates a 3x3 grid.

The objective is to minimize the length of the wires or nets in the 
routing problem.

The algorithm is based on Simulated Annealing.

Running the project:
python Simulated_Annealing.py -i hw3.data -t 10 -a .9 -b 1 -m 10 -x .5

Where, 
-i <inputfile>
-t <initial temperature>
-a <cooling rate, alpha>
-b <constant, beta>
-m <time until next parameter update in Metropolis function>
-x <the value t should be to finish the execution>
-h help

The output displays the initial random netlist, the initial cost, the 
final netlist that the heuristic found as the best solution, final cost,
how much time the function ran and how many "hill climbs" it accepted.

This project was developed using Python version 2.7.4.

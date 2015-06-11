# sexy_attractor
######################################################################
sexy attractor - numerical timestep propagator for the Lorenz
attractor equations - mini project for python course at aalborg
university, "summer" 2015

daniel lawther, unclellama@gmail.com
######################################################################

this file has an attached example: if you do
>> python sexy_attractor.py
it will produce a plot myplot.pdf showing the lorenz attractor for
a single start location and a given set of [sigma,rho,beta].

you can also do in e.g. ipython:
>> from sexy_attractor import *

so that the functions attractor() or finite_difference_ode() can be
used stand-alone to investigate lorenz attractors or more general ode.

this code also has test cases as outlined in the exercise docs;
they are in seperate text files and can be run using, e.g.
>> python test1.py

######################################################################

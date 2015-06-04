"""
sexy attractor - numerical timestep propagator for the Lorenz
attractor equations - mini project for python course at aalborg
university, "summer" 2015

daniel lawther, DARK/uni.of copenhagen, unclellama@gmail.com

rough map (WIP!)

main - import numpy, scipy, matplotlib
main - define the coefficients
    - sigma, rho, beta
from the lorenz equations, and also the initial conditions at t=0
    - xvec, and probably velocity???
and also set the timestep. maybe a variable timestep depending on the
potential steepness? wanna look at the curvature in a given timestep
and use that to decide the next Dt?
i dunno...

loop over timesteps
    my ODE solver - to propagate the xvec one timestep
    scipy ODE solver - for testing purposes
    logger - to attach various interesting values for this t to a log
    (especially interested in divergence speed of my solution from the
    scipy solver!)
    plotter - draw a line in 3d plot between xvec(t(n-1)) and
    xvec(t(n))
    the line color should depend on speed for this step :)
end loop over timesteps

output
    3d plot in pdf format
    2d slices in pdf
    data structure with t,x(t),... incl. comparisons

######################################################################

my ODE solver?
first try euler finite distance method:
- we have xvec at t(n)
- we have the function, so we can take derivative at t(n)
- and so we can hop along the tangent to t(n+1)
- which will obviously give some error! what to do?
- i *think* the euler method just says fuck that error.

testing plan for ODE solver
- test in 1d first
- test an ODE with a closed solution as 'oracle'

- now go to 3d; but implement scipy ode solver for comparison

testing plan for plotter:
- sanity checks: try points in 3d, do spheres appear as circles in
slices?

testing plan for data storage:
- should be able to replot the trajectory based on the saved points.
- so, be sure to set the code up so that the plotter can be fed
numbers from the output data :)
"""
import numpy as np

def threexsq(x)
    """
    the function f(xvec) equal to d(xvec)/dt in the ODE
    imma start this off as a simple 1d polynomial
    ...for testing purposes :)
    """
    # ** oper should work for np.array objects too, right?
    return 3*x**2

def ode(xvec,f,t,deltat)
    """
    daniel's ordinary differential equation solver based on the euler
    method

    flow:
    - get xvec(t(n)) (in one dimension, a float x - otherwise a np.array x,y,z)
    - calculate xvec(t(n)) + df(t(n),xvec(t(n)))*deltat
    - this gives approximation to xvec(t(n+1))
    - return that!
    """
    # guard against shitty input
    try:
        test=xvec+np.zeroes_like(xvec)
    except (TypeError)
        print "xvec does not appear to be a np array"
        raise
    
    

"""
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

output generated:
    3d plot in pdf format of the solution curve (done!)
    2d slices in pdf format (not done yet!)
    data structure with t,x(t),... incl. comparisons (not done yet!)

######################################################################

testing strategy:

i am trying to follow a test-driven development strategy as
outlined at
http://en.wikipedia.org/wiki/Test-driven_development
...albeit somewhat half-heartedly.

i have made unittests for the ODE solver. to begin with i defined a
polynomial function

def tpoly(t,xvec,params=[1.0,1.0,1.0]):
    return params[0]*3*t**2+params[1]*2*t+params[2]

and tested whether the output of my ODE solver corresponded to the
analytical solution for this function, given an initial xvec=[x0]. i
then worked on the ODE code until its output passed this test.

next i expanded the unittests to test in three spatial dimensions,
with initial conditions [x0,y0,z0] and a known analytical
solution, and expanded the ODE solver functionality until it produced
the correct output in this case. the nice thing about using the
py.test method is that the previous test is still automatically run,
so there is no doubt that the ODE solver still works for 1d input even
after rewriting it to accept n independent variables.

future testing plan:

- implement scipy ODE solver code for comparison for functions
with no analytical solution.
- sanity checks for plotter?
testing plan for data storage:
- should be able to replot the trajectory based on the saved points.
- so, be sure to set the code up so that the plotter can be fed
numbers from the output data :)

######################################################################

quick description of individual functions

lorenz() defines the d(xyz)/dt for the lorenz attractor

make_time() defines a function t(n) that gives the time for
   each loop tick

finite_difference_ode() approximates a
solution for an ordinary differential equation numerically using the
euler finite-difference method ("follow the tangent for a small dt").

attractor() calls finite_difference_ode for the lorenz function, and
plots the results in a pdf file.

######################################################################
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(t,xvec,params):
    """
    the function f(xvec) equal to d(xvec)/dt
    for the lorenz attractor
    """
    sigma=params[0]
    rho=params[1]
    beta=params[2]
    dxdt=sigma*(xvec[1]-xvec[0])
    dydt=xvec[0]*(rho-xvec[2])-xvec[1]
    dzdt=xvec[0]*xvec[1]-beta*xvec[2]
    return np.array([dxdt,dydt,dzdt])

def make_time(timestep):
    """
    takes the timestep variable and makes a function t(n) that tells
    us what the time is.
    inputs: tmestep (float)
    """
    try:
        timestep+1.0
    except TypeError:
        print "timestep should be a float!"
    def t(n):
        """
        gives the time at tick n, based on a previously specified
        timestep size. inputs: n (int)
        """
        try:
            n+int(1)
        except TypeError:
            print("n should be a positive integer!")
        return timestep*n
    return t

def finite_difference_ode(xin,f,params,nmax,deltat):
    """
    ode numerical solver based on euler finite diff method.

    inputs:
    xinit (np.array) is initial vector of dependent var.
    f() is the function equal to d(xvec)/dt in the ODE
    params (python list) is the parameters of f() 
    nmax (int) is the amount of ticks to run for
    deltat (float) is the duration of each loop tick

    outputs:
    the function returns a np.array "nmax*xvec(n)", i.e., a
    value of the position vector for each loop tick n.
    
    """
    
    def rota_fortunae(xvec,t,f,params,deltat):
        """
        performs one timestep.
        
        "So we see that even when Fortuna spins us downward,
        the wheel sometimes halts for a moment and we find ourselves
        in a good, small cycle within a larger bad cycle. The universe,
        of course, is based upon the principle of the circle within the
        circle."
        
        - ignatius p reilly

        """
        xvec=xvec+deltat*f(t,xvec,params)
        return xvec

    # guard against shitty input
    try:
        test=xin+np.zeros_like(xin)
    except TypeError:
        print "xin does not appear to be a np.array"
        raise
    
    t=make_time(deltat) # makes a t(n) function
    print("Running to t_max: ",t(nmax-1))
    xlist=np.zeros((nmax,xin.size))
    xlist[0,:]=xin
    # loop over timesteps
    for n in range(1,nmax):
        xlist[n,:]=rota_fortunae(xlist[n-1,:],t(n),f,params,deltat)
    return xlist

def attractor(xinit=[1.0,1.0,1.0],deltat=0.01,nmax=10000,sigma=1.0,rho=1.0,beta=1.0,plotname="myplot.pdf"):

    def plot_xlist(xlist,nmax):
        xt=xlist[:,0]
        yt=xlist[:,1]
        zt=xlist[:,2]
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot(xt, yt, zt, 'bo', label='Initial condition:'+str(xlist[0,0])+", "
                +str(xlist[0,0])+", "+str(xlist[0,0])+"\nEnd position:"+'{0:.2f}'.format(xlist[nmax-1,0])+", "
                +'{0:.2f}'.format(xlist[nmax-1,1])+", "+'{0:.2f}'.format(xlist[nmax-1,2]))

        ax.legend()

    xin=np.array(xinit)
    params=[sigma,rho,beta] # the lorenz attractor parameters
    
    xlist=finite_difference_ode(xin,lorenz,params,nmax,deltat) # call ode solver

    print("Start coordinate (x,y,z): ",xlist[0,:])
    print("Parameters sigma,rho,beta: ",params)  
    print("End coordinate (x,y,z): ",xlist[nmax-1,:])
    
    plot_xlist(xlist,nmax) # make plot
    plt.savefig(plotname) # save to pdf

if __name__ == "__main__":
    attractor(xinit=[10,-10,10],sigma=10.0,beta=8.0/3.0,rho=6.0)

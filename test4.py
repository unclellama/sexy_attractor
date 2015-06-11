from sexy_attractor import *
import os

"""
test 4 of the test cases described in the exercise specification.
calls the main attractor script, which solves the ODE numerically and
plots the result.
"""
newpath = 'test4/' 
if not os.path.exists(newpath): os.makedirs(newpath)

sigma=14.0
rho=28.0
beta=8.0/3.0

attractor(xinit=[1.0,1.0,1.0],deltat=0.01,nmax=10000,sigma=sigma,rho=rho,beta=beta,plotname=newpath+"init1.pdf")
attractor(xinit=[5.0,-5.0,1.0],deltat=0.01,nmax=10000,sigma=sigma,rho=rho,beta=beta,plotname=newpath+"init2.pdf")
attractor(xinit=[-10.0,5.0,10.0],deltat=0.01,nmax=10000,sigma=sigma,rho=rho,beta=beta,plotname=newpath+"init3.pdf")
attractor(xinit=[0.0,0.0,0.0],deltat=0.01,nmax=10000,sigma=sigma,rho=rho,beta=beta,plotname=newpath+"init4.pdf")
attractor(xinit=[0.0,5.0,-10.0],deltat=0.01,nmax=10000,sigma=sigma,rho=rho,beta=beta,plotname=newpath+"init5.pdf")

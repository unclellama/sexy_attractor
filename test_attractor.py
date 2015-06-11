import unittest
import sexy_attractor as at
import numpy as np

class TestAttractor(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_tpoly1d(self):
        """
        the solver should be able to calculate that dx/dt=a*3t^2+b*t*c
        gives x(t)=at^3+bt^2+ct+x0.
        """
        
        def tpoly(t,xvec,params=[1.0,1.0,1.0]):
            return params[0]*3*t**2+params[1]*2*t+params[2]      
        rtolerance=1.0e-2
        atolerance=1.0e-2
        deltat=0.0001
        testn=500000
        xinit=np.array([-3.0])
        params=[10.0,1.0,3.0]
        t=at.make_time(deltat)
        analytical_result=map(lambda tn: params[0]*(tn**3)+params[1]*(tn**2)+params[2]*tn+xinit, t(np.arange(testn))) # for dx/dt=a*3t^2+b*t*c
        numerical_result=at.finite_difference_ode(xinit,tpoly,params,testn,deltat) 
        self.assertTrue(np.allclose(analytical_result,numerical_result,rtol=rtolerance, atol=atolerance))
        print("t max: ",t(testn-1))

    def test_3d(self):
        """
        the solver should be able to calculate that d(x1,x2)/dt=(2t,2t)
        gives (x1(t),x2(t))=(t**2 i,t**2 j)+x0.
        """
        
        def tlin_3d(t,xvec,params=[1.0]):
            return params[0]*np.array([2*t,2*t,2*t])
            
        rtolerance=1.0e-2
        atolerance=1.0e-2
        deltat=0.0001
        testn=50000
        xinit=np.array([-3.0,1.0,-25.0])
        params=[1.0]
        t=at.make_time(deltat)
        analytical_result=map(lambda tn: np.array([params[0]*tn**2,params[0]*tn**2,params[0]*tn**2])+xinit, t(np.arange(testn))) # for dxi/dt=2xi
        numerical_result=at.finite_difference_ode(xinit,tlin_3d,params,testn,deltat) 
        self.assertTrue(np.allclose(analytical_result,numerical_result,rtol=rtolerance, atol=atolerance))
        print("numerical result: ",numerical_result[testn-1])
        print("analytical result: ",analytical_result[testn-1])
        print("t max: ",t(testn-1))

    #def test_is_not_prime(self):
        #is_prime = check_prime.check_prime(4)
        #self.assertFalse(is_prime)
    #    pass
    
    #def test_small(self):
        #self.assertRaises(ValueError,check_prime.check_prime,1)
        #self.assertRaises(ValueError,check_prime.check_prime,-1)
     #   pass

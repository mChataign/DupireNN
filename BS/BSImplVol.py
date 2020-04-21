__author__ = 'dixon'

from BS import bsformula
from Bisect import bisect
from newton import newton
import numpy as np


def bsimpvol(callput,S0,K,r,T,price,q=0,priceTolerance=0.01,init=0, max_iter=100, method='bisect'):

    '''
    :param callput:judgement for option
    :param S0:intial value of the underlying
    :param K:the strike price
    :param r:interest rate
    :param T:time to maturity
    :param price:theoretical price under BS formula
    :param q:continuous return rate on the underlying
    :param priceTolerance:criterion to stop the process
    :param method:judgement to use bisect method or newton method
    :return:implied volatility and iteration
    '''

    sigma=init #np.random.random()
    results=[]


    def f(x):
        return bsformula(callput,S0,K,r,T,x,q)[0]-price

    if method=='bisect':
        results=bisect(0,f,None,[0.001,1.0],[priceTolerance,priceTolerance],max_iter)
  
    else:
        def f_prime(x):
             return bsformula(callput,S0,K,r,T,x,q)[2]

        results=newton(f,f_prime,sigma,priceTolerance,max_iter)
    return results


if __name__=="__main__":
    
    results = bsimpvol(1,50.0,50.0,0.01,1.0,8.0,0,0.01,'bisect')
    print(results)
    
    results = bsimpvol(1,50.0,50.0,0.01,1.0,8.0,0,0.01,'newton')
    print(results)
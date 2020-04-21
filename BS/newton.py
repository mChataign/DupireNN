__author__ = 'dixon'

import numpy as np

def newton(f,f_prime,start=None,tol=0.01,maxiter=100):

    n=1
    results=[]
    if start==None:
       start=np.random.random()

    while n<=maxiter:
        start1=start-f(start)/f_prime(start)
        if abs(start1-start)<tol:
            return results
        else:
            results.append(start1)
            start=start1
            n=n+1

    return results

if __name__=="__main__":
    y=lambda start: start**3+2*start**2-5
    dy=lambda start: 3*start**2+4*start
    results=newton(y,dy,5.0,0.001,100)
    print(results)
__author__ = 'dixon'

import numpy as np

def bisect(target,targetfunction,start=None,bounds=None,tols=[0.01,0.01],maxiter=100):

    '''
:param target:target value for the function,supposed to be 0
:param targetfunction:the function to be executed
:param start:the x-value to determine bounds
:param bounds:the bounds of the range to be conducted
:param tols:the criterion to stop the process
:param maxiter:the iteration to execute
:return:x-values that tested, x-value under tolerance
'''

    results = []



    if bounds != None:
        a=bounds[0]
        b=bounds[1]
    else:
        if start==None:
           start=np.random.random()

        n=0
        a=start+2**n
        b=start-2**n

        while targetfunction(a)*targetfunction(b)>0:

            a=start+2**n
            b=start-2**n

            n=n+1

            if n==maxiter:
                raise ValueError('Error: impossible to find the target')

    i = 0
    while (i < maxiter and targetfunction(a)*targetfunction(b)<0):
         c=(a+b)*0.5
         if abs(targetfunction(c)-target)<tols[0] or abs(a-b)*0.5<tols[1]:
             results.append(c)
             break

         elif targetfunction(c)<target:
             results.append(c)
             a=c
         else:
             results.append(c)
             b=c

         i = i +1


    if i == maxiter:
         raise ValueError('Error: max number of iterations reached')

    return np.array(results)

if __name__=="__main__":
    try:
       y = lambda x: x**3 + 2*x**2 - 5
       results=bisect(0.0, y, None, [-5, 5], [0.00001, 0.00001], 100)
       print(results)

    except ValueError as e:
       print(e.args())

'''

University of Santo Tomas
Faculty of Engineering
Electronics Engineering Department
First Term, AY 2019-2020

Machine Problem
ECE2112: Advanced Computer Programming and Algorithms

Aaron Zabala & Marvin Wong
2ECE-A

For n = 0:199, given the user-input x(n), determine y(n) if

       {-1.5x(n) + 2x(n+1) - 0.5x(n+2), n=0
y(n) = {0.5x(n+1)-0.5x(n-1), 0<n<198
       {1.5x(n) - 2x(n-1) + 0.5x(n-2), n=199

Superimpose the graphs of x(n) and of y(n) with different line colors in one 
figure window. Do not forget to put legends.

'''

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,199,200)

def x_of_n(x):
    
    y = np.zeros(200)
    
    for m in n:
        
        m = int(m)
        
        if m==0:
            y[m] = -1.5*x[m] + 2*x[m+1] - 0.5*x[m+2]
            
        elif m>0 and m<=198:
            y[m] = 0.5*x[m+1] - 0.5*x[m-1]
            
        elif m==199:
            y[m] = 1.5*x[m] - 2*x[m-1] + 0.5*x[m-2]
        
    plt.plot(n, x, label = 'Value of x(n)')
    plt.plot(n, y, label = 'Value of y(n)')
    plt.legend(frameon = True, loc = 'upper right')
    plt.show()
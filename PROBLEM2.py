'''

University of Santo Tomas
Faculty of Engineering
Electronics Engineering Department
First Term, AY 2019-2020

Machine Problem
ECE2112: Advanced Computer Programming and Algorithms

Marvin Dale Wong & Aaron Vincent Zabala
2ECE-A

Write a program that accepts as input three points (x,y) lying on a circle in 
a 2-dimensional Cartesian plane. The program must return the following 
parameters of the circle on which the three points lie:
    
    - center(h,k);
    - radius r;
    - vector [D, E, F] where D, E, and F are the coefficients in the general 
    equations of a circle x^2 + y^2 + Dx + Ey + F = 0;

Recall from your analytic geometry/pre-calculus class that the standard and 
general equations, respectively, are given as

(x−h)^2 + (y-k)^2 = r^2
x^2 + y^2 + Dx + Ey + F = 0

Hint: An easier way to solve this is to form a system of equations solving D, 
E, and F. Once, D, E, and F are solved, one can determine the general form. 
From the general form, competing the square can be applied to transform the 
general equation to the standard form to determine the center and the radius 
of the circle.

'''

import numpy as np

def circle(x1,y1,x2,y2,x3,y3):
    
    import math
    
    xy1 = x1**2 + y1**2
    xy2 = x2**2 + y2**2
    xy3 = x3**2 + y3**2
    
    # solving for the vector [D, E, F]
    A = np.array([(x1, y1, 1), (x2, y2, 1), (x3, y3, 1)])
    D = -np.array([(xy1, y1, 1), (xy2,y2, 1), (xy3, y3, 1)])
    E = np.array([(xy1, x1, 1), (xy2,x2, 1), (xy3, x3, 1)])
    F = -np.array([(xy1, x1, y1), (xy2,x2, y2), (xy3, x3, y3)])
    
    detA = round(np.linalg.det(A))
    detD = round(np.linalg.det(D))
    detE = round(np.linalg.det(E))
    detF = round(np.linalg.det(F))
    
    valueofD = detD/detA
    valueofE = detE/detA
    valueofF = detF/detA
    
    rnd_valueofD = valueofD.astype(int)
    rnd_valueofE = valueofE.astype(int)
    rnd_valueofF = valueofF.astype(int)
    
    # solving for h and k
    h = -detD/(2*detA)
    k = -detE/(2*detA)
    
    arnd_h = h.astype(int)
    arnd_k = k.astype(int)
    
    # solving for r
    r = math.sqrt((h - x1)**2 + (k - y1)**2)
    arnd_r = np.around(r, decimals = 2)
    
    print('\n')
    print('Parameters of the Circle on which the three points lie:')
    print('\n')
    print('The center of the circle is (', arnd_h,',', arnd_k,').')
    print('The radius of the circle is r = ', arnd_r)
    print('Vector [D, E, F]: [', rnd_valueofD,',', rnd_valueofE,',', rnd_valueofF,']')
    print('\n')
    
    # Standard and General Equations
    print('Standard Equation of the Circle: ')
    print('( x -', arnd_h, ')^2 + ( y - ', arnd_k,')^2')
    print('\n')
    print('General Equation of the Circle: ')
    print('x^2 + y^2 +', rnd_valueofD, 'x +', rnd_valueofE, 'y +', rnd_valueofF, '= 0')
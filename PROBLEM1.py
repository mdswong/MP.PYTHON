'''

University of Santo Tomas
Faculty of Engineering
Electronics Engineering Department
First Term, AY 2019-2020

Machine Problem
ECE2112: Advanced Computer Programming and Algorithms

Marvin Dale Wong & Aaron Vincent Zabala
2ECE-A

Write a program that will implement the function

f(n) = {(n^2)−7, n<9
       {f(n−10), n≥10

where n is an integer and n ≥ 0. Using your program, graph f(n) from n = 0 to 
n = 99 using stem(). Provided with figures, describe and comment on the graph 
f(n).

'''

import matplotlib.pyplot as plt

def StemFunction(n):
    
    result = (n**2)-7
    
    if (n<=9):
        return result
    return StemFunction(n-10)

x = [] # for storing x values
y = [] # for storing y values

# storing
for i in list(range(100)):
    x.append(i)
    y.append(StemFunction(i))

# plotting f(n) from n = 0 to n = 99 using stem()
plt.stem(x,y)
plt.title('Graph of function(n)')
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.show()
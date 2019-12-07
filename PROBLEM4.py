'''

University of Santo Tomas
Faculty of Engineering
Electronics Engineering Department
First Term, AY 2019-2020

Machine Problem
ECE2112: Advanced Computer Programming and Algorithms

Aaron Zabala & Marvin Wong
2ECE-A

Create a program that plots the trajectory, from the initial height to the 
ground, of a projectile accelerating both in the horizontal and vertical 
directions. The program must accept the following as inputs:

1. initial height of the projectile above the ground in meters
2. magnitude of velocity in m/s
3. the angle in degrees with respect to the +x-axis at which the projectile 
   is fired
4. x-component of the acceleration
5. y-component of the acceleration

The program must also have error detection for the instance the user inputs 
zero acceleration for the vertical component. (If the vertical acceleration 
is zero, then there would be no free fall.) You may use the error command.

Do not forget to put axis labels and grids on your plot. No restrictions on 
the line style and width. Do not use white for the line color.

'''

import matplotlib.pyplot as plt
import math

def projectilemotion(s0,v0,theta0,ax,ay):
   
   if ay==0:
       print("Error! Vertical acceleration (ay) cannot be 0.")
       return  

   x_values = [] # for storing x axis values
   y_values = [] # for storing y axis values
   
   # from trigonometry
   v0x = v0*math.cos(theta0*(3.141/180))
   v0y = v0*math.sin(theta0*(3.141/180))
   
   # initializing parameters
   t = 0
   x = 0
   y = s0 # initial height
   delta = 0.0001 # granularity in time in seconds
   
   # storing
   x_values.append(x)
   y_values.append(y)
   
   # performing simulation
   while(True):
       
       # incrementing time
       t = t+delta
       
       # calculate next time instants parameters
       x = v0x*t + (0.5)*ax*(t*t)
       y = v0y*t + (0.5)*ay*(t*t) + s0
       
       # storing
       x_values.append(x)
       y_values.append(y)
       
       # simulation breaking condition
       if y < delta:
           break
       
   # plotting the result of the simulation
   plt.plot(x_values,y_values)  
   plt.xlabel('x axis')
   plt.ylabel('y axis')
   plt.title('Simulation of Projectile Motion') 
   plt.show()
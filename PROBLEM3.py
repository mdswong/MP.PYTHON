'''
University of Santo Tomas
Faculty of Engineering
Electronics Engineering Department
First Term, AY 2019-2020

Machine Problem
ECE2112: Advanced Computer Programming and Algorithms

Marvin Dale Wong & Aaron Vincent Zabala
2ECE-A

Given a certain set of experimental points (xi, yi), regardless of how many, 
the program must be able to return the coefficients of the polynomial f(x) 
that would best approximate the data according to the least-norm error vector 
e(x) in Experiment 4, i.e.

e(xi) = yi − f(xi)

Limit your polynomials from the 1st degree up to the 10th degree. The set of 
points should be input in the form of an n × 2 matrix where 𝑛 is the number of 
experimental data. Note that the data points should only be the user input, 
and not n.

'''

import numpy as np

print('\n')
print("[[xi],[yi]]: ")
Points=eval(input())

X=np.array([Points[0]]).flatten()
Y=np.array([Points[1]]).flatten()

Poly_1st=np.polyfit(X, Y, 1)
Xi1=X
Val_1st=np.polyval(Poly_1st, Xi1)
Error_1st=np.linalg.norm(Y-Val_1st)

Poly_2nd=np.polyfit(X, Y, 2)
Xi2=X
Val_2nd=np.polyval(Poly_2nd, Xi2)
Error_2nd=np.linalg.norm(Y-Val_2nd)

Poly_3rd=np.polyfit(X, Y, 3)
Xi3=X
Val_3rd=np.polyval(Poly_3rd, Xi3)
Error_3rd=np.linalg.norm(Y-Val_3rd)

Poly_4th=np.polyfit(X, Y, 4)
Xi4=X
Val_4th=np.polyval(Poly_4th, Xi4)
Error_4th=np.linalg.norm(Y-Val_4th)

Poly_5th=np.polyfit(X, Y, 5)
Xi5=X
Val_5th=np.polyval(Poly_5th, Xi5)
Error_5th=np.linalg.norm(Y-Val_5th)

Poly_6th=np.polyfit(X, Y, 6)
Xi6=X
Val_6th=np.polyval(Poly_6th, Xi6)
Error_6th=np.linalg.norm(Y-Val_6th)

Poly_7th=np.polyfit(X, Y, 7)
Xi7=X
Val_7th=np.polyval(Poly_7th, Xi7)
Error_7th=np.linalg.norm(Y-Val_7th)

Poly_8th=np.polyfit(X, Y, 8)
Xi8=X
Val_8th=np.polyval(Poly_8th, Xi8)
Error_8th=np.linalg.norm(Y-Val_8th)

Poly_9th=np.polyfit(X, Y, 9)
Xi9=X
Val_9th=np.polyval(Poly_9th, Xi9)
Error_9th=np.linalg.norm(Y-Val_9th)

Poly_10th=np.polyfit(X, Y, 10)
Xi10=X
Val_10th=np.polyval(Poly_10th, Xi10)
Error_10th=np.linalg.norm(Y-Val_10th)

VectorNorm = np.min(np.array([Error_1st,Error_2nd,Error_3rd,Error_4th, 
                              Error_5th,Error_6th,Error_7th,Error_8th, 
                              Error_9th,Error_10th]))

print ('\n')

if (VectorNorm==Error_1st):
    print("Coefficients of the Polynomial: \n")
    print(Poly_1st)    
elif (VectorNorm==Error_2nd):
    print("Coefficients of the Polynomial: \n")
    print(Poly_2nd)    
elif (VectorNorm==Error_3rd):
    print("Coefficients of the Polynomial: \n")
    print(Poly_3rd)    
elif (VectorNorm==Error_4th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_4th)
elif (VectorNorm==Error_5th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_5th)    
elif (VectorNorm==Error_6th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_6th)
elif (VectorNorm==Error_7th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_7th)
elif (VectorNorm==Error_8th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_8th)
elif (VectorNorm==Error_9th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_9th)
elif (VectorNorm==Error_10th):
    print("Coefficients of the Polynomial: \n")
    print(Poly_10th)
    
print('\n')
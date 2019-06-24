#Python Program to solve the Quadratic Equation.

#The Quadratic Equation is AX**2+BX+C=0

# To the Quadratic equation the Co-Efficients X of various powers are applied in the formula

#X = -B(+or-)(sqrt(B**2-4AC))/2A

#Take the coefficients of X from the Users.

import math

A=input("Enter the Co-efficient of X**2: ")

B=input("Enter the Co-efficient of X: ")

C=input("Enter the Constant: ")

# Solution 1

X1= -B-(B**2-4*A*C)**(1/2)/2*A

# Solution 2

X2= -B+(B**2-4*A*C)**(1/2)/2*A

print ("Solution 1",X1)

print ("Solutuin 2",X2)




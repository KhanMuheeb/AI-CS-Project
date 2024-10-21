import cmath
a = int(input("Enter Coefficient of x"))
b = int(input("Enter Coefficient of x"))
c = int(input("Enter any Constant"))
D = (b**2)-(4*a*c)
r1 = (-b + cmath.sqrt(D))/(2*a)
r2 = (-b - cmath.sqrt (D))/(2*a)
print("The Roots of the Quadratic Equations are",r1,"and",r2)

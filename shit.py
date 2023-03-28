from sympy import *

x = Symbol('x')
y = Symbol('y')
eq1 = Eq(2*x+3*y,5)
eq2 = Eq(5*x+11*y,10,x>10)
solution = solve([eq1, eq2], [x,y])
print(solution)

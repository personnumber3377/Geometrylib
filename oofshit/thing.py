import numpy as np
import matplotlib.pyplot as plt

from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
f = simplify(x**2)
f_comma = diff(f, x)
eq = Eq(f_comma, 0)
an_sol = solve(eq)

print(an_sol)


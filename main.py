from sympy import *
from IPython.display import display, Math
import pandas as pd


x, y, z, a, b, m, n = symbols("x y z a b m n")

f = simplify(3*x**2-4*x*y+y**2-5*x*y+6*x**2-3*y**2-6*y**2-8*x*y-9*x**2)
g = simplify((3*x**2)*(2*x**2))
h = div((x**2-x-6),(x+3))
h = diff(sin(x), x)
#pprint(latex(f))
#pprint(f)
pprint(h)
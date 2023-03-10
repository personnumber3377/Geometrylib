

import numpy as np
import sympy
from sympy.parsing.sympy_parser import parse_expr
import sys
from sympy.solvers import solve
from sympy import Symbol
from sympy import Eq



global_things = []

class var:
	def __init__(self, value):
		if value ==


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def warn(string):
	print(bcolors.WARNING + "Warning: " + str(string) + bcolors.ENDC)
	return


class point:
	def __init__(self, x=None, y=None, vector=None):
		if vector != None:
			self.vector = vector
			self.x=vector.item(0)
			self.y=vector.item(1)
		elif x==None and y==None:
			warn("Warning. Uninitialized point.")
			return
		else:
			self.vector = np.array([[x],[y]])
			self.x = x
			self.y = y

	
		



class line:
	def __init__(self,a="unknown",b="unknown",c="unknown"):


		# a*x+b*x=c
		self.debug=False

		self.a = a
		self.b = b
		self.c = c

	def set_values_point_line(point, line_vector):
		
		# this basically gets the appropriate values for a,b,c when the line goes through point and steps from there to line_vector from point

		# basically assume that c=1

		self.c = 1
		
		xv = line_vector.item(0)
		xy=line_vector.item(1)
		
		x0 = point.item(0)
		x1 = point.item(1)

		# a = -(yv/(x0*yv-xv*y0))
		# b = xv/(x0*yv-xv*y0)

		self.a = -(yv/(x0*yv-xv*y0))
		self.b = xv/(x0*yv-xv*y0)

		self.c = float(self.c)
		self.a = float(self.a)
		self.b = float(self.b)
		return;

	def set_values_two_points(point1, point2):

		# get vector from point1 to point2

		from1to2 = -1*point1+point2

		self.set_values_point_line(point1, from1to2)

	def get_equation(self):
		# returns the line in the a*x+b*y+c = 0 format
		equation = "("+str(self.a)+")*x+("+str(self.b)+")*y+("+str(self.c)+")"
		right_side = "0"
		if self.debug:
			print(equation)
		equation_left_side = parse_expr(equation)
		print("oof")
		equation_right_side = parse_expr(right_side)
		print("oof22")
		#return parse_expr(equation_left_side),parse_expr(equation_right_side) 
		return Eq(equation_left_side, equation_right_side)




def debug_tests():

	# self,a=0,b=0,c=0

	line_object = line(a=10, b=4, c=3)
	line_object.debug = True

	print(line_object.get_equation())
	x = Symbol('x')
	print("thing")
	#print(line_object.get_equation()[0])
	print("thingooff")
	print(solve(line_object.get_equation()), x)

	return 0








if __name__=="__main__":

	if sys.argv[-1] == "--test":
		debug_tests()
		exit(0)

	


		





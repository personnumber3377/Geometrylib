

import numpy as np
import sympy
from sympy.parsing.sympy_parser import parse_expr
import sys
from sympy.solvers import solve
from sympy import Symbol
from sympy import Eq
from sympy import *


global_things = []




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
		count = 0
		while str(count) in global_things:
			count += 1
		self.var_count = count


		


		self.a = Symbol('a'+str(count))
		self.b = Symbol('b'+str(count))
		self.c = Symbol('c'+str(count))

		self.x = Symbol('x'+str(count))
		self.y = Symbol('y'+str(count))

		self.a = a
		self.b = b
		self.c = c


	def set_values_point_line(point, line_vector):
		
		# this basically gets the appropriate values for a,b,c when the line goes through point and steps from there to line_vector from point

		# basically assume that c=1

		self.c_val = 1
		'''
		xv = line_vector.item(0)
		xy=line_vector.item(1)
		
		x0 = point.item(0)
		x1 = point.item(1)
		'''

		xv = line_vector[0]
		xy=line_vector[1]
		
		x0 = point[0]
		x1 = point[1]

		# a = -(yv/(x0*yv-xv*y0))
		# b = xv/(x0*yv-xv*y0)

		self.a = simplify(-(yv/(x0*yv-xv*y0)))
		self.b = simplify(xv/(x0*yv-xv*y0))

		#self.c = float(self.c)
		#self.a = float(self.a)
		#self.b = float(self.b)
		return;

	def set_values_two_points(point1, point2):

		# get vector from point1 to point2

		from1to2 = -1*point1+point2

		self.set_values_point_line(point1, from1to2)

	def get_equations(self):
		# returns the line in the a*x+b*y+c = 0 format
		equation = "("+str(self.a)+")*"+str(self.x)+"+("+str(self.b)+")*"+str(self.y)+"+("+str(self.c)+")"
		right_side = "0"
		if self.debug:
			print(equation)
		equation_left_side = parse_expr(equation)
		print("oof")
		equation_right_side = parse_expr(right_side)
		print("oof22")
		#return parse_expr(equation_left_side),parse_expr(equation_right_side) 
		return [Eq(equation_left_side, equation_right_side)]





def intersection(object1, object2):

	# object is assumed to have the get_equation method which returns the equation which describes the object (like a line is a*x+b*y+c=0 )

	equations1 = object1.get_equations()

	equations2 = object2.get_equations()



	results = []

	for equation1, equation2 in zip(equations1, equations2):
		



	temp_var_x = Symbol("tempvarx")
	temp_var_y = Symbol("tempvary")

	substitute_first = {object1.x:temp_var_x, object1.y:temp_var_y}
	substitute_second = {object2.x:temp_var_x, object2.y:temp_var_y}
	print("substitute_first : " + str(substitute_first))

	equation1 = equation1.subs(substitute_first)

	equation2 = equation2.subs(substitute_second)

	print("-----------")
	print(equation1)
	print(equation2)
	print("-----------")
	print(temp_var_x)
	print(temp_var_y)

	result = sympy.solve((equation1, equation2), (temp_var_x, temp_var_y))

	print("result: "+str(result))

	return result




def debug_tests():

	# self,a=0,b=0,c=0

	line_object = line(a=10, b=4, c=3)
	line_object.debug = True
	result = line_object.get_equation()
	#print("here is the result: "+str(result))
	#x = Symbol('x')
	#print("thing")
	#print(line_object.get_equation()[0])
	#print("thingooff")
	#print(solve(line_object.get_equation(), line_object.y))
	line_object2 = line(a=11, b=4, c=3)
	intersection(line_object, line_object2)


	return 0








if __name__=="__main__":

	if sys.argv[-1] == "--test":
		debug_tests()
		exit(0)

	


		





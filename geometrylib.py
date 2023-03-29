

import numpy as np
import sympy
from sympy.parsing.sympy_parser import parse_expr
import sys
from sympy.solvers import solve
#from sympy import Symbol
#from sympy import Eq
from sympy import *
from outcolors import *
import readline
from sympy.calculus.util import *
import random
import os


global_things = []
global_objects = []

user_defined_variables = {}
# commands = ["line", "intersect", "help", "quit", "objects", "circle", "point", "mindistobjdot", "maxdistobjdot", "mindistpointobjdot", "maxdistpointobjdot", "integrate"]
commands = ["line", "intersect", "help", "quit", "objects", "circle", "point", "mindistobjdot", "maxdistobjdot", "mindistpointobjdot", "maxdistpointobjdot", "integrate", "area_between_intersections"]

object_types = ["line", "circle", "point"] # these are the types for when the argument to a method of an object are themselves objects. If not, then they are assumed to be constant values or expressions





'''


Todo list:

- Add a polygon object or atleast a triangle.
- Way to compute angles and add an angle object. (Basically use stuff like the law of sines to compute them etc etc.)
- 3D-objects.
- Add a line to a point which has a certain angle.
- Default arguments. (if an argument is not given to a function then it assumes that a certain argument has a certain value instead of erroring out.)

'''



VERSION_STR="1.0"

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

def fail(string):
	print_col(bcolors.FAIL, "Error: " + str(string))
	return



class point:

	def __init__(self, *arguments):

		self.debug = False
		self.default_arguments = {"x":"unknown", "y":"unknown", "name":"point"}

		self.methods = [self.set_point_to_values, self.get_equations]
		self.method_strings = ["set_point_to_values", "get_equations"]
		self.method_arg_types = [["float", "float"], []]
		self.num_args = [2, 0]
		self.parameters = ["x", "y"]

		common_arg_stuff(self, *arguments)


	def run_method_on_self(self,method_string, command, attribute_name): # attribute_name actually does not get even used :=)
		# global_objects
		print("bullshitrgregreg")
		print("command: "+str(command))
		command_string = command
		arguments = command_string.split(" ")[1:]

		if method_string not in self.method_strings:
			fail("Invalid method : "+str(method_string))
			return 1

		# self.method_arg_types = [["point", "point"], ["point", "point"], []]
		correct_method_index = self.method_strings.index(method_string)
		correct_method = self.methods[correct_method_index]
		arguments_for_method = []
		
		#for i in range(self.num_args[self.num_args.index(correct_method_index)]):
		for i in range(self.num_args[correct_method_index]):
			# get the arguments
			print("self.method_arg_types : " + str(self.method_arg_types))
			if self.method_arg_types[correct_method_index][i] in object_types:
				object_name = arguments[i]
				object_itself = get_object_by_name(object_name)

				arguments_for_method.append(object_itself)
			else:
				# assumed to be a constant:
				arguments_for_method.append(float(arguments[i]))

		# call the method with the arguments:

		return_value = correct_method(*arguments_for_method)
		

		return return_value

	def set_point_to_values(self, x_in, y_in):
		print("SHITSHITSHIT")
		#self.x = self.x.subs({"x":x_in})
		#self.y = self.y.subs({"y":y_in})
		
		self.x = x_in
		self.y = y_in

		print("self.x == "+str(self.x))
		print("self.y == "+str(self.y))

		print("x_in: "+str(x_in))
		print("y_in: "+str(y_in))

		return 0


	def set_property_on_self(self,selected_property, value):


		# thanks to https://stackoverflow.com/questions/2612610/how-to-access-get-or-set-object-attribute-given-string-corresponding-to-name-o
		# stackoverflow username @pratik-deoghare
		# setattr(t, 'attr1', 21)
		print("selected_property: "+str(selected_property))
		print("value: "+str(value))
		setattr(self, selected_property, value)
		return 0


	def replace_equation_shit(self):
		return ["x="+str(self.x), "y="+str(self.y)]

	def get_equations(self):

		




		left_side_1 = "x"
		left_side_2 = "y"
		right_side_1 = self.x
		right_side_2 = self.y
			
		equation_stuff = self.replace_equation_shit()

		paskaoof = []

		equation1 = equation_stuff[0]
		equation2 = equation_stuff[1]

		left_side_1 = equation1[:equation1.index("=")]
		right_side_1 = equation1[equation1.index("=")+1:]

		left_side_2 = equation2[:equation2.index("=")]
		right_side_2 = equation2[equation2.index("=")+1:]


		print("left_side_1 : "+str(left_side_1))

		print("right_side_1 : "+str(right_side_1))

		

		first_equation = Eq(parse_expr(left_side_1), parse_expr(str(right_side_1)))
		second_equation = Eq(parse_expr(left_side_2), parse_expr(str(right_side_2)))
		
		print("first_equation : "+str(first_equation))
		print("second_equation : "+str(second_equation))
		
		#second_equation = str(left_side_2)+"="+str(right_side_2)

		#print("first_equation : "+str(first_equation))

		equation_list = [first_equation, second_equation]
		#equation_list = [Eq(left_side_1, self.x), Eq(left_side_2, self.y)]
		return equation_list
	def __str__(self):
		
		return '''=======================\nType: point\nx = {}\ny = {}\nname = {}\n=======================\n'''.format(self.x, self.y, self.name)

def get_ranges(x0,y0,x1,y1):

	# get the range of numbers:
	
	output = []


	x0 = str(x0)
	y0 = str(y0)
	x1 = str(x1)
	y1 = str(y1)


	print("=======================\n\n")
	print("oofthingaaaa")
	print("x0: "+x0)
	print("y0: "+y0)
	print("x1: "+x1)
	print("y1: "+y1)

	print("=======================\n\n")



	if x0 > x1:
		output.append("x>="+str(x1))
		output.append("x<="+str(x0))
	else:
		output.append("x<="+str(x1))
		output.append("x>="+str(x0))

	if y0 > y1:
		output.append("y>="+str(y1))
		output.append("y<="+str(y0))
	else:
		output.append("y<="+str(y1))
		output.append("y>="+str(y0))
	print("Output: "+str(output))
	return output

class triangle:
	def __init__(self, *arguments):


		self.debug = False
		
		# {"x":"unknown", "y":"unknown", "name":"point"}

		self.default_arguments = {"x0":0, "y0":0, "x1":0, "y1":0, "x2":0, "y2":0, "name":"triangle"} # list of tuples which are all 0,0

		self.parameters = ["x0", "y0", "x1", "y1", "x2", "y2"]
		
		self.method_strings = ["set_lines_from_points"]
		self.methods = [self.set_lines_from_points]

		self.num_args = [3]
		self.method_arg_types = [["point", "point", "point"]]

		common_arg_stuff(self, *arguments)


		'''
				self.debug = False
		self.default_arguments = {"x":"unknown", "y":"unknown", "name":"point"}

		self.methods = [self.set_point_to_values, self.get_equations]
		self.method_strings = ["set_point_to_values", "get_equations"]
		self.method_arg_types = [["float", "float"], []]
		self.num_args = [2, 0]
		self.parameters = ["x", "y"]

		common_arg_stuff(self, *arguments)

		'''

	def run_method_on_self(self,method_string, command, attribute_name): # attribute_name actually does not get even used :=)
		# global_objects
		
		command_string = command
		arguments = command_string.split(" ")[1:]

		if method_string not in self.method_strings:
			fail("Invalid method : "+str(method_string))
			return 1

		# self.method_arg_types = [["point", "point"], ["point", "point"], []]
		correct_method_index = self.method_strings.index(method_string)
		correct_method = self.methods[correct_method_index]
		arguments_for_method = []
		
		#for i in range(self.num_args[self.num_args.index(correct_method_index)]):
		for i in range(self.num_args[correct_method_index]):
			# get the arguments
			print("self.method_arg_types : " + str(self.method_arg_types))
			if self.method_arg_types[correct_method_index][i] in object_types:
				object_name = arguments[i]
				object_itself = get_object_by_name(object_name)

				arguments_for_method.append(object_itself)
			else:
				# assumed to be a constant:
				arguments_for_method.append(float(arguments[i]))

		# call the method with the arguments:

		return_value = correct_method(*arguments_for_method)
		

		return return_value

	'''
	def get_range(self,x0,y0,x1,y1):

		# spaghetti code

		# get the range of numbers:
		
		output = []

		if x0 > x1:
			output.append("x>="+str(x1))
			output.append("x<="+str(x0))
		else:
			output.append("x<="+str(x1))
			output.append("x>="+str(x0))

		if y0 > y1:
			output.append("y>="+str(y1))
			output.append("y<="+str(y0))
		else:
			output.append("y<="+str(y1))
			output.append("y>="+str(y0))

		return output


	'''

	def get_line_equation(self,x0,y0,x1,y1):

		# a,b = [[(y0-y1)/(x0*y1-x1*y0),(-x0+x1)/(x0*y1-x1*y0)]]   and c=1

		print("Setting a to this: "+str("(({})-({}))/(({}*{})-({}*{}))".format(str(y0), str(y1), str(x0), str(y1), str(x1), str(y0))))
		a = simplify("(({})-({}))/(({}*{})-({}*{}))".format(str(y0), str(y1), str(x0), str(y1), str(x1), str(y0)))
		b = simplify("(-({})+({}))/(({}*{})-({}*{}))".format(str(x0), str(x1), str(x0), str(y1), str(x1), str(y0)))
		c = "1"
		print("Line-equation thing: "+str("({})*x+({})*y+1=0".format(str(a), str(b))))
		

		print("self.x0 : "+str(self.x0))
		print("self.x0 : "+str(self.y0))
		print("self.x1 : "+str(self.x1))
		print("self.y1 : "+str(self.y1))
		print("self.x2 : "+str(self.x2))
		print("self.y2 : "+str(self.y2))

		return "({})*x+({})*y+1".format(str(a), str(b))



	def get_equations(self):

		# basically just return the list of lines, except that there are constrictions on the answers

		line_equations = [self.get_line_equation(self.x0, self.y0, self.x1, self.y1), self.get_line_equation(self.x0, self.y0, self.x2, self.y2), self.get_line_equation(self.x1, self.y1, self.x2, self.y2)]

		constraints = []

		constraints.append(get_ranges(self.x0, self.y0, self.x1, self.y1))

		constraints.append(get_ranges(self.x0, self.y0, self.x2, self.y2))

		constraints.append(get_ranges(self.x1, self.y1, self.x2, self.y2))

		final_eqs = []

		for i in range(3):

			equation = line_equations[i]
			constraint_thing = constraints[i]

			#final_equation = equation + "," + constraint_thing
			print("Parsing equation: "+str(equation))
			print("resulting thing: "+str(parse_expr(equation)))

			print("constraint_thing: "+str(constraint_thing))

			#print("parse_expr(constraint_thing) == "+str(parse_expr(constraint_thing)))

			final_equation = Eq(parse_expr(equation))
			
			#constraint_stuff = parse_expr(constraint_thing)

			constraint_stuff = [parse_expr(thing) for thing in constraint_thing]

			print("Final equation: "+str(final_equation))
			print("Value of x: "+str(parse_expr('x')))
			
			final_eqs.append([final_equation, constraint_stuff])

		return final_eqs



	def set_property_on_self(self,selected_property, value):


		
		print("selected_property: "+str(selected_property))
		print("value: "+str(value))
		setattr(self, selected_property, value)
		return 0

	def set_lines_from_points(self, point1, point2, point3):

		self.x0 = point1.x
		self.y0 = point1.y

		self.x1 = point2.x
		self.y1 = point2.y

		self.x2 = point3.x
		self.y2 = point3.y





'''

 - Polygon which has X points.




def intersection(object1, object2):

	# object is assumed to have the get_equation method which returns the equation which describes the object (like a line is a*x+b*y+c=0 )
	print("================================================")
	print("object1 : " + str(object1))
	print("object2 : " + str(object2))
	print("object1 : " + str(type(object1)))
	print("object2 : " + str(type(object2)))
	print("================================================")
	equations1 = object1.get_equations()

	equations2 = object2.get_equations()


	all_equations = equations1 + equations2
	print("All equations as a list: "+str(all_equations))


	result = sympy.solve(all_equations, ('x', 'y'))
	print("result: "+str(result))

	return result
'''
# def mindistobjdot(command:str, objects:list):


def polygon_command(command_string: str, objects: list):

	# basically three lines.

	# one point is line1 int line2  second point is line2 int line3  and third is line3 int line1

	arguments = command_string.split(" ")

	lines = arguments[1:]

	line_objects = []

	for line in lines:

		line_objects.append(get_object_by_name(line))





	




	
		

def get_object_by_name(name_str):
	print("name_str: " + str(name_str))
	print(get_names(global_objects))
	count = 0
	obj = global_objects[0]

	print("---------------------------")
	for object_thing in global_objects:
		print(object_thing.name)
	print("---------------------------")

	while obj.name != name_str and count != len(global_objects):
		print("obj.name == " + str(obj.name))
		count += 1
		obj = global_objects[count]

		


	if count == len(global_objects):
		# object by that name does not exist
		fail("Object of name "+str(name_str)+" does not exist.")
		return 1
	return obj



def common_arg_stuff(the_object, *arguments_thing):
	
	count = 0
	print("*arguments_thing : " + str(*arguments_thing))

	default_arguments = the_object.default_arguments
	
	# assume default arguments first, and then replace the overridden arguments afterwards
	final_arguments = default_arguments
	bullshit = str(*arguments_thing)
	print("bullshit: "+str(bullshit))

	# ==============================

	# refer to this: https://stackoverflow.com/questions/17610732/error-dictionary-update-sequence-element-0-has-length-1-2-is-required-on-dj

	#bullshit2 = dict(bullshit)   # this shit wont work, because reasons and spagetti code. We must use the *VERY SAFE* function "eval" :)
	bullshit2 = eval(bullshit)
	
	# ==============================

	print("bullshit: "+str(bullshit2))
	for argument in bullshit2.keys():
		final_arguments[argument] = bullshit2[argument]

	name = final_arguments["name"]
	while str(name)+str(count) in get_names(global_objects):
		count += 1
	if count or name == the_object.default_arguments["name"]:
		the_object.name = str(name)+str(count)
		the_object.var_count = count
	else:
		the_object.name = name
		the_object.var_count = count

	# run through the rest of the arguments and set the appropriate values for each of the parameters for the object:

	# this next loop is here to set the variables of the object to an unknown value. The values (if specified) are set in the later loop.

	for param in the_object.parameters:
		# self.a = Symbol('a'+str(count))
		print("the_object.name == "+str(the_object.name))
		print("setting parameter "+str(param)+" to this: "+str(str(param)+str(count)))
		setattr(the_object, str(param), Symbol(str(param)+str(count)))
		#setattr(the_object, str(Symbol(str(param)+str(count))), str(param))

	# if a value is mentioned specifically,then set the value of the variable to that.

	for param in the_object.parameters:
		if param in final_arguments:
			# the parameter is specified in arguments
			if final_arguments[param] != "unknown": # the variable is actually specified
				# self.a = Symbol('a'+str(count))
				setattr(the_object, str(param), final_arguments[param])
		#else:
		#	setattr(the_object, str(param), final_arguments[param])  # this was done in the earlier loop
	print("Names of global objects at the end of common_arg_stuff: " + str(get_names(global_objects)))

class line:
	#def __init__(self,a="unknown",b="unknown",c="unknown", name="line"):
	def __init__(self,*arguments):

		#name_str = name+str(self.var_count)

		# a*x+b*x=c
		self.debug=False
		self.default_arguments = {"a":"unknown", "b":"unknown", "c":"unknown", "name":"line"}

		self.methods = [self.set_values_point_line, self.set_values_two_points, self.get_equations, self.noop]
		self.method_strings = ["set_values_point_line", "set_values_two_points", "get_equations", "noop"] # the noop is just for sanity testing
		self.method_arg_types = [["point", "point"], ["point", "point"], [], []]

		self.num_args = [2,2,0,0]  # these are strict number of arguments for each method
		self.parameters = ["a","b","c","x","y"]


		common_arg_stuff(self, *arguments)
		'''
		count = 0
		while str(name)+str(count) in get_names(global_objects):
			count += 1
		if count:

			self.name = str(name)+str(count)
			self.var_count = count
		else:
			self.name = name # there were no duplicates so just set the name as name
			self.var_count = count


		if name == "line":
			
			print("self.var_count : " + str(self.var_count))
			print("name: " + str(name))

			name_str = name+str(self.var_count)
			print("name_str : " + str(name_str))

			self.name = name_str
		else:
			self.name = name


		


		self.a = Symbol('a'+str(count))
		self.b = Symbol('b'+str(count))
		self.c = Symbol('c'+str(count))

		self.x = Symbol('x'+str(count))
		self.y = Symbol('y'+str(count))
		if a != "unknown":
			self.a = a
		if b != "unknown":
			self.b = b
		if c != "unknown":
			self.c = c

		'''

	def noop(self):

		return 0

	def set_values_point_line(point, line_vector):
		
		# this basically gets the appropriate values for a,b,c when the line goes through point and steps from there to line_vector from point

		# basically assume that c=1

		#self.c_val = 1
		self.c = 1
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

	def set_values_two_points(self, point1, point2):

		# get vector from point1 to point2

		#from1to2 = -1*point1+point2


		print("==========================================")


		print("point1.x : "+str(point1.x) + " point1.y: "+str(point1.y))
		print("point2.x : "+str(point2.x) + " point2.y: "+str(point2.y))


		print("==========================================")

		print("-1*point1.x+point2.x == " + str(-1*point1.x+point2.x))
		print("-1*point1.x == " + str(-1*point1.x))
		print("type(point1.x) == "+str(type(point1.x)))


		point1.x = float(point1.x)
		point1.y = float(point1.y)
		point2.x = float(point2.x)
		point2.y = float(point2.y)

		line_vector_x = -1*point1.x+point2.x
		line_vector_y = -1*point1.y+point2.y

		#line_vector_x = point2.x

		#line_vector_y = point2.y

		#self.set_values_point_line(point1, from1to2)


		self.c = 1
		'''
		xv = line_vector.item(0)
		xy=line_vector.item(1)
		
		x0 = point.item(0)
		x1 = point.item(1)
		'''

		xv = line_vector_x
		yv= line_vector_y

		print("xv: "+str(xv))
		print("yv: "+str(yv))
		print("0000000")

		
		x0 = point1.x
		#x1 = point1.y
		y0 = point1.y

		x1 = xv


		# a = -(yv/(x0*yv-xv*y0))
		# b = xv/(x0*yv-xv*y0)


		print("yv: " + str(yv))
		print("x0: "+str(x0))
		print("xv: "+str(xv))
		print("y0: "+str(y0))
		string_oof_1 = "-({}/({}*{}-{}*{}))".format(yv, x0, yv, xv, y0)
		
		# xv/(x0*yv-xv*y0)
		

		print("string_oof_1 : "+str(string_oof_1))


		# (y0-y1)/(x0*y1-x1*y0)

		# -yv/(x0*yv-xv*y0)



		self.a = sympy.simplify(string_oof_1)

		string_oof_2 = "{}/({}*{}-{}*{})".format(xv, x0, yv, xv, y0)
		print("string_oof_2 == "+str(string_oof_2))
		self.b = sympy.simplify(string_oof_2)

		print("self.a =="+str(self.a))
		print("self.b =="+str(self.b))


		#self.a = simplify(-(yv/(x0*yv-xv*y0)))
		#self.b = simplify(xv/(x0*yv-xv*y0))


	def get_equations(self):
		# returns the line in the a*x+b*y+c = 0 format
		#equation = "("+str(self.a)+")*"+str(self.x)+"+("+str(self.b)+")*"+str(self.y)+"+("+str(self.c)+")"
		equation = "("+str(self.a)+")*"+"x"+"+("+str(self.b)+")*"+"y"+"+("+str(self.c)+")"
		right_side = "0"
		if self.debug:
			print(equation)
		equation_left_side = parse_expr(equation)
		print("oof")
		equation_right_side = parse_expr(right_side)
		print("oof22")
		#return parse_expr(equation_left_side),parse_expr(equation_right_side) 
		return [Eq(equation_left_side, equation_right_side)]
	def __str__(self):
		return_string = '''=======================\nType: line\na = {}\nb = {}\nc = {}\nname = {}\n=======================
		'''.format(self.a, self.b, self.c, self.name)
		return return_string

	def run_method_on_self(self,method_string, command, attribute_name): # attribute_name actually does not get even used :=)
		# global_objects
		print("bullshitrgregreg")
		print("command: "+str(command))
		command_string = command
		arguments = command_string.split(" ")[1:]

		if method_string not in self.method_strings:
			fail("Invalid method : "+str(method_string))
			return 1

		# self.method_arg_types = [["point", "point"], ["point", "point"], []]
		correct_method_index = self.method_strings.index(method_string)
		correct_method = self.methods[correct_method_index]
		arguments_for_method = []
		
		#for i in range(self.num_args[self.num_args.index(correct_method_index)]):
		for i in range(self.num_args[correct_method_index]):
			# get the arguments
			print("self.method_arg_types : " + str(self.method_arg_types))
			if self.method_arg_types[correct_method_index][i] in object_types:
				object_name = arguments[i]
				object_itself = get_object_by_name(object_name)

				arguments_for_method.append(object_itself)
			else:
				# assumed to be a constant:
				arguments_for_method.append(float(arguments[i]))

		# call the method with the arguments:

		return_value = correct_method(*arguments_for_method)
		

		return return_value


		'''
		args = command.split(" ")[1:]

		if len(args) != self.num_args[self.num_args.index(method_string)]:
			fail("Invalid number of arguments for method "+str(method_string)+" on object named "+str(self.name))


		if method_string == "set_values_point_line":
			obj1_name = args[0]
			obj2_name = args[1]
			point1 = get_object_by_name(obj1_name)
			point2 = get_object_by_name(obj2_name)
			if point1 == 1 or point2 == 1:
				return 1
			self.set_values_point_line(point1, point2) # the line vector is basically a point

			return 0

		if method_string == "set_values_two_points":
			obj1_name = args[0]
			obj2_name = args[1]
			point1 = get_object_by_name(obj1_name)
			point2 = get_object_by_name(obj2_name)
			if point1 == 1 or point2 == 1:
				return 1
			self.set_values_two_points(point1, point2)
			return 0
		
		'''



	def set_property_on_self(self,selected_property, value):


		# thanks to https://stackoverflow.com/questions/2612610/how-to-access-get-or-set-object-attribute-given-string-corresponding-to-name-o
		# stackoverflow username @pratik-deoghare
		# setattr(t, 'attr1', 21)
		print("selected_property: "+str(selected_property))
		print("value: "+str(value))
		setattr(self, selected_property, value)
		return 0







class circle:

	#def __init__(self, xc="unknown", yc="unknown", r="unknown", name="circle"):
	def __init__(self, *arguments):
		self.debug=False

		


		self.default_arguments = {"xc":"unknown", "yc":"unknown", "r":"unknown", "name":"circle"}
		self.methods = [self.replace_equation_shit, self.get_equations]
		self.method_strings = ["replace_equation_shit", "get_equations"]

		self.num_args = [0,0]
		self.parameters = ["xc", "yc", "r", "x", "y"]

		common_arg_stuff(self, *arguments)

		'''

		self.debug=False
		self.default_arguments = {"a":"unknown", "b":"unknown", "c":"unknown", "name":"line"}

		self.methods = [self.set_values_point_line, self.set_values_two_points, self.get_equations]
		self.method_strings = ["set_values_point_line", "set_values_two_points", "get_equations"]
		self.num_args = [2,2,0]  # these are strict number of arguments for each method
		self.parameters = ["a","b","c","x","y"]
		'''
		


		'''
		count = 0
		while str(count) in global_things:
			count += 1
		self.var_count = count
		if name == "circle":
			name_str = name+str(self.var_count)
			self.name = name_str
		else:
			self.name = name
		


		self.xc = Symbol('xc'+str(count))
		self.yc = Symbol('yc'+str(count))
		self.r = Symbol('r'+str(count))

		self.x = Symbol('x'+str(count))
		self.y = Symbol('y'+str(count))
		if xc != "unknown":
			self.xc = xc
		if yc != "unknown":
			self.yc = yc
		if r != "unknown":
			self.r = r

		'''

	def replace_equation_shit(self):
		print("Circle equation bullshit: ")
		print(str("(("+"x"+")-("+str(self.xc)+"))**2+(("+"y"+")-("+str(self.yc)+"))**2=("+str(self.r)+")**2"))
		return "(("+"x"+")-("+str(self.xc)+"))**2+(("+"y"+")-("+str(self.yc)+"))**2=("+str(self.r)+")**2"
		#return "(("+str(self.x)+")-("+str(self.xc)+"))**2+(("+str(self.y)+")-("+str(self.yc)+"))**2=("+str(self.r)+")**2"



	def get_equations(self):
		# returns the line in the a*x+b*y+c = 0 format
		#equation = "((x)-(xc))**2+((y)-(yc))**2=(r)**2"
		thing = self.replace_equation_shit()

		equation_left_side = thing[:thing.index("=")]
		equation_right_side = thing[thing.index("=")+1:]


		right_side = "0"
		if self.debug:
			print(equation)
		equation_left_side = parse_expr(equation_left_side)
		print("oof")
		equation_right_side = parse_expr(equation_right_side)
		print("oof22")
		#return parse_expr(equation_left_side),parse_expr(equation_right_side) 
		return [Eq(equation_left_side, equation_right_side)]

	def set_property_on_self(self,selected_property, value):


		# thanks to https://stackoverflow.com/questions/2612610/how-to-access-get-or-set-object-attribute-given-string-corresponding-to-name-o
		# stackoverflow username @pratik-deoghare
		# setattr(t, 'attr1', 21)
		print("selected_property: "+str(selected_property))
		print("value: "+str(value))

		print("self.yc : "+str(self.yc))
		setattr(self, selected_property, value)
		return 0
	def __str__(self):
		return_string = '''=======================\nType: circle\nx0 = {}\ny0 = {}\nr = {}\nname = {}\n=======================
		'''.format(self.xc, self.yc, self.r, self.name)
		return return_string




def solve_equation_stuff(object_list, variables):
	equations = []

	for obj in object_list:
		stuff = obj.get_equations()
		
		if isinstance(stuff, list):
			
			# this is for compatibility if the get_equations function returns a list of equations
			equations += stuff
		else:
			equations.append(stuff)
	plain_eqs = True

	for eq in equations:
		if isinstance(eq, list):
			plain_eqs = False
			break

	if plain_eqs:  # they are plain equations without any constraints (aka a line and a point for example)

		all_equations = equations
		print("All equations as a list: "+str(all_equations))


		result = sympy.solve(all_equations, variables)
		print("result: "+str(result))
	
	else:
		result = []

		or_eqs = []
		plain_eqs = []
		print("equations: "+str(equations))
		for eq in equations:
			print
			if not isinstance(eq, list):
				plain_eqs.append(eq)
			else:
				or_eqs.append(eq)

		print("Final plain_eqs: "+str(plain_eqs))

		for or_eq1 in or_eqs:
			restriction_thing = []
			print("or_eq1 : "+str(or_eq1))
			print("plain_eqs: "+str(plain_eqs))

			poplist = []

			for i in range(len(or_eq1)):
				if ">=" in str(or_eq1[i]) or "<=" in str(or_eq1[i]):
					poplist.append(i)
					restriction_thing.append(or_eq1[i])
			
			'''

			# big thanks to https://stackoverflow.com/questions/11303225/how-to-remove-multiple-indexes-from-a-list-at-the-same-time

			indexes = [2, 3, 5]
			for index in sorted(indexes, reverse=True):
				del my_list[index]

			'''

			for index in sorted(poplist, reverse=True):
				del or_eq1[index]




			#result.append(solve(or_eq1+plain_eqs, variables))
			thing = solve(or_eq1+plain_eqs, variables)

			print("Thing stuff: ")
			print("restriction_thing: "+str(restriction_thing))

			print("thing: "+str(thing))
			if isinstance(thing, list):

				# handle the list thing:

				# this is for when there are multiple solution stuff:

				if len(thing) > 1:

					# handle multiple solutions aka check them all sequentially


					print("poopoo")
					#exit(1)

					for sol in thing:

						if isinstance(sol, dict):


							# handle multiple dictionary stuff

							thing = sol

							for restriction in restriction_thing:

								print("current restriction: "+str(restriction))
								print("substitution: "+str(thing))
					
								passing = True
					
								oofthing = restriction[0]
								for restriction_expr in restriction:
						
									oofthing = (restriction_expr).subs(thing)

									if oofthing == False:
										passing = False
										break

								if passing:
									result.append(thing)

						else:


							if len(sol) == 2:
								thing = {"x":sol[0], "y":sol[1]}
							elif len(sol) == 1:
								thing = {"x":sol[0]}
							else:
								fail("Invalid length for solution thing in solve_equation_stuff:")
								print("sol: "+str(sol))
								exit(1)



							# this is basically for when they are tuples or lists.
							# for example in the intersection between a triangle and a circle: [(0.648031893339682, 0.141338648889947), (1.02764378233599, 0.204607297055999)]

							for restriction in restriction_thing:

								print("current restriction: "+str(restriction))
								print("substitution: "+str(thing))
					
								passing = True
					
								oofthing = restriction[0]
								for restriction_expr in restriction:
						
									oofthing = (restriction_expr).subs(thing)

									if oofthing == False:
										passing = False
										break

								if passing:
									result.append(thing)





				else:

					thing = thing[0]

					for restriction in restriction_thing:

						print("current restriction: "+str(restriction))
						print("substitution: "+str(thing))
					
						passing = True
					
						oofthing = restriction[0]
						for restriction_expr in restriction:
						
							oofthing = (oofthing).subs(thing)

							if oofthing == False:
								passing = False
								break

						if passing:
							result.append(thing)


			else:



				for restriction in restriction_thing:

					print("current restriction: "+str(restriction))
					print("substitution: "+str(thing))
					
					passing = True
					
					oofthing = restriction[0]
					for restriction_expr in restriction:
						
						oofthing = (oofthing).subs(thing)

						if oofthing == False:
							passing = False
							break

					if passing:
						result.append(thing)



					#if (restriction).subs(thing):
					#	print("passed this: "+str(restriction)+"  "+str(thing))
					#	result.append(thing)

	return result



def intersection(object1, object2):

	# object is assumed to have the get_equation method which returns the equation which describes the object (like a line is a*x+b*y+c=0 )
	print("================================================")
	print("object1 : " + str(object1))
	print("object2 : " + str(object2))
	print("object1 : " + str(type(object1)))
	print("object2 : " + str(type(object2)))
	print("================================================")


	results = solve_equation_stuff([object1, object2], ('x','y'))
	return results

	
	'''
	equations1 = object1.get_equations()

	equations2 = object2.get_equations()


	plain_eqs = True

	for eq in equations1:
		if isinstance(eq, list):
			plain_eqs = False
			break
	if plain_eqs:
		for eq in equations2:
			if isinstance(eq, list):
				plain_eqs = False
				break

	if plain_eqs:  # they are plain equations without any constraints (aka a line and a point for example)

		all_equations = equations1 + equations2
		print("All equations as a list: "+str(all_equations))


		result = sympy.solve(all_equations, ('x', 'y'))
		print("result: "+str(result))
	else:
		result = []
		plain_eqs = []

		or_eqs1 = []
		or_eqs2 = []

		for eq in equations1:
			if not isinstance(eq, list):
				plain_eqs.append(eq)
			else:
				or_eqs1.append(eq)

		for eq in equations2:
			if not isinstance(eq, list):
				plain_eqs.append(eq)
			else:
				or_eqs2.append(eq)

		if or_eqs1 != [] and or_eqs2 != []:

			for or_eq1 in or_eqs1:
				for or_eq2 in or_eqs2:

					result.append(solve([or_eq1, or_eq2]+plain_eqs), ('x', 'y'))
		elif or_eqs1 != [] and or_eqs2 == []:

			for or_eq1 in or_eqs1:


				result.append(solve([or_eq1]+plain_eqs), ('x', 'y'))

		elif or_eqs1 == [] and or_eqs2 != []:
			for or_eq2 in or_eqs2:
				result.append(solve([or_eq2]+plain_eqs), ('x', 'y'))

		else:
			# We should not reach this point here.
			print("Something went wrong in intersection.")
			exit(1)
	return result
	
	'''



def debug_tests():

	# self,a=0,b=0,c=0

	line_object = line(a=10, b=4, c=3)
	line_object.debug = True
	result = line_object.get_equations()
	#print("here is the result: "+str(result))
	#x = Symbol('x')
	#print("thing")
	#print(line_object.get_equation()[0])
	#print("thingooff")
	#print(solve(line_object.get_equation(), line_object.y))
	#line_object2 = line(a=11, b=4, c=3)
	#thingoof = intersection(line_object, line_object2)
	line_object2 = line(a=11, b=4, c=3)
	
	# x0="unknown", y0="unknown", r="unknown"

	circle_object = circle(xc=1,yc=3, r=10)


	thingoof = intersection(line_object, circle_object)

	print("thingoof: " + str(thingoof))


	return 0




def print_banner():
	print("Welcome to geometrylib "+str(VERSION_STR) + " !")
	print("Type \"help\" for help menu.")

def print_col(color, string):
	print(color + string + bcolors.ENDC)
	return

def set_attributes(object, attributes):

	print("attribute thing: " + str(attributes))


	for attribute_setting in attributes:
		# these arguments are of the format attribute=value

		if "=" not in attribute_setting:
			fail("= character must be in arguments. For example \"line a=1 b=2 c=3\" would create a line of the form 1*x+2*y+c=0 .")
			return 1
		pair = attribute_setting.split("=")
		value = pair[1]   # my_string.replace('.', '', 1).isdigit()
		if value.replace('.', '', 1).isdigit():

			value = float(value)
		
		attribute = pair[0]
		print("poopoopoopoopoopoo")
		print("object.name: "+str(object.name))
		print("attribute: "+str(attribute))
		print("value: "+str(value))
		setattr(object, attribute, value)

def common_object_creation_stuff(arguments, object_name, objects):
	# first create the dictionary from the arguments

	print("arguments: "+str(arguments))
	print("object_name: "+str(object_name))

	arg_dict = dict([thing.split("=")[0], thing.split("=")[1]] for thing in arguments)
	print(arg_dict)

	#  globals()["line"]
	#  thanks to https://stackoverflow.com/questions/3451779/how-to-dynamically-create-an-instance-of-a-class-in-python
	# stackoverflow username @elewinso
	
	if object_name not in globals().keys():
		fail("Class named "+str(object_name)+" does not exist.")
		return 1

	new_object = globals()[object_name](arg_dict) # create the object
	print("global_objects at the start: " + str(get_names(global_objects)))
	print("objects after creation of new_object : " + str(get_names(objects)))
	objects.append(new_object)
	print("gregregregrr")
	print("global_objects at the start: " + str(get_names(global_objects)))
	print("objects after appending new_object: " + str(get_names(objects)))
	#global_objects.append(new_object)
	print("global_objects after appending new_object: " + str(get_names(global_objects)))
	return 0





def line_command(command:str, objects:list):
	
	#new_line = line()

	args = command.split(" ")
	args = args[1:]
	#print("args : "+str(args))
	#if set_attributes(new_line, args):
		#return 1

	# common_object_creation_stuff(arguments, object_name, objects):
	print("objects at the start: "+str(get_names(objects)))

	common_object_creation_stuff(args, "line", objects)
	print("objects at the end: "+str(get_names(objects)))


	print_col(bcolors.OKGREEN, "Created new object.")
	#print(new_line)

	#objects.append(new_line)
	#global_objects.append(new_line)
	return 0





def triangle_command(command:str, objects:list):

	args = command.split(" ")

	args = args[1:]

	common_object_creation_stuff(args, "triangle", objects)

	return 0






def point_command(command:str, objects:list):

	args = command.split(" ")
	args = args[1:]

	common_object_creation_stuff(args, "point", objects)

	return 0




def circle_command(command:str, objects: list):
	args = command.split(" ")
	args = args[1:]
	common_object_creation_stuff(args, "circle", objects)
	print_col(bcolors.OKGREEN, "Created new object.")
	return 0

def help_command(command:str, objects:list):
	print_col(bcolors.OKCYAN, "Current commands: ")
	for comm in commands:
		print_col(bcolors.BOLD, comm)
	return


def get_names(object_list):
	return [obj.name for obj in object_list]



def angle_between_lines(line1, line2):

	result = simplify(parse_expr("Abs(atan(-{}/{})-atan(-{}/{}))".format(str(line1.a), str(line1.b), str(line2.a), str(line2.b))))
	# it is in radians so convert to degrees.

	result *=360
	result /= 2
	result /= 3.14159265358979323846 # pi
	return result



def angle_between_lines_command(command:str, objects:list):

	# returns the angle between two lines
	args = command.split(" ")

	args = args[1:]

	first_line = get_object_by_name(args[0])
	second_line = get_object_by_name(args[1])

	final_result = angle_between_lines(first_line, second_line)

	print_col(bcolors.OKBLUE, "Angle between lines: "+str(final_result)+" == " + str((final_result).evalf()))

	return (final_result).evalf()








def intersection_command(command:str, objects:list):
	args = command.split(" ")
	print("Args : "+str(args))
	args = args[1:]

	
	obj_name1 = args[0]
	obj_name2 = args[1]
	
	print("obj_name1 : "+str(obj_name1))
	print("obj_name2 : "+str(obj_name2))

	obj1 = get_object_by_name(obj_name1)
	obj2 = get_object_by_name(obj_name2)
	print("poopooo")
	print("obj1: "+str(obj1))
	print("obj2: "+str(obj2))
	results = intersection(obj1, obj2)
	if results == []:
		print_col(CYELLOW, "Objects do not intersect.")
	else:
		print_col(CYELLOW, "Objects intersect atleast at one point.")

		print_col(CYELLOW, "Intersections are at points: " + str(results))

	if len(results) == 1:
		print("Results thing: " + str(results))

		point = results[0]

		if isinstance(point, dict):
			return point

		x = point[0]
		y = point[1]
		return {"x":x, "y":y}



	return results




	#obj_names = get_names(objects)

	#print("obj_names : " + str(obj_names))
	# get_object_by_name(name_str)





	return

def invalid_command(command):
	print_col(bcolors.FAIL, "Invalid command: " + str(command))
	return


def quit_command(*args):
	print_col(bcolors.OKGREEN, "Thank you for using geometrylib! See you again soon!")
	exit(0)


def check_common_syntax(command_string, max_args, min_args, all_commands):
	print("fewfeewfewfewf")

	# this part is shared by every command (checks that the correct number of arguments are passed to the function)

	index = all_commands.index(command_string.split(" ")[0])
	
	stuff = command_string.split(" ")
	stuff = stuff[1:]
	max_num_args = max_args[index]
	min_num_args = min_args[index]

	if len(stuff) > max_num_args or len(stuff) < min_num_args:
		if not any("[" in a for a in stuff): # check unpack thing

			fail("Invalid number of arguments: "+str(command_string))
			fail("Min number of arguments is "+str(min_num_args) + " and max number of arguments is "+str(max_num_args) + " .")
			return 1
		else:
			return 0
	return 0


def check_common_syntax_var(command_string, max_args, min_args, all_commands):
	print("fewfeewfewfewf")

	# this part is shared by every command (checks that the correct number of arguments are passed to the function)

	index = all_commands.index(command_string.split(" ")[0])
	
	stuff = command_string.split(" ")
	stuff = stuff[1:] # get rid of the initial command
	max_num_args = max_args[index]
	min_num_args = min_args[index]
	print("stuff == "+str(stuff))
	print("command_string: "+str(command_string))
	if len(stuff) > max_num_args or len(stuff) < min_num_args:
		fail("Invalid number of arguments: "+str(command_string))
		fail("Min number of arguments is "+str(min_num_args) + " and max number of arguments is "+str(max_num_args) + " .")
		return 1
	return 0


def objects_command(command_string, objects):
	print_col(CYELLOW, "Here are all of the objects generated so far: ")
	for obj_name in get_names(objects):
		print_col(CBLUE, obj_name)
	return 0



def run_method(obj, command_string, attribute_name):
	# method = getattr(emp1, 'get_name', None)

	things = command_string.split(" ")
	
	args = things[1:]
	method_str = things[0].split(".")[1] # the method is after the dot

	
	return_value = obj.run_method_on_self(method_str, command_string, attribute_name)
	#function = getattr(obj, method_str, None)
	return return_value


def set_property(obj, command_string):

	things = command_string.split(" ")



	if things[0].count(".") > 1:
		fail("There can only be one dot in command when setting property of an object.")
		return 1

	selected_property = things[0].split(".")[1]

	if things[1] != "=":
		fail("Called set_property with this command \""+str(command_string)+"\" the second operand must be \"=\" . For example myline.name = newname.")
		return 1

	value = things[2]

	obj.set_property_on_self(selected_property, value)

	return










def check_method_command(command_string, all_objects):

	# check if the command is trying to run a method on an object

	obj_dot_method = command_string.split(" ")[0]

	obj_name = obj_dot_method.split(".")[0]
	
	attr_name = obj_dot_method.split(".")[1]

	if obj_name not in get_names(all_objects):
		fail("Object "+str(obj_name)+" does not exist currently.")
		return 1

	correct_index = get_names(all_objects).index(obj_name)
	correct_object = all_objects[correct_index]

	# now check that the attribute exists and that it is callable (aka a function).

	if not hasattr(correct_object, attr_name):
		fail("Object "+str(obj_name)+" does not have the attribute "+str(attr_name))
		return 1
	if not callable(getattr(correct_object, attr_name)):
		# assume that the attribute is just a property
		print("==================================================================================")
		print("Setting property : "+str(attr_name))
		print("On object: "+str(correct_object.name))
		return set_property(correct_object, command_string)   # if returns 1, then failure (for example property does not exist for object) otherwise 0
			
	else:
		# is callable:
		return run_method(correct_object, command_string, attr_name)

def print_object(obj):
	print(obj)
	return str(''.join(str(obj).split("\n")))


def distance_thing(x0,y0,x1,y1):
	print("bullshit ooof :::: "+str("sqrt(({}-{})**2+({}-{})**2)".format(x0,x1,y0,y1)))
	return sympy.simplify("sqrt(({}-{})**2+({}-{})**2)".format(x0,x1,y0,y1))



def distance_min(object, point, maximumthing=False):

	x1 = point.x
	y1 = point.y

	#x0 = 'x'
	#object_equation = object.get_equations()[0]  # support only a thing which has a single equation per object for now :)

	object_equations = object.get_equations()


	print("object_equation : "+str(object_equations))
	#y0 = sympy.solve(object_equations, 'y')  # make it of the form: y=...
	#x_is_var = False

	#solutions = sympy.solve(object_equations,"x,y")
	sol_x = sympy.solve(object_equations,"x")
	sol_y = sympy.solve(object_equations,"y")


	print("sol_x : "+str(sol_x))
	print("sol_y : "+str(sol_y))
	if isinstance(sol_x, list):
		sol_x = sol_x[0]
		sol_y = sol_y[0]


	thing = sol_x
	thing.update(sol_y)
	print("substitution: "+str(thing))
	print("thing: "+str(thing))

	#print("Solutions: "+str(solutions))



	#y0 = y0[list(y0.keys())[0]]

	x = Symbol('x')
	y = Symbol('y')
	distance_function = distance_thing(x,y,x1,y1) # at this point in a case where there are all known values for the objects this should return a function which only has one variable: "x"



	print("distance_function : "+str(distance_function))
	distance_function = distance_function.subs(thing)
	print("Substituted distance function: "+str(distance_function))

	# thanks to https://computationalmindset.com/en/mathematics/experiments-with-sympy-to-solve-odes-1st-order.html
	f = symbols('f', cls=Function) # make the distance function
	f = distance_function

	
	print("f: "+str(f))
	if not maximumthing:

		solution = minimum(f, x)
	else:
		solution = maximum(f, x)

	print("solution: "+str(solution))
	print("distance_function : "+str(distance_function))

	

	return solution


def mindistobjdot(command:str, objects:list):

	# the first object can be anything, but the second argument must be a point

	arguments = command.split(" ")
	arguments = arguments[1:]
	
	object_thing = get_object_by_name(arguments[0])

	dot_thing = get_object_by_name(arguments[1])

	print("dot_thing: "+str(dot_thing))
	print("object_thing: "+str(object_thing))

	solution = distance_min(object_thing, dot_thing, maximumthing=False)

	if solution == []:
		print("No results for some reason")
		return 0
	else:
		print("Minimum distance: " + str(solution))
		return solution


	return 0

def maxdistobjdot(command:str, objects:list):

	# the first object can be anything, but the second argument must be a point
	arguments = command.split(" ")
	arguments = arguments[1:]
	
	object_thing = get_object_by_name(arguments[0])

	dot_thing = get_object_by_name(arguments[1])

	solution = distance_min(object_thing, dot_thing, maximumthing=True)

	if solution == []:
		print("No results for some reason")
		return 0
	else:
		print("Maximum distance: " + str(solution))
		return solution


	return 0

def get_circle_eq(xc,yc,r):
	print("Returning this: "+str("(x-{})**2+(y-{})**2=({})**2".format(xc,yc,r)))
	return [Eq(parse_expr("(x-{})**2+(y-{})**2".format(xc,yc)), parse_expr("({})**2".format(r)))]  # remember to write about the {}**2 instead of ({})**2 bug


def mindistpointobjdot(command:str, objects:list):
	
	arguments = command.split(" ")
	arguments = arguments[1:]

	radiuses = mindistobjdot(command, objects)
	point = get_object_by_name(arguments[1])
	other_object = get_object_by_name(arguments[0])
	equations = other_object.get_equations()
	print("radiuses : "+str(radiuses))
	radius = radiuses
	x = sympy.Symbol('x')
	y = sympy.Symbol('y')

	'''
	all_equations = equations1 + equations2
	print("All equations as a list: "+str(all_equations))


	result = sympy.solve(all_equations, ('x', 'y'))
	print("result: "+str(result))
	'''


	
	circle_equation = get_circle_eq(point.x, point.y, radius)
	print("circle_equation : "+str(circle_equation))
	equations += circle_equation
	print("all equations: "+str(equations))
	result = sympy.solve(equations, ('x', 'y'))

	print("Result: "+str(result))

	resulting_dict = {'x':result[0][0], 'y':result[0][1]}

	print("Resulting dict: "+str(resulting_dict))

	oofstring1 = str(result[0][0])
	oofstring2 = str(result[0][1])

	print("oofstring1: "+str(oofstring1))
	print("oofstring2: "+str(oofstring2))

	oofstring1 = ''.join(oofstring1.split(" ")) # get rid of spaces
	oofstring2 = ''.join(oofstring2.split(" "))

	print("oofstring1 after: "+str(oofstring1))

	print("oofstring2 after: "+str(oofstring2))

	final_dict = {'x':oofstring1, 'y':oofstring2}
	print("final_dict: "+str(final_dict))
	return final_dict


# variable_assignment_command(command_string, global_objects)

def variable_assignment_command(command_string: str, global_objects: list, max_arg_lengths: list, min_arg_lengths: list, commands: list) -> int:

	tokens = command_string.split(" ")

	if tokens[1] != ":=":
		fail("Invalid variable assignment command: "+str(command_string))
		return 1



	# the new variable name is tokens[0]
	new_var_name = tokens[0]

	assigning_command = tokens[2:] # the command is after the "variable :="   part .

	new_command_string = ' '.join(assigning_command)



	result = check_common_syntax_var(new_command_string, max_arg_lengths, min_arg_lengths, commands)  # this check is shared by every command to check the arguments
	if result:
		return 1

	commands = ["line", "intersect", "help", "quit", "objects", "circle", "point", "mindistobjdot", "maxdistobjdot", "mindistpointobjdot", "maxdistpointobjdot", "integrate"]
	index = commands.index(new_command_string.split(" ")[0])

	handle_functions = [line_command, intersection_command, help_command, quit_command, objects_command, circle_command, point_command, mindistobjdot, maxdistobjdot, mindistpointobjdot, maxdistpointobjdot]

	print("new_command_string == "+str(new_command_string))
	print("Running subcommand: "+str(commands[index]))


	var_values = handle_functions[index](new_command_string, global_objects)
	print("Returned from the assignment command:")
	print("var_values : "+str(var_values))



	user_defined_variables[new_var_name] = var_values
	print("var_values.keys()" + str(var_values.keys()))
	print(str([str(a) for a in var_values.keys()]))
	print(str([str(a) for a in var_values.values()]))
	return 0






def maxdistpointobjdot(command:str, objects:list):
	
	arguments = command.split(" ")
	arguments = arguments[1:]

	radiuses = maxdistobjdot(command, objects)
	point = get_object_by_name(arguments[1])
	other_object = get_object_by_name(arguments[0])
	equations = other_object.get_equations()
	print("radiuses : "+str(radiuses))
	radius = radiuses
	x = sympy.Symbol('x')
	y = sympy.Symbol('y')

	'''
	all_equations = equations1 + equations2
	print("All equations as a list: "+str(all_equations))


	result = sympy.solve(all_equations, ('x', 'y'))
	print("result: "+str(result))
	'''


	
	circle_equation = get_circle_eq(point.x, point.y, radius)
	print("circle_equation : "+str(circle_equation))
	equations += circle_equation
	print("all equations: "+str(equations))
	result = sympy.solve(equations, ('x', 'y'))

	print("Result: "+str(result))

# command_string = unpack_variables_in_command(command_string, user_defined_variables)

def unpack_variables_in_command(command_string:str, user_defined_variables: list):

	tokens = command_string.split(" ")
	
	generated_command = []
	for token in tokens:
		if "[" not in token or "]" not in token: # if there is nothing to unpack then just append as is
			generated_command.append(token)
		else:

			start = None
			end = None
			if token.count("[") > 1 or token.count("]") > 1:

				# get only partial part of the result:

				partial = token[token.index("]")+1:] # get the rest of the thing
				start = partial[1:partial.index(":")]
				end = partial[partial.index(":")+1:partial.index("]")]
				start = int(start)
				end= int(end)


				#fail("Subtokens like [myvar][a:b] are not implemented.")
				#return 1

			var_name = token[token.index("[")+1:token.index("]")] # get the variable name from inside the brackets
			if var_name not in user_defined_variables.keys():
				fail("Undefined variable: "+str(var_name)+" .")
				return 1


			var_values = user_defined_variables[var_name]

			print("str(var_values) == "+str(str(var_values)))
			print("start == "+str(start))
			print("end == "+str(end))
			if start != None and end != None:
				
				print("abcdefg")
				# print({k:d[k] for k in l if k in d})
				'''
				d = {1:2, 3:4, 5:6, 7:8}

				# the subset of keys I'm interested in
				l = (1,5)

				'''
				l = tuple([list(var_values.keys())[x] for x in range(start, end)])
				print("l == "+str(l))

				var_values = {k:var_values[k] for k in l if k in var_values}


			print("var_values final: "+str(var_values))

			replacement = ' '.join([str(key)+str("=")+str(var_values[key]) for key in var_values.keys()])

			generated_command.append(replacement)
	final_command = ' '.join(generated_command)
	return final_command


# mindistobjdot(command:str, objects:list):

def integrate_command(command: str, objects: list):

	# integrate a function over xstart to xend

	tokens = command.split(" ")
	selected_object = tokens[1]

	int_var = tokens[2] # variable is assumed to be next
	xstart = tokens[3]
	xend = tokens[4]
	expression = None

	if selected_object not in get_names(global_objects):
		# the input is assumed to be a literal expression
		equation = Eq(parse_expr(selected_object[:selected_object.index("=")]), parse_expr(selected_object[selected_object.index("=")+1:]))
		expressions = [equation]

	else:
		expressions = get_object_by_name(selected_object).get_equations()

	# if there are multiple equations for the object, then make the user choose which of them:

	if len(expressions) > 1:
		warn("The object you selected has multiple equations associated with it: ")
		count = 0
		for expr in expressions:
			print(CBLUE +str("[{}] ".format(count)) + str(expr)+bcolors.ENDC)
			count += 1
		print("Please select the index of the desired expr: ")
		index = int(input("> "))
		selected_expr = expressions[index]
	else:
		selected_expr = expressions[0]

	x = Symbol('x')
	y = Symbol('y')

	print("selected_expr: "+str(selected_expr))
	y_function = solve(selected_expr,y)
	print("y_function: " +str(y_function))
	y_function = y_function[0]
	result = integrate(y_function,(x,xstart, xend))

	print(CYELLOW + "Result: "+str(result) + bcolors.ENDC)

	return result



def area_between_intersections(command:str, objects:list):

	# calculate the area between the two intersection points of two graphs

	# the syntax for this problem would be "commandstring" object1 object2

	# parse command


	tokens = command.split(" ")


	equation_list = []



	# get equations from the arguments:  (I should probably makes this a function in itself to check if an arguments a raw expression or an object itself. )

	for i in range(1,3):
		object_name = tokens[i]

		if object_name not in get_names(objects):
			# assumed to be a raw expression
			equation = Eq(parse_expr(object_name[:object_name.index("=")]), parse_expr(object_name[object_name.index("=")+1:]))
			expressions = [equation]

		else:
			# object
			expressions = get_object_by_name(object_name).get_equations()

		if len(expressions) > 1:
			warn("The object you selected has multiple equations associated with it: ")
			count = 0
			for expr in expressions:
				print(CBLUE +str("[{}] ".format(count)) + str(expr)+bcolors.ENDC)
				count += 1
			print("Please select the index of the desired expr: ")
			index = int(input("> "))
			selected_expr = expressions[index]
		else:
			selected_expr = expressions[0]
		equation_list.append(selected_expr)
			
	# get intersection points:

	# def intersection(object1, object2):

	'''
	all_equations = equations1 + equations2
	print("All equations as a list: "+str(all_equations))


	result = sympy.solve(all_equations, ('x', 'y'))
	print("result: "+str(result))

	return result
	'''







	intersection_points = solve(equation_list, ('x', 'y'))
	print("intersection_points == "+str(intersection_points))
	if len(intersection_points) < 2:
		fail("Not enough intersection points for the integral command!")
		return 1

	intersection_x_values = [intersection_points[0][0], intersection_points[1][0]]
	print("thingoof intersection_x_values ==" + str())

	# make the difference function

	#functions_in_y_format = Solve(equation_list, ('y'))

	#function1 = functions_in_y_format[0]
	functions_in_y_format = []

	for eq in equation_list:
		functions_in_y_format.append(solve(eq, ('y')))

	intersection_x_values = sorted(intersection_x_values)

	check_value = random.uniform(intersection_x_values[0], intersection_x_values[1])



	# see which function is larger in that range
	print("functions_in_y_format == "+str(functions_in_y_format))

	if (len(functions_in_y_format[0])) > 1:
		print("Please select one of these graphs: ")
		count = 0
		for thing in functions_in_y_format[0]:
			print(str(count) + " : "+str(thing))
			count+=1 
		index = int(input(">>"))

		functions_in_y_format[0] = [functions_in_y_format[0][index]]





	if (len(functions_in_y_format[1])) > 1:
		print("Please select one of these graphs: ")
		count = 0
		for thing in functions_in_y_format[1]:
			print(str(count) + " : "+str(thing))
			count+=1 
		index = int(input(">>"))

		functions_in_y_format[1] = [functions_in_y_format[1][index]]



	if functions_in_y_format[0][0].subs({'x':check_value}) > functions_in_y_format[1][0].subs({'x':check_value}):

		bigger_function = functions_in_y_format[0][0]
		smaller_fun = functions_in_y_format[1][0]
	else:
		bigger_function = functions_in_y_format[1][0]
		smaller_fun = functions_in_y_format[0][0]


	print("bigger function: "+str(bigger_function))
	print("smaller_fun : " + str(smaller_fun))

	#difference_function = parse_expr(bigger_function) - parse_expr(smaller_fun)

	difference_function = bigger_function - smaller_fun


	print("Difference function: "+str(difference_function))


	print("intersection_x_values[0] == "+str(intersection_x_values[0]))
	print("intersection_x_values[1] == "+str(intersection_x_values[1]))


	resulting_area = integrate(difference_function, ('x', intersection_x_values[0], intersection_x_values[1]))

	print(CYELLOW + "Area: "+str(resulting_area) + bcolors.ENDC)



	return resulting_area


	#obj1 = get_object_by_name(tokens[1])
	#obj2 = get_object_by_name(tokens[2])



def get_tangent_from_point_and_derivative(x0thing,fx0):

	xnew = Symbol('xnew')
	x0 = Symbol('x0')
	x = Symbol('x')
	k = simplify(Derivative(fx0,x0thing)).subs({str(x0thing):xnew})
	print("k : "+str(k))

	# y - y0 = k*(x - x0)

	print("x0 : "+str(x0))
	print("fx0 : "+str(fx0))
	derivative_line = simplify(k*(x - x0thing.subs({x0thing:xnew})) + fx0.subs({str(x0thing):xnew}))
	print("derivative_line: "+str(derivative_line))

	return derivative_line






def get_tangents(objects:list):

	# get the tangentlines which are shared by all the objects (if there exists any)

	if len(objects) == 1:
		
		# just get the tangent line stuff at x=x0 and return it

		# triangles are not supported because reasons.

		# the point is (x0,f(x0)) and the derivative aka k is derivative(f(x),x)|x=x0
		obj = objects[0]

		equation_list = obj.get_equations()

		# first solve y from the equation

		#y_eqs = []
		
		tangent_lines = []
		for eq in equation_list:

			y_eqs = solve(eq, 'y')

			for y_eq in y_eqs:


				#k = simplify(derivative(y_eq, x))

				x0 = Symbol('x0')

				print("y_eq: "+str(y_eq))
				print("equation_list: "+str(equation_list))

				tangent = get_tangent_from_point_and_derivative(x0,y_eq.subs({"x":x0}))

				tangent = tangent.subs({"xnew":x0})

				tangent_lines.append(tangent)
		
		return tangent_lines









def get_tangents_command(command:str, objects: list):

	# get_tangents

	args = command.split(" ")
	args = args[1:]

	objects = [get_object_by_name(x) for x in args]
	result = get_tangents(objects)

	return result





def parse_expected(filething):

	
	fh = open(filething, "r")
	lines = fh.readlines()
	fh.close()

	# the expected value is assumed to be after the # on the very last line of the file

	expected_value = lines[-1]

	if "\n" == expected_value[-1]:
		expected_value = expected_value[:-1]
	if "#" == expected_value[0]:
		expected_value = expected_value[1:]

	return expected_value



def command_mainloop(file=None, testsuite=None):
	print_banner()
	line_counter = 0
	lines = []
	if file:
		fh = open(file, "r")
		lines = fh.readlines()
		fh.close()
		for i in range(len(lines)):
			lines[i] = lines[i][:-1]
		print("Running commands from file "+str(file)+".")


	if testsuite:
		fh = open(testsuite, "r")
		lines = fh.readlines()
		fh.close()
		for i in range(len(lines)):
			lines[i] = lines[i][:-1]
		print("Testsuite from file "+str(testsuite)+".")



	objects = []
	commands = ["line", "intersect", "help", "quit", "objects", "circle", "point", "mindistobjdot", "maxdistobjdot", "mindistpointobjdot", "maxdistpointobjdot", "integrate", "area_between_intersections", "triangle", "angle_lines", "tangents"]
	min_arg_lengths = [0,0,0,0,0,0,0,2,2,2,2,4,2,0,2,1]
	max_arg_lengths = [3,2,0,0,0,3,2,2,2,2,2,4,2,6,2,100]

	command_result = None

	handle_functions = [line_command, intersection_command, help_command, quit_command, objects_command, circle_command, point_command, mindistobjdot, maxdistobjdot, mindistpointobjdot, maxdistpointobjdot, integrate_command, area_between_intersections, triangle_command, angle_between_lines_command, get_tangents_command]
	

	expected_result = None

	if testsuite:
		expected_result = parse_expected(testsuite)

	while True:

		if not testsuite:

			if line_counter != len(lines):
				command_string = lines[line_counter]
				line_counter += 1
				print("Command string: " + str(command_string))
			else:
				command_string = str(input(bcolors.OKBLUE + ">>> " + bcolors.ENDC))
				#command_string = "line a=1 b=2 c=3"
		else:

			if line_counter != len(lines):
				command_string = lines[line_counter]
				line_counter += 1
				print("Command string: " + str(command_string))
			else:

				# check the final output:
				print("The output of the last command: "+str(command_result))
				print("Expected final result: "+str(expected_result))
				
				if str(command_result) != str(expected_result):
					print("Testsuite failed!")

		command_start = command_string.split(" ")[0]
		if command_start == "quit":
			if testsuite:
				print("\"quit\" encountered in testsuite. Checking answer:")
				break

		command_result = None
		if command_start not in commands:

			if ":=" in command_string: # check variable assignment command
				print("poopooshit")
				result = variable_assignment_command(command_string, global_objects, max_arg_lengths, min_arg_lengths, commands)
				if result:
					fail("Invalid command: "+str(command_string))
				continue


			if command_start != "":
				print("thing")
				if len(command_string.split(" ")) == 1 and "." not in command_string.split(" ")[0]:
					# if the user types just the object name, then print object as string
					if command_start in get_names(global_objects):
						command_result = print_object(get_object_by_name(command_start))
						continue
					invalid_command(command_string)
					continue
				


				# first assume that the command is an attempt to run a method on an object:

				result = check_method_command(command_string, global_objects)
				print("result: "+str(result))
				if result: # 0 means success, 1 means failure
					invalid_command(command_string)
			continue

		index = commands.index(command_start)
		result = check_common_syntax(command_string, max_arg_lengths, min_arg_lengths, commands)  # this check is shared by every command to check the arguments
		if result:
			continue
		
		command_string = unpack_variables_in_command(command_string, user_defined_variables)  # this is to unpack arguments like [myvar]


		command_result = handle_functions[index](command_string, global_objects)

		print("Command result: " + str(command_result))

		#global_objects = 

	print("The output of the last command: "+str(command_result))
	print("Expected final result: "+str(expected_result))
	passing = False

	print("command_result: " + str(command_result))
	print("expected_result: "+str(expected_result))

	if str(command_result) != str(expected_result):
		print_col(bcolors.FAIL, "Testsuite " + str(testsuite)+ " failed!")
	else:
		print_col(bcolors.OKGREEN, "Testsuite " +str(str(testsuite))+ " passed!")
		passing = True
	return command_result, passing





def reset_state():

	global_objects = []
	global_things = []
	user_defined_variables = {}





if __name__=="__main__":
	'''


	if sys.argv[-1] == "--test":
		debug_tests()
		exit(0)
	'''


	if "--file" in sys.argv:
		filething = sys.argv[sys.argv.index("--file")+1]
	else:
		filething = None



	if "--testsuite" in sys.argv:
		testsuite = sys.argv[sys.argv.index("--testsuite")+1]
	else:
		testsuite = None

	test_all = False

	if "--test-all" in sys.argv:
		test_all = True


	if "--get-expected" in sys.argv:

		results = []

		for test in os.listdir("tests/"):
			print("Running test "+str(test))

			results.append(command_mainloop(file=filething, testsuite="tests/"+str(test)))

			# reset state:

			reset_state()

		print("Expected values for the tests:")
		count = 0
		for filething in os.listdir("tests/"):

			print("tests/"+filething+" : "+str(results[count]))

			count += 1
		exit(0)

	if not test_all:

		command_mainloop(file=filething, testsuite=testsuite)

	else:
		results = []
		for test in os.listdir("tests/"):
			print("Running test "+str(test))

			_, passing = command_mainloop(file=filething, testsuite="tests/"+str(test))

			results.append(passing)

			reset_state()   # reset the state such that we do not fuck up the next tests
			global_objects = []
			global_things = []
			user_defined_variables = {}

		#print summary
		count = 0
		fail = False

		print("results list: "+str(results))

		print_col(bcolors.OKBLUE, "=================================================\n\n")

		print_col(bcolors.OKBLUE, "Final results: \n")
		for thing in os.listdir("tests/"):
			if results[count]:
				# pass
				print_col(bcolors.OKGREEN, "Test: tests/"+str(thing)+" PASSED!")
			else:
				# fail:
				print_col(bcolors.FAIL, "Test: tests/"+str(thing)+" FAILED!")
				fail=True
			count += 1
		print("\n\n")
		if fail:
			print_col(bcolors.FAIL, "Some tests failed!\n\n")
		else:
			print_col(bcolors.OKGREEN, "All tests passed!\n\n")
		print_col(bcolors.OKBLUE, "=================================================")





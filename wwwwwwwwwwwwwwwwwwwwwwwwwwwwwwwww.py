

import numpy as np
import sympy
from sympy.parsing.sympy_parser import parse_expr
import sys
from sympy.solvers import solve
from sympy import Symbol
from sympy import Eq
from sympy import *
from outcolors import *
import readline

global_things = []
global_objects = []

commands = ["line", "intersect", "help", "quit", "objects", "point"]

object_types = ["line", "circle", "point"] # these are the types for when the argument to a method of an object are themselves objects. If not, then they are assumed to be constant values.

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
		

		print(string_oof_1)


		# (y0-y1)/(x0*y1-x1*y0)

		# -yv/(x0*yv-xv*y0)



		self.a = sympy.simplify(string_oof_1)

		string_oof_2 = "{}/({}*{}-{}*{})".format(xv, x0, yv, xv, y0)

		self.b = sympy.simplify(string_oof_2)
		#self.a = simplify(-(yv/(x0*yv-xv*y0)))
		#self.b = simplify(xv/(x0*yv-xv*y0))


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



	results = []
	'''
	for equation1, equation2 in zip(equations1, equations2):




		temp_var_x = Symbol("tempvarx")
		temp_var_y = Symbol("tempvary")

		#substitute_first = {object1.x:temp_var_x, object1.y:temp_var_y}
		#substitute_second = {object2.x:temp_var_x, object2.y:temp_var_y}

		#substitute_first = {"x":temp_var_x, "y":temp_var_y}
		#substitute_second = {"x":temp_var_x, "y":temp_var_y}


		substitute_first = {"x"+str(object1.var_count):temp_var_x, "y"+str(object1.var_count):temp_var_y}
		substitute_second = {"x"+str(object1.var_count):temp_var_x, "y"+str(object1.var_count):temp_var_y}




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
		results.append(result)
	'''

	temp_var_x = Symbol("tempvarx")
	temp_var_y = Symbol("tempvary")

	substituted_equations = []


	print("bullshit")
	for equation in equations1:
		print("equation : "+str(equation))
		print("\"x\"+str(object1.var_count) == " + str("x"+str(object1.var_count)))
		substitute_first = {"x":temp_var_x, "y":temp_var_y}
		#substitute_second = {"x"+str(object1.var_count):temp_var_x, "y"+str(object1.var_count):temp_var_y}

		equation1 = equation.subs(substitute_first)
		substituted_equations.append(equation1)

	for equation in equations2:

		substitute_first = {"x":temp_var_x, "y":temp_var_y}
		#substitute_second = {"x"+str(object1.var_count):temp_var_x, "y"+str(object1.var_count):temp_var_y}

		equation1 = equation.subs(substitute_first)
		substituted_equations.append(equation1)


	print("substituted_equations")
	for eq in substituted_equations:
		print(str(eq))

	print()
	result = sympy.solve(substituted_equations, (temp_var_x, temp_var_y))
	print("result: "+str(result))

	return result




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

	return 0




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
	return 0




def command_mainloop(file=None):
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

	objects = []
	commands = ["line", "intersect", "help", "quit", "objects", "circle", "point"]
	min_arg_lengths = [0,0,0,0,0,0,0]
	max_arg_lengths = [3,2,0,0,0,3,2]
	handle_functions = [line_command, intersection_command, help_command, quit_command, objects_command, circle_command, point_command]
	while True:
		if line_counter != len(lines):
			command_string = lines[line_counter]
			line_counter += 1
			print("Command string: " + str(command_string))
		else:
			command_string = str(input(bcolors.OKBLUE + ">>> " + bcolors.ENDC))
			#command_string = "line a=1 b=2 c=3"

		command_start = command_string.split(" ")[0]
		if command_start not in commands:
			if command_start != "":
				print("thing")
				if len(command_string.split(" ")) == 1 and "." not in command_string.split(" ")[0]:
					# if the user types just the object name, then print object as string
					if command_start in get_names(global_objects):
						print_object(get_object_by_name(command_start))
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

		handle_functions[index](command_string, global_objects)



		#global_objects = 












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

	command_mainloop(file=filething)






	


		






from geometrylib import *









if __name__=="__main__":


	x = Symbol('x')
	function = x**2
	result = get_tangent_from_point_and_derivative(x,function)

	print(result.subs({"xnew":"3"}))

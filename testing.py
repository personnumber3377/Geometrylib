


def get_range(x0,y0,x1,y1):

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



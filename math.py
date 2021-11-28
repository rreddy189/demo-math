# Add implementation
def add(x,y):
	return x+y

# Subtract implementation
def subtract(x,y):
	return x-y      # on master branch

# Multiply implementation
def multiply(x,y):
	return x*y 		# on Bug456 branch

# Divide implementation
def divide(x,y):
	if y==0:
		return DIVIDE_BY_ZERO_ERROR
	else:
		return x/y

# Absolute implementation
def absol(x):
	if x>=0:
		return x
	else:
		return -x

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
		return 'DIVIDE_BY_ZERO_ERROR'
	else:
		return x/y

# Absolute implementation
def absol(x):
	if x>=0:
		return x
	else:
		return -x

# exponent implementation
def power(x,a):
	if type(a) == 'int':
		ans = 1
		for _ in range(1,a+1):
			ans *= x
		return ans
	else:
		return 'TYPE_ERROR a is not int'
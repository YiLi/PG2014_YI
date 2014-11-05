#YiLi
#11/05/2014
#HW1Fibonacci

def fib(n):

	"""Return the first n items
	of Fibonacci array
	"""

	if n==1:
    
		f=[1]

	else:

		f=[1,1]

		for i in range(2,n):
			f.append(f[i-2]+f[i-1])
	return f

print 'please input how many Numbers you want in Fibonacci '

print 'the result is:'+str(fib(int(raw_input())))

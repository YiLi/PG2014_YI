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

if __name__ == '__main__':
	print 'input example:'
	print 'fib(4)' #result should be [1,1,2,3]
	print fib(4)


	while True:
		print 'please input how many Numbers you want in Fibonacci '
		print input()
		print 'please enter y to give another input or give other thing to quit:'
		a=raw_input()
		if a != 'y':
			break


	


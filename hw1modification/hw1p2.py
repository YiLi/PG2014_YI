#YiLi
#11/05/2014
#HW1Trapezodial
def Tra(f,dx=1.0):

	"""this is used to calculate
	intergration by Trapezodial
	rule"""

	n=len(f)

	sum=0.0

	for i in range(0,n-1):

		sum=sum+(f[i]+f[i+1])/2*dx

	return sum


print 'input example:'
print 'Tra([1,2,3],0.5)'
print 'result is 1.5'

while True:
	print 'please input f and dx'
	print input()
	print 'please enter y to give another input or enter other thing to quit:'
	a=raw_input()
	if a != 'y':
		break

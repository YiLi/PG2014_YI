##HW2Q3
##programmed by Yili
##Oct 9th.
import numpy as np
import matplotlib.pyplot as plt

def high_pass(Points,order=1):

	x,y=Points[:,0],Points[:,0]

	poly=np.polynomial.Polynomial.fit(x, y, order)
	highpass=y-poly(x)

	hppoints=[]
	for i in range( len(x)):
		hppoints.append([x[i],highpass[i]])

	return hppoints

Points=np.random.rand(5,2)

hppoints=high_pass(Points)

print hppoints

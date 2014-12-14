##HW2Q3
##programmed by Yili
##Dec 13th

import numpy as np
import matplotlib.pyplot as plt

def high_pass(x,y,order=1):


	poly=np.polynomial.Polynomial.fit(x, y, order)
	highpass=y-poly(x)

	return highpass

x=np.random.rand(100)
y=np.random.rand(100)

highpass=high_pass(x,y)

print highpass

plt.plot(x,y,'r.', label = 'Polynomial')
plt.plot(x,highpass,'b.',label='Difference')
plt.show()

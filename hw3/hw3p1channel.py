#Yi Li
#11/05/2014
#HW3channel

def channel(points,delta_x,delta_t,H0,steps,g=9.81):

	import numpy as np
	import matplotlib.pyplot as plt
	from math import pi,cos
	nx=int(points)
	nt=int(steps)

	eta=np.zeros((nt,nx-1))
	u=np.zeros((nt,nx))
	eta[0,0]=H0/2.

	for t in range (0,nt-1):
		u[t+1,1:-1]=u[t,1:-1]-g*delta_t/delta_x*(eta[t,1:]-eta[t,:-1,])
		eta[t+1,:]=eta[t,:]-H0*delta_t/delta_x*(u[t+1,1:]-u[t+1,:-1])
		for x in range(0,nx-1):
			print '%10.3f' % eta[t,x],
		print '\n'

	x=range(0,nx-1)
	t=range(0,nt)
	X,T=np.meshgrid(x,t)



	pcm = plt.pcolormesh(T,X,eta, cmap = plt.cm.RdBu_r,)
	plt.colorbar(pcm)
	plt.show()

channel(points=20.,delta_x=10000.,delta_t=360.,H0=40.,steps=150)

##HW2Q5
##programmed by Yili
##Oct 13th

import numpy as np
import matplotlib.pyplot as plt
import netCDF4

def read_etopo5(filename):
	f = open(filename)

	x=[]
	y=[]
	z=[]

	for line in f.readlines():
		data = line.split()

		x.append(float(data[0]))
		y.append(float(data[1]))
		z.append(float(data[2]))

	x=np.array(x)
	y=np.array(y)
	z=np.array(z)

	return x,y,z

x,y,z=read_etopo5('/home/yili/global_merged5.txt')



#transfer vector to matrix
lat=np.reshape(np.array(x),[2161,4321])
lon=np.reshape(np.array(y),[2161,4321])
z=np.reshape(np.array(z),[2161,4321])

fig = plt.figure(figsize=(11,8))

contour1=plt.contour(lat,lon,z,-1000.,colors='k',linewidths=1)
contour2=plt.contour(lat,lon,z,0.,colors='k',linewidths=3)
contour3=plt.contour(lat,lon,z,1000.,colors='k',linewidths=1)

contour2.collection[0].set_linestyle('solid')
contour3.collection[0].set_linestyle('solid')

plt.pcolormesh(lat,lon,z,cmap=plt.cm.RdBu_r)

plt.show()

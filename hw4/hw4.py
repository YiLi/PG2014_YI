##HW4Q1
##programmed by Yili
##Dec 14th

import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import pylab
import time

class channel(object):
	def __init__(self,steps,points,g,H,delta_x,delta_t):
		self.nt=steps
		self.nx=points
		self.H =H
		self.dx=delta_x
		self.dt=delta_t
		self.g = g

	def eta(self):

		t=np.array(range(0,self.nt))
		x_u=np.array(np.arange(0.0,self.nx*self.dx,self.dx))
		x_eta = np.array(np.arange(self.dx/2.,(self.nx-1./2)*self.dx,self.dx))
		time = np.array(np.arange(0.,self.nt*self.dt,self.dt))
		eta=np.array(np.zeros([self.nx,self.nt]))
		u =np.array(np.zeros([self.nx+1,self.nt]))

		eta[0:10,0]=self.H/2.
		T,X=np.meshgrid(t,x_u)
		for i in range(1,self.nt):
			u[1:-1,i] = u[1:-1,i] - self.g*self.dt/self.dx*(eta[1:,i-1]-eta[:-1,i-1])
			eta[:,i] = eta[:,i] - self.H*self.dt/self.dx*(u[1:,i]-u[:-1,i])

		for n in range(self.nt):
			plt.clf();plt.plot(eta[:,n]);
			pylab.ylim([-6,6])
			plt.savefig('./plots/wave_%03d.png' % n)

		self.eta=eta
		self.u = u
		self.X =X
		self.T =T

		nc = netCDF4.Dataset('Channel.nc', 'w')
	
		nc.createDimension('x_eta', self.nx-1)
		nc.createDimension('x_u', self.nx)
		nc.createDimension('timesteps', self.nt)

		nc.createVariable('x_eta', 'd', ('x_eta',))
		nc.variables['x_eta'][:] = x_eta
		nc.variables['x_eta'].units = 'meters'

		nc.createVariable('x_u', 'd', ('x_u',))
		nc.variables['x_u'][:] = x_u
		nc.variables['x_u'].units = 'meters'

		nc.createVariable('time', 'd', ('time',))
		nc.variables['time'][:] = t
		nc.variables['time'].units = 'second'

		nc.createVariable('eta', 'd', ('x_eta', 'timesteps'))
		nc.variables['eta'][:] = self.eta
		nc.variables['eta'].units = 'meter'

		nc.createVariable('u', 'd', ('x_u', 'timesteps'))
		nc.variables['u'][:] = self.u
		nc.variables['eta'].units = 'meter/second'
		
		nc.close()
	
if __name__ == '__main__':

	data=channel(points=201,steps=1000,g=9.81,H=40.,delta_x=100,delta_t=5.0)

	data.eta()

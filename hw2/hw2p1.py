##HW2Q1
##programmed by Yili
##Oct 7th
import numpy as np
    
def dis_points(m,n):

    x1,x2=np.meshgrid(m[:,0],n[:,0])
    y1,y2=np.meshgrid(m[:,1],n[:,1])

    dis=np.sqrt((x1-x2)**2+(y1-y2)**2)
    return dis

Points=np.random.rand(5,2)
n=np.random.rand(3,2)

dis=dis_points(m,n)
print dis

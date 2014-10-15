##HW2Q2
##programmed by Yili
##Oct 7th

from math import sqrt,sin,cos,pi

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotation(self, theta,p=None):
        if p is None:
            p = Point(0.0, 0.0)
        d_x=p.x-self.x
        d_y=p.y-self.y
        rot=Point(p.x+d_x*cos(theta)-d_y*sin(theta),
				  p.y+d_x*sin(theta)+d_y*cos(theta))
        return rot



	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y)

	def __str__(self):
		return '(%f, %f)' % (self.x, self.y)

	def __repr__(self):
		return 'Point(%f, %f)' % (self.x, self.y)

if __name__ == '__main__':
	p1 = Point(3.0, 4.0)
	p2 = Point(5.0, 8.0)


	rot=p1.rotation(theta=pi/2)
	print rot.x,rot.y

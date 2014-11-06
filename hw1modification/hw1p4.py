#YiLi
#11/05/2014
#HW1drifter
def read_drifter(filename):

	f=open(filename)

	names=[]
	tracks={}

	for line in f.readlines():
		data=line.split()
		if data!=[]:
			if data[1] == 'ACTIVE':
				if data[3][1]=='0':
					name = data[1] + ' ' + data[2] + ' ' + data[3]
				else:
					name = data[1] + ' ' + data[2]
			else:
				name = data[1]
		names.append(name)

	for name in names:

		positions=[]
		f=open(filename)

		while 1:
			line=f.readline()
			lines=line.split()

			if (len(lines) == 7 and lines[1]==name) or (len(lines)==12 and lines[1]+' '+lines[2]+' '+lines[3]==name) or (len(lines)==11 and lines[1]+' '+lines[2]==name and lines[3][0]=='5'):

				f.readline()
				f.readline()
				f.readline()

				while 1:
					line=f.readline()
					lines=line.split()

					if not len(lines) == 0:
						lat=float(lines[1][1:])+(float(lines[2]))%100.0/60.0
						lon=float(lines[3][1:])+(float(lines[4]))%100.0/60.0
						lat = "%.4f" % lat
						lon = "%.4f" % lon
						positions.append((lat,lon))

					else:
						break

					tracks.update({name:positions})
				break
			if not line:
				break
	return tracks 


if __name__ == '__main__':
	tracks=read_drifter('/home/yili/python/drifter.dat')

	print 'this is a example of FRODO' #result should be [('42.8203', '70.8108'), ('42.8212', '70.8134')]

	print tracks['FRODO']

	while True:
		print 'please track a rider you want:'
		print input()
		print 'please enter y to give another input or enter other thing to quit:'
		a=raw_input()
		if a != 'y':
			break

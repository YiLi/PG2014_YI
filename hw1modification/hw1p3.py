#YiLi
#11/05/2014
#HW1discharge
def read_and_discharge(filename):
	f = open(filename)
    
	import datetime

	dates=[]
	discharges=[]

	for line in f.readlines():
		data = line.split('\t')
		if (data[0] == 'USGS'):
			year = int(data[2][:4])
			month = int(data[2][5:7])
			day = int(data[2][8:])
            	
			discharge=data[3].split('_')[0]	    
			date=datetime.date(year,month,day)
			dates.append(date)
			discharges.append(discharge)
	return dates,discharges

dates,discharges=read_and_discharge('/home/yili/python/discharge.dat')

if __name__ == '__main__':
	print 'dates and discharge values are stored in dates and discharges'
	print 'please call what you want to see.'
	print 'example:'
	print 'dates[0],discharges[0]'
	print '1923-06-01 4800'

	while True:
		print 'please call dates or discharge values'
		print input()
		print 'please enter y to give another input or enter other thing to quit:'
		a=raw_input()
		if a != 'y':
			break


##HW2Q4 And Q6
##programmed by Yili
##Oct 13th

import numpy as np
import matplotlib.pyplot as plt
import datetime

class discharge(object):

    def __init__(self,file):
        self.name=file

    def disch(self):
        f = open(file)
        dates=[]
        discharges=[]
        for line in f.readlines():
            data = line.split('\t')
        if (data[0] == 'USGS'):
            year = int(data[2][:4])
            month = int(data[2][5:7])
            day = int(data[2][8:]) 
            discharge=data[3]	 
            date=datetime.date(year,month,day)
            dates.append(date)
            discharges.append(discharge*0.3048**3)
        dates=np.array(dates)
        discharges=np.array(discharges)
        return dates,discharges

    def data_of_year(self,year):
        if year>=1967 and year<=2014:
    
            dates, discharges = self.disch()    
            ydates=[]
            ydischarges=[]
            for date in dates:
                if date.year == year:    
                    ydates.append(date)
                    ydischarges.append(discharges[dates.index(date)])

            ydates=np.array(ydates)
            ydischarges=np.array(self.disch)
            return ydates, ydischarges

        else:
		    print "wrong value of year"

	def plot_alltime(self)
		figure=plt.figure()
		dates,dischargers=self.disch()
		plt.plot(dates, discharges)
		plt.show()

    def mean_std_yrs(self, years=None):
		if years is None:
			print "this is the annual mean/std value of whole data time"
			years=[]
			for i in range(1967,2015):
				years.append(i)

		mean_dates=[]
		mean_values=np.zeros(365)
		###year of 1969 has the data of all 365 days###
		###we do not want the day of 2.29###
		dates,discharges = self.data_of_year(1969)
		for date in dates:
			###use year=8888 to save mean value's year
			year=8888
			month=date.month
			day=date.day
			time=datetime.date(year,month,day)
			mean_dates.append(time)
			
		mean_value=np.zeros(365)
		mean_number=np.zeros(365)
		std_value=365*[[]]

		for yr in years:
			dates,discharges=self.data_of_year(yr)
			
			for date in dates:
				if date.month==2 and date.day=29:
					continue
				else:
				year=8888
				month=date.month
				day=date.day
				time=datetime.date(year,month,day)
				mean_value[dates.index(time)]=mean_value+discharges[dates.index(time)]
				mean_number[dates.index(time)]=mean_number+1
					for mean_day in mean_dates:
						if (month = mean_dates.month and day = mean_dates.day):
							std_values[mean_dates].append(discharges[dates.index(time)])

		for i in range(365):
			if mean_number==0.0:
				mean_value[i]=0
				std_value[i]=0
			else:
				mean_value[i]=mean_value[i]/mean_number
				std_value=np.std(std_values[i])

			

		return mean_dates,mean_value,std_value

	def plot_dev(year)
		if not (year>=1968 or year<=2013):
			print 'wrong input of the year'
		else:
			dates,discharges = self.data_of_year(year)
			mdate,mean_discharges,std_value=self.mean_value_yrs()

			plt.plot(dates,discharges,'r-')	
			plt.plot(dates,mean_discharges,'b-')
			plt.fill(dates,mean_discharges+std_value,'grey')
			plt.fill(dates,mean_discharges-std_value,'grey')
			plt.show()

import numpy as np
import sys 
import code
import cPickle as pickle
import glob
import re
import csv
y = '2007'

boop = []
with open('stats'+y+'.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        boop.append(row)
#code.interact(local=locals())
master = np.genfromtxt(y+'.csv', dtype=str, delimiter=',')
worker = np.asarray(boop)
xM, yM = master.shape

years = ['Year']
years.extend([y for i in range(xM-1)])
years = np.asarray(years)
#code.interact(local=locals())

master = np.c_[years, master]
where = master[:,6]

ats = np.where(where == '@')
notats = np.where(where == '')
master[ats, 6] = 'A'
master[notats,6] = 'H'

weeks = np.where(master[:,1] == 'Week')
weeks = weeks[0][1:]
master = np.delete(master, weeks, 0)



winners = master[:, 5]
losers = master[:, 7]
workerNames = worker[1:, 0]

#for xx, each in enumerate(workerNames):
	#ss =  len(re.findall(r"^[0-9]{5}$", each))
	#dd =  len(re.findall(r"^[0-9]{8}$", each))
	#if ss != 0 or dd != 0:
		
		#workerNames[xx] = '0'+ each
		

copy = np.hstack((master[0,:], worker[0,:], worker[0,:]))
master = master[1:,:]

for xx,each in enumerate(master):
	
	winner = each[5]
	loser = each[7]
	
	indx = np.where(workerNames == winner)
	indx2 = np.where(workerNames == loser)
	
	a=master[xx].T
	#code.interact(local=locals())
	try:
		b= worker[indx[0]+1][0]
		c= worker[indx2[0]+1][0]
	except IndexError as e:
		code.interact(local=locals())
	
	ee = np.hstack((a,b,c))
	
	copy = np.vstack((copy, ee))	

	

with open('alignedData' + y+ '.csv', 'w') as ff:
	csv.writer(ff).writerows(copy)
	
	
#code.interact(local=locals())

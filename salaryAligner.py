import numpy as np
import sys 
import code
import cPickle as pickle
import glob
import re
import csv
boop = []
with open('FootBallPlayerStats_old.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
		boop.append(row)
master = np.asarray(boop)
master = master[:,0:55]

boop = []
with open('salaries.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
		boop.append(row)
worker = np.asarray(boop)
#worker = np.genfromtxt('salaries.csv', dtype=str, delimiter=',')


masterNames = master[1:,1]
workerNames = worker[1:,2]
counter = 0

badList = []
#code.interact(local=locals())
#for xx, each in enumerate(workerNames):
	#ss =  len(re.findall(r"^[0-9]{5}$", each))
	#dd =  len(re.findall(r"^[0-9]{8}$", each))
	#if ss != 0 or dd != 0:
		
		#workerNames[xx] = '0'+ each
		

copy = np.hstack((master[1,:], worker[0,:]))

for xx,each in enumerate(masterNames):
	indx = np.where(workerNames == each)
	if len(indx[0]) > 0:
		
		ee = np.append(master[xx+1].T, worker[indx[0]+1])
		#code.interact(local=locals())
		try:
			copy = np.vstack((copy, ee))
		except ValueError as e:
			print 'value error' + e
			code.interact(local=locals())
			continue
	else:
		#code.interact(local=locals())
		badList.append(xx)


print badList
print len(badList)		

with open('alignedData1.csv', 'w') as ff:
	csv.writer(ff).writerows(copy)
	
	
code.interact(local=locals())

import numpy as np
import sys 
import code
import cPickle as pickle
import glob
import re
import csv
boop = []
with open('combine1415.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
		
		if len(row) != 28:
			row.append('')
			row.append('')
			
		boop.append(row)
master = np.asarray(boop)
worker = np.genfromtxt('years_2015_draft_drafts.csv', dtype=str, delimiter=',')
code.interact(local=locals())
master = master[:, 0:-2]
masterNames = master[1:,1]
workerNames = worker[1:,3]
counter = 0
code.interact(local=locals())
badList = []
#code.interact(local=locals())
#for xx, each in enumerate(workerNames):
	#ss =  len(re.findall(r"^[0-9]{5}$", each))
	#dd =  len(re.findall(r"^[0-9]{8}$", each))
	#if ss != 0 or dd != 0:
		
		#workerNames[xx] = '0'+ each
		

copy = np.hstack((master[0,:], worker[0,:]))

for xx,each in enumerate(masterNames):
	indx = np.where(workerNames == each)
	if len(indx[0]) > 0:
		
		ee = np.append(master[xx+1].T, worker[indx[0]+1])
		#c
		try:
			copy = np.vstack((copy, ee))
		except ValueError as e:
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

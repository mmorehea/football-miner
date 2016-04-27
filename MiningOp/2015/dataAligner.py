import numpy as np
import sys 
import code
import cPickle as pickle
import glob
import re
import csv


l = glob.glob('./years/*.csv')
l.sort()

BigSet = np.array([])
for y in range(2015,2016):
	#y = each.split('/')[-1].split('.')[0]
	print y
	y = str(y)
	boop = []
	with open('./AllStats/'+y+'AllStats.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			boop.append(row)
	#code.interact(local=locals())
	master = np.genfromtxt('./years/'+y+'.csv', dtype=str, delimiter=',')
	worker = np.asarray(boop)
	xM, yM = master.shape


	
	ats = np.where(master == '@')
	colAts = ats[1][0]
	where = master[:,colAts]
	notats = np.where(where == '')
	master[ats, colAts] = 'A'
	master[notats,colAts] = 'H'

	
	
	workerNames = worker[:, 2]
	wNames = []
	for each in workerNames:
		title = re.sub("[^A-Za-z0-9\.]+", " ", each.strip()).strip()
		wNames.append(title)
	#code.interact(local=locals())
	workerNames = np.asarray(wNames)
	worker[:,2] = workerNames


	master = master[1:,:]
	
	ee2 = master[0]
	WL = []
	for xx,each in enumerate(ee2):
		if each in workerNames:
			WL.append(xx)
	#code.interact(local=locals())		
	W = WL[0]
	L= WL[1]
	xW, yW = worker.shape
	
	copy = np.array([])
	
	for xx,each in enumerate(master):
		if each[W] == '':
			continue
		if 'N' in each:
			continue
			
		winner = each[W]
		loser = each[L]
		
		indx = np.where(workerNames == winner)
		indx2 = np.where(workerNames == loser)
		
		a=master[xx].T
		#code.interact(local=locals())
		try:
			b= worker[indx[0]][0]
			c= worker[indx2[0]][0]
		except IndexError as e:
			code.interact(local=locals())
		
		ee = np.hstack((a,b,c))
		#code.interact(local=locals())
		copy = np.vstack((copy, ee)) if copy.size else ee	
		

		
	print copy.shape
	with open('alignedData' + y+ '.csv', 'w') as ff:
		csv.writer(ff).writerows(copy)
	BigSet = np.vstack((BigSet, copy)) if BigSet.size else copy
	
	#code.interact(local=locals())
with open('2000-2015set.csv', 'w') as ff:
		csv.writer(ff).writerows(BigSet)	
#code.interact(local=locals())

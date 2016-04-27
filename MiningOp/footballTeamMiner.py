from bs4 import BeautifulSoup
import urllib
import code
import string
import sys
import urllib2
import numpy as np
import cPickle as pickle
import os
import csv
import html2text
import nltk

for year in range(2015, 2016):
	print year

	html = urllib2.urlopen('http://www.pro-football-reference.com/years/'+str(year)+ '/games.htm')

	soup = BeautifulSoup(html)
	s =soup.find_all("tr")
	l=[]
	for each in s:
		line = each.text.encode('utf-8').split('\n')
		if len(line) == 15:
			l.append(line)

	l = np.asarray(l)


	week = l[:,1]

	week = np.where(week == 'Week')
	
	week = week[0][1:]
	l = np.delete(l, week,0)

	#code.interact(local=locals())
	l[:,0] = str(year)

	with open(str(year)+'.csv', 'w') as ff:
			csv.writer(ff).writerows(l)
	

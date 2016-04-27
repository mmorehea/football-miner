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


def setSplitter(arr):
	a1 = arr[::2]
	a2 = arr[1::2]
	
	return a1, at
	
class Year(object):
		
	def __init__(self, name):
		self.name = name
		self.sets = []
		
		

for year in range(1997, 1999):
	year = str(year)
	print year

	html = urllib2.urlopen('http://www.pro-football-reference.com/years/' +year +'/')

	soup = BeautifulSoup(html)
	
	s = soup.find_all('tbody')
	dd = []
	for each in s:
		xx =each.find_all('tr')
		for ee in xx:
			w = ee.text.encode('utf-8').split('\n')
			#code.interact(local=locals())
			dd.append(w)

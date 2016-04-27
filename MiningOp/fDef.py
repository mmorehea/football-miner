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

for year in range(1960, 2016):
	year = str(year)
	print year

	html = urllib2.urlopen('http://www.pro-football-reference.com/years/2015/opp.htm')

	soup = BeautifulSoup(html)
	
	s = soup.find_all('tbody')
	dd = []
	for each in s:
		xx =each.find_all('tr')
		for ee in xx:
			w = ee.text.encode('utf-8').split('\n')
			#code.interact(local=locals())
			dd.append(w)
	#code.interact(local=locals())
	set1 = np.asarray([x for x in dd if len(x) == 30])
	set2 = np.asarray([x for x in dd if len(x) == 24])
	set3 = np.asarray([x for x in dd if len(x) == 12])
	set4 = np.asarray([x for x in dd if (len(x) == 14 and 'Own' not in x[-4])])
	set5 = np.asarray([x for x in dd if len(x) == 25])
	set6 = np.asarray([x for x in dd if len(x) == 22])
	set7 = np.asarray([x for x in dd if len(x) == 14 and 'Own' in x[-4]])
	
	top1 = 'Rk	Tm	G	PF	Yds	Ply	Y/P	TO	FR	1stD	Cmp	Att	Yds	TD	Int	NY/A	1stD	Att	Yds	TD	Y/A	1stD	Pen	Yds	1stPy	Sc%	TO%	EXP'
	top1 = top1.split()
	top1.insert(0,'')
	top1.append('')
	set1 = set1[:-1,:]
	set1 = set1[set1[:,1].argsort()]
	set1 = np.vstack((top1,set1))
	set1[:,0] = year
	#code.interact(local=locals())
	top2 = 'Rk	Tm	G	Cmp	Att	Cmp%	Yds	TD	TD%	Int	Int%	Y/A	AY/A	Y/C	Y/G	Rate	Sk	Yds	NY/A	ANY/A	Sk%	EXP'
	top2 = top2.split()
	top2.insert(0,'')
	top2.append('')
	set2 = set2[:-1,:]
	set2 = set2[set2[:,2].argsort()]
	set2 = np.vstack((top2,set2))
	set2 = set2[:,1:]		
	
	
	top3 = 'Rk	Tm	G	Att	Yds	TD	Y/A	Y/G	Fmb	EXP'
	top3 = top3.split()
	top3.insert(0,'')
	top3.append('')
	set3 = set3[:-1,:]
	set3 = set3[set3[:,2].argsort()]
	set3 = np.vstack((top3,set3))
	set3 = set3[:,1:]	
	
	top4 = 'Rk	Tm	G	Ret	Yds	TD	Y/R	Rt	Yds	TD	Y/Rt	APYd'
	top4 = top4.split()
	top4.insert(0,'')
	top4.append('')
	set4 = set4[:-1,:]
	set4 = set4[set4[:,2].argsort()]
	set4 = np.vstack((top4,set4))
	set4 = set4[:,1:]		
	
	top5 = 'Rk	Tm	G	FGA	FGM	FGA	FGM	FGA	FGM	FGA	FGM	FGA	FGM	FGA	FGM	FG%	XPA	XPM	XP%	Pnt	Yds	Blck	Y/P'
	top5 = top5.split()
	top5.insert(0,'')
	top5.append('')
	set5 = set5[:-1,:]
	set5 = set5[set5[:,2].argsort()]
	set5 = np.vstack((top5,set5))
	set5 = set5[:,1:]		
	
	top6 = 'Rk	Tm	G	RshTD	RecTD	PRTD	KRTD	FblTD	IntTD	OthTD	AllTD	2PM	2PA	XPM	XPA	FGM	FGA	Sfty	Pts	Pts/G'
	top6 = top6.split()
	top6.insert(0,'')
	top6.append('')
	set6 = set6[:-1,:]
	set6 = set6[set6[:,2].argsort()]
	set6 = np.vstack((top6,set6))
	set6 = set6[:,1:]	
	
	top7 = 'Rk	Tm	G	#Dr	Plays	Sc%	TO%	Plays	Yds	Start	Time	Pts'
	top7 = top7.split()
	top7.insert(0,'')
	top7.append('')
	set7 = set7[set7[:,2].argsort()]
	set7 = np.vstack((top7,set7))
	set7 = set7[:,1:]	
	
	
	code.interact(local=locals())
	superSet = np.c_[set1, set2, set3, set4, set5, set6, set7]
	code.interact(local=locals())
	


	with open(str(year)+'.csv', 'w') as ff:
			csv.writer(ff).writerows(l)
	

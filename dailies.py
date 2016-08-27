#!/Users/jacob/anaconda/bin/python

import lxml
import re
import urllib
import requests
import time
import urllib2
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'jakesbot/5.0'}
req = urllib2.Request('http://xkcd.com/', None, headers)
html = urllib2.urlopen(req).read()

soup = BeautifulSoup(html, "html.parser") 
for div in soup.findAll('div', {'id': 'comic'}):
	image = div.find('img')['src']
	print 'downloading from ' +  image
	urllib.urlretrieve('http:' + image, 'xkcd.jpg') 



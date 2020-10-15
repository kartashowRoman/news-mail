import re

#clean html tags
def cleanhtml(raw_html):
	cleanr = re.compile('<[^<]+?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext
#clean html entities
def clean(raw_html):
  	cleanr = re.compile('&[^<]+?;')
  	cleantext = re.sub(cleanr, '', raw_html)
  	return cleantext


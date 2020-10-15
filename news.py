from urllib.request import urlopen
import functions
import re 


#get the html
url = 'https://www.rbc.ru/'
page = urlopen(url)
html = page.read().decode("utf-8")
#save urls of all articles
find_all_url = re.findall('data-vr-contentbox-url="(.*)">',html)


#scrape each article 
text = ''
name = ''
name_and_text = "Subject: DailyAutoNews-rbc.ru\n"
#total num of articles is 15, so I limited the total number to 5
for i in range(len(find_all_url)-10):
	url = find_all_url[i]
	page = urlopen(url)
	html = page.read().decode("utf-8")
	
	#find title
	name = re.findall('<title>(.*)</title>', html)
	name_and_text += '\n\n'
	for j in name:
		name_and_text += j + '\n\n'
	
	
	#find all the text between <p>
	text = re.findall('<p>(.*)</p>', html)
	for t in text:
		name_and_text += t


name_and_text = functions.cleanhtml(name_and_text)
name_and_text = functions.clean(name_and_text)



''' debug
html_to_file = open("html.txt","w")
html_to_file.write(name_and_text)
html_to_file.close()
'''


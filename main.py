import pynotify
import untangle
import urllib
import re
import time
flag=False
this_string=''
while True:
	tree=untangle.parse('http://static.cricinfo.com/rss/livescores.xml')
	for item in tree.rss.channel.item:
		string=' '
		string=item.title.cdata
		print string
		for word in string.split(' '):
			if word=="India":
				this_string=string
				flag=True
	if flag==False:
		string="Not India's match today. Focus on studies"
	pynotify.init("TEST")
	notice=pynotify.Notification("Your Score card by Jaskaran",this_string)
	notice.show()
	time.sleep(60)


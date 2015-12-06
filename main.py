''' Author : Jaskaran Singh (jvsg)
    Date   : 6 December 2015
'''
import pynotify			#Used to display message on to the screen
import untangle			#Used for 'untangling' XML file
import urllib			#Used for Url managment
import time			#Used for sleep function
flag=False			#initializing Flag
while True:			#infinite loop
	tree=untangle.parse('http://static.cricinfo.com/rss/livescores.xml')#get the information
	for item in tree.rss.channel.item:			
		string=' '					#Clears the previous val
		string=item.title.cdata				
		print string
		for word in string.split(' '):			#Iterates over the Sentence
			if word=="India":			#You can Choose your own Country
				this_string=string		
				flag=True
	if flag==False:
		string="Not India's match today. Focus on studies"#If your contry isn't playing match
	pynotify.init("TEST")			#Just an obligation. Nothing more.
	notice=pynotify.Notification("Your Score card by Jaskaran",this_string)
	notice.show()
	time.sleep(60)				#change this to change scorecard refresh rate


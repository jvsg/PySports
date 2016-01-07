import untangle			#Used for 'untangling' XML file
import time				#Used for sleep function
import re

#logger=logging.getLogger('fetch')

def list_matches(value):
	'''Returns a list of all the matches'''
	tree=untangle.parse('http://static.cricinfo.com/rss/livescores.xml')#get the information
	match_list=[]
	for item in tree.rss.channel.item:			
		string=str(item.title.cdata)
		string=re.sub(r'[0-9/\*&]','',string)
		' '.join(string.split())
		match_list.append(string)
	return match_list


def match_details(value):
	'''Returns the detail of the match you asked for'''
	tree=untangle.parse('http://static.cricinfo.com/rss/livescores.xml')#get the information
	iterator=0
	for item in tree.rss.channel.item:
		if iterator==value:
			string=item.title.cdata
			break
		iterator+=1
	return string




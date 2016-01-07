import display
import ui
import logging
import fetch
from time import sleep

logger=logging.getLogger('main.py')
logger.setLevel(logging.DEBUG)
fh=logging.FileHandler('Seeker.log')
fh.setLevel(logging.DEBUG)
ch=logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

SLEEP=60


print '''The sports we are supporting are : 
		 1) Cricket
	  '''
while True:
	try:
		sport_choice=int(raw_input())
		break
	except ValueError:
		logger.debug("Asking for valid sport choice")
		print "Supply a valid value."

while True:
	match_list=fetch.list_matches(sport_choice)
	n=0
	for item in match_list:
		print "%d. %s"%(n+1,item)
		n+=1
	while True:
		try:
			match_choice=int(raw_input())
			break
		except ValueError:
			logger.debug("Asking for a valid sport choice")
			print "Supply a valid value."
	while True:
		ui.show_message(fetch.match_details(match_choice-1))
		sleep(SLEEP)







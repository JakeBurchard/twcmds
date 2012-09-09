#!/usr/bin/env python
import time
import HTMLParser
from cmd_exec import cmd_exec

ITER_TIME = 15.0

def get_status(api, truncate):
	cur_cmd = ""
	while True:
		curStatus = api.user_timeline()[0]
		curStatus = HTMLParser.HTMLParser().unescape(curStatus.text)
		if curStatus != cur_cmd:
			cur_cmd = curStatus
            print "----------------"
			print "New Status: " + curStatus
			if cmd_exec(api, curStatus, truncate):
				print "Status successfully executed"
			else:
				print "Status is not a command"
		time.sleep(ITER_TIME)





	
	
	

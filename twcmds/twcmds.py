#!/usr/bin/env python
import threading
import sys
import time
from connection import TwitConn
from daemon import get_status
from process_args import process_args

CONSUMER_KEY = "IC04UVhEliv1wlLrMNA"
CONSUMER_SECRET = "po9TU3YHe4VrkY7Ez3HAJHLX1gOPMCs0lnbFUwctAU"

  
def main():
    truncate = False
    if process_args(sys.argv) == 2:
        print "Truncate command responses to one tweet..."
        truncate = True
    connObj = TwitConn(CONSUMER_KEY, CONSUMER_SECRET)
    connObj.start_api()
    api = connObj.api
    try:
        thread = threading.Thread(target = get_status, args = (api, truncate))
        thread.daemon = True
        thread.start()
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print "Keyboard Interrupt, quitting Twell..."
    
if __name__ == "__main__":
    main()





	
	
	

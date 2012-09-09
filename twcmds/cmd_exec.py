#!/usr/bin/env python
import re, os
import subprocess
from read_config import ConfigInfo
from response import update_response

CMD_CHARS = ">>"
config = ConfigInfo('config.ini')

if config.keyword_exists('Settings', 'Chars'):
    CMD_CHARS = config.config.get('Settings', 'Chars')
    
CMD_PRECS = {CMD_CHARS + "shell(.*)": ""}
 
for key, value in config.commands:
	CMD_PRECS[CMD_CHARS + key + "(.*)"] = value
	

def cmd_exec(api, cmd, truncate):
	for key in CMD_PRECS:	
		matchObj = re.match(key, cmd)
		if matchObj:
			cmd = CMD_PRECS[key] + matchObj.group(1)
			cmd = cmd.split()
			try:
				resp = subprocess.check_output(cmd, shell = True, stderr = subprocess.STDOUT, universal_newlines = True)
			except CalledProcessError:
				resp = CalledProcessError.output
			if not resp: resp = "Success!"
			update_response(api, resp, truncate)
			return True
	return False
			
	
	

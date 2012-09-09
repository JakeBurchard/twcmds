#!/usr/bin/env python
import sys
import re
from cmd_exec import cmd_exec
from connection import TwitConn
from read_config import ConfigInfo


def print_commands(config):
    print "[Commands]"
    if config.commands:
        for (key, val) in config.commands:
            print "{key}:{value}".format(key=key,value=val)
        return
    print "No commands set"
def add_commands(config, args):
    if len(args) == 4:
        keyword = args[2]
        command = args[3]
        if not config.keyword_exists('Commands', keyword):
            config.set_settings('Commands', keyword, command)
            print "Successfully added keyword '%s'" % keyword
        else:
            print "Keyword '%s' already exists" % keyword
    else:
        print "Usage: twcmds -a [keyword] \"[command]\""
def delete_commands(config, args):
    if len(args) == 3:
        keyword = args[2]
        if config.remove_keyword(keyword):
            print "Successfully deleted keyword '%s'" % keyword
        else:
            print "No such keyword '%s'" % keyword
    else:
        print "Usage: twcmds -d [keyword]"
def change_command_chars(config, args):
    if len(args) == 3:
        if config.has_settings('Settings'):
            chars = args[2]
            if not re.search('[@#]+', chars):
                config.set_settings('Settings', 'Chars', chars)
                print "Successfully changed command indicating characters to '%s'" % chars
            else:
                print "'@' and '#' are illegal characters"
        else:
            print "twcmds first needs to be authorized"
    else:
        print "Usage: twcmds -c [chars]"
def unauthorize(config):
    if config.remove_settings():
        print "Successfully unauthorized twcmds"
    else:
        print "twcmds is not currently authorized"
    
def process_args(args):
    usage = """Usage: twcmds [options]
    Options:
    -p                      : Print current commands
    -a [keyword] "[command]": Add a [keyword] denoting some [command]
    -d [keyword]            : Delete a [keyword]
    -u                      : Unauthorize twcmds
    -t                      : Truncate command responses to one tweet
    -c "[chars]"            : Change command indicating characters ('>>' is default)
    -h, --help              : Print usage
    """
    if len(args) > 1:
        config = ConfigInfo('config.ini')
        if args[1] in ('-h', '--help'):
            print usage  
            sys.exit(1)
        elif args[1] == '-p':
            print_commands(config)
            sys.exit(1)
        elif args[1] == '-a':
            add_commands(config, args)
            sys.exit(1)
        elif args[1] == '-d':
            delete_commands(config, args)
            sys.exit(1)
        elif args[1] == '-u':
            unauthorize(config)
            sys.exit(1)
        elif args[1] == '-t':
            return 2
        elif args[1] == '-c':
            change_command_chars(config, args)
            sys.exit(1)
    




	
	
	

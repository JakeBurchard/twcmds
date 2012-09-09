===========
Twcmds 
===========

Getting Comsumer Keys and Secrets
---------------------------------

To use twcmds you must first setup a Twitter developer account and get
a consumer key and secret. Then edit twcmds.py under the twcmds folder
and add you spefic key and secret where indicated. 

Introduction
-------------

Twcmds is a command line utility that receives predefined 
commands from an authroized Twitter account and runs them on a
host computer. Custom keywords referring to specific shell 
commands can be set, or the shell can be interfaced with 
directly. Valid twitter commands may look like:

    >>shell echo 'hello'
    >>ftp 123.23.123.123 foo.txt

The preceding '>>' characters differentiate a command from a normal
tweet. 'Shell' and 'ftp' are keywords which refer to commands set
by the user ('shell' is the default keyword for directly interfacing
the shell). 

After twcmds receives the commands from twitter it executes 
them and posts the standard output as a separate tweet(s).


Adding Keywords
-------------

To add custom keywords, use the -a flag:

    python twcmds.py -a [keyword] "[command..]"

Make sure that the command the keyword refers to is in quotes if 
it spans more than one word. The configuration file can also be
edited directly to add or remove keywords.
    
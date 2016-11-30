# -*- coding: utf-8 -*-
#!/usr/bin/python
# mail spammer by Incognito04

import platform
import smtplib
import getpass
import os	
from time import gmtime, strftime, sleep
import random


banner1 = """\033[35m""" + """

 _____                _ _                                                 
|  ___|              (_) |                                                
| |__ _ __ ___   __ _ _| |  ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
|  __| '_ ` _ \ / _` | | | / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
| |__| | | | | | (_| | | | \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
\____/_| |_| |_|\__,_|_|_| |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                               | |                                        
                               |_|                                                                       

\033[35m A simple but efficient email spammer   

\033[38m[---]\033[35m        Email_spammer		       \033[38m[---]
\033[34m[---]\033[35m        Created by: incognito04           \033[34m[---]
\033[35m[---]\033[35m        Version: 2.1.0                    \033[35m[---]
\033[32m[---]\033[33m        Codename:more nicer and efficient \033[32m[---]

"""


banner2 = """\033[31m""" + """
                                                                         
                        (                                                
 (       )       )  (   )\                 )     )       )      (   (    
 )\     (     ( /(  )\ ((_)  (   `  )   ( /(    (       (      ))\  )(   
((_)    )\  ' )(_))((_) _    )\  /(/(   )(_))   )\  '   )\  ' /((_)(()\  
| __| _((_)) ((_)_  (_)| |  ((_)((_)_\ ((_)_  _((_))  _((_)) (_))   ((_) 
| _| | '  \()/ _` | | || |  (_-<| '_ \)/ _` || '  \()| '  \()/ -_) | '_| 
|___||_|_|_| \__,_| |_||_|  /__/| .__/ \__,_||_|_|_| |_|_|_| \___| |_|   
                                |_|                                      

\033[35m A simple but efficient email spammer   

\033[38m[---]\033[35m        Email_spammer		       \033[38m[---]
\033[34m[---]\033[35m        Created by: incognito04           \033[34m[---]
\033[35m[---]\033[35m        Version: 2.1.0                    \033[35m[---]
\033[32m[---]\033[33m        Codename:more nicer and efficient \033[32m[---]

"""


banner3 = """\033[35m""" + """

███████╗███╗   ███╗ █████╗ ██╗██╗         ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                        
\033[35m A simple but high speed email spammer   

\033[38m[---]\033[35m        Email_spammer		       \033[38m[---]
\033[34m[---]\033[35m        Created by: incognito04           \033[34m[---]
\033[35m[---]\033[35m        Version: 2.1.0                    \033[35m[---]
\033[32m[---]\033[33m        Codename:more nicer and efficient \033[32m[---]
                        
"""

banner4 = """\033[35m""" + """


▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓         ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░         ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░      ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
   ░  ░       ░         ░  ░ ░      ░  ░         ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                                                             
\033[35m A simple but efficient email spammer   

\033[38m[---]\033[35m        Email_spammer		        \033[38m[---]
\033[34m[---]\033[35m        Created by: incognito04            \033[34m[---]
\033[35m[---]\033[35m        Version: 2.1.0                     \033[35m[---]
\033[32m[---]\033[33m        Codename: more nicer and efficient \033[32m[---]
                        
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

def get_banner():
    banners = [banner1, banner2, banner3, banner4]
    return random.choice(banners)

def name():
    
    blue = '\033[36m'
    
    red = '\033[31m'
      

    
    print get_banner()
 
    
    try:
	try:
	    email = raw_input(blue + 'spammer:username\33[33m>\33[32m email login\33[36m:')
	    password = getpass.getpass('spammer:password\33[33m>\33[32m password for account [BLANK]\33[36m:')
	    spoofed_mail = raw_input('spammer:spoofed email\33[33m>\33[32m spoofed email address\33[36m:')
	    sender = raw_input('spammer:victims_email\33[33m>\33[32m targets email address\33[36m:')
	    msg = raw_input('spammer:message\33[33m >\33[32m message to send\33[36m:')
	    time = int(raw_input('spammer:spam\33[33m>\33[32m amount of times to spam:\33[36m'))
	    server1 = raw_input("""
1. Use a gmail Account for your email attack.
                                  
2. Use your own server or open relay 
				
spammer:option\33[33m>\33[32m choose which option to use\33[36m:""")
	    if server1 == '1':
		print(blue + '\n[*]Logging in using gmail...\n')
	    	server1 = 'smtp.gmail.com'	
		port = '587'
	    if server1 == '2':
	    	server1 = raw_input('\nspammer:server\33[33m>\33[32m name of server to use example [smtp.yourserver.com]:')
		port = int(raw_input('spammer:port>\33[32m port of server example [25]:'))
        except KeyboardInterrupt:
	    print("\n\nGoodbye ;)")
	    sleep(1)
	    exit()
    except ValueError:
	print(red + '\n[*]Make sure you type an number for the amount of times message should be spammed.')
	sleep(2)
	clear()       
	name()
    
    try:
        server = smtplib.SMTP(server1, port)
	server.starttls()
	server.login(email, password)
    except:
	print(red + '\n[-]Make sure you are connected to the internet and that the information you supplied is correct.')
	sleep(2)
	clear()
	name()
    
    try:
	for i in range (0,time):
    		server.sendmail(spoofed_mail, sender, msg)
    	    	print(blue + strftime('\n[%H:%M:%S] [*] Email sent.'))
        server.quit()
    except:
	print(red + '\n[-] Email failed to send.')

    clear() 
	      
    try:
        name()
    except KeyboardInterrupt:
	print(blue + '\n\nGoodbye ;)')
name()
    

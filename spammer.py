#!/usr/bin/python
# -*- coding: utf-8 -*-

# mail spammer by Incognito04

import platform
import smtplib
import getpass
import time
import os

def name():
    print """\033[35m""" + """
                 _ _                                                 
                (_) |                                                
 _ __ ___   __ _ _| |  ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
| '_ ` _ \ / _` | | | / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
| | | | | | (_| | | | \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
|_| |_| |_|\__,_|_|_| |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                          | |                                        
                          |_|                                        

\033[35m A simple but high speed email spammer   

\033[38m[---]\033[35m                 Email_spammer		   \033[38m[---]
\033[34m[---]\033[35m        Created by: incognito04               \033[34m[---]
\033[35m[---]\033[35m                 Version: 1.1.0               \033[35m[---]
\033[32m[---]\033[33m        Codename: Less errors and gliches     \033[32m[---]

 """
    
    try:
	try:
	    email = raw_input('\033[36m' + 'gmail_email_address > ')
	    password = getpass.getpass('password > ')
	    spoofed_mail = raw_input('spoofed email > ')
	    sender = raw_input('email of reciever > ')
	    msg = raw_input('message > ')
	    time = int(raw_input('amount of times to spam > '))
	    server1 = ('smtp.gmail.com')
	    port = ('587')
	except KeyboardInterrupt:
	    print("\n\nGoodbye ;)")
	    exit()
    except ValueError:
	print('\033[31m' + '\n[*]Make sure you type an number for the amount of times message should be spammed.')
        exit()
    
    try:
	server = smtplib.SMTP(server1, port)
	server.starttls()
	server.login(email, password)
    except:
	print('\033[31m' + '\n[-]Make sure you are connected to the internet and that the information you supplied is correct.')
    
    try:
	for i in range (0,time):
    		server.sendmail(spoofed_mail, sender, msg)
        	print('\033[36m' + '\n[*] Mail sent.')
        server.quit()    
    except:
	('\033[31m' + '\n[-] Email failed to send.')

    if platform.system() == ("Linux"):
	os.system("clear")

    if platform.system() == ("Windows"):
	os.system("cls")	
    	
    try:
        name()
    except KeyboardInterrupt:
	print('\033[36m''\n\nGoodbye ;)')
    
	
name()
    

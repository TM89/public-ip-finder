#!/usr/bin/python

from urllib2 import urlopen
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os
import smtplib

#smtp-server setup
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

#mail parameters
username = 'themevik89@gmail.com'
password = ''
fromaddr = 'themevik89@gmail.com'
toaddr = 'themevik89@gmail.com'

#Static subject for this script
subject = 'Public ip changed!'

#getting ip
old_ip = '0.0.0.0'
public_ip = urlopen('http://ip.42.pl/raw').read()
filename = 'publicip.txt'

def sendmail(new_ip):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	body = 'Your public ip has changed and is now: '+public_ip
	msg.attach(MIMEText(body,'plain'))
	
	server.login(username, password)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)

if os.path.isfile(filename):
	file = open(filename,'r+')
	old_ip = file.read()
	file.close()
else:
	file = open(filename,'w')
	file.write(public_ip)
	file.close()
	sendmail(public_ip)
	
if public_ip != old_ip:
	file = open(filename, 'w')
	file.write(public_ip)
	file.close()
	sendmail(public_ip)	 
	
	


#!/usr/bin/python
#Script starts here


import sys,pexpect
import getpass
import time

HOST = '10.10.10.1'
user = 'admin'
password = 'passworc'
TFTPSERVER = '200.200.200.200'

child = pexpect.spawn ('telnet '+HOST) #start telnet session in switch
child.timeout = 30
child.logfile = sys.stdout #display progress of script on screm

time.sleep(2)

child.expect ('User:') #wait user

child.sendline (user+'\r') #send user

child.expect('Password:') #wait password

child.sendline (password+'\r') #send password

child.sendline ('\r')

time.sleep(2)

child.sendline (' enable\n'+'\r') #change mode to enable mode

child.expect('#') #wait # enable mode

child.sendline ('copy startup-config tftp ip-address '+TFTPSERVER+' filename bksw-'+HOST+ '\r') #send command to upload startup-config to TFTP server
time.sleep(2)

child.sendline ('logout \r') #exit switch console

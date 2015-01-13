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

child.expect ('User:')

child.sendline (user+'\r')

child.expect('Password:')

child.sendline (password+'\r')

child.sendline ('\r')

time.sleep(2)

child.sendline (' enable\n'+'\r')

child.expect('#')

child.sendline ('copy startup-config tftp ip-address '+TFTPSERVER+' filename bksw-'+HOST+ '\r')
time.sleep(2)

child.sendline ('logout \r')

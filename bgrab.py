#!usr/bin/env python

# banner.py

import socket
portList = range(1,1024)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP

t_host = str(raw_input("Enter the host name: "))
t_port = int(raw_input("Enter Port: "))

for port in portList:
	
	sock.connect((t_host,t_port))
	sock.send('GET HTTP/1.1 \r\n')

	ret = sock.recv(1024)
	print 'Grabbing 192.168.189.159' + '[+]' + str(ret)
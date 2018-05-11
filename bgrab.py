#!usr/bin/env python

# banner.py

import socket
portList = range(t_port,tt_port)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP

t_host = str(raw_input("Enter the host name: "))
t_port = int(raw_input("Specify port range start : "))
tt_port = int(raw_input("Specify port range stop : "))
sock.connect((t_host,portList))


for port in portList:
	
	sock.send('GET HTTP/1.1 \r\n')

	ret = sock.recv(1024)
	print 'Scanning ports 1-1024'
	print 'Grabbing 192.168.189.159' + '[+]' + str(ret)
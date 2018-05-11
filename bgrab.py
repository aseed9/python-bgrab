#!usr/bin/env python

# banner.py

import socket

def getbanner(ip,port):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
	socket.setdefaulttimeout(4)

	ip = str(raw_input("Enter the host name: "))
	port = int(raw_input("Enter Port: "))

	sock.connect((ip,port))
	sock.send('GET HTTP/1.1 \r\n')

	ret = sock.recv(1024)
	print '[+]' + str(ret)
	return ret

def main():
	banner = getbanner(ip, port)
	return banner

if _name_ == '_main_':
	main()




#!usr/bin/env python

# banner.py

import socket

def retBanner(ip, port):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
	sock.connect((ip,port))
	sock.send('GET HTTP/1.1 \r\n')
	ret = sock.recv(1024)
	print 'Scanning...'
	return ret

def main():
	ip = raw_input('Enter IP : ')
	portList = [21,22,25,80,110,443]
	for port in portList:
		banner = retBanner(ip, port)
		if banner:
			print '[+]' + str(ip) + ':' + str(port) + '- ' + banner
		else :
			banner = 'No banner recieved'
			print '[+]' + str(ip) + ':' + str(port) + '- ' + banner

if __name__ == '__main__':
    	main() 
		
	
import socket

print('Banner Grabbing // v1.0')
print('- Coded by aseed9 irc.anonops.com:6697')
ans = True
p = [21,22,25,80,110,443]

while ans:

    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "https://bing.com"}
    print ("""
  - Menu Selection -
  1. Manual
  2. Automatic List
  3. Add to list
  4. Exit
           """)
    ans = input('Select Option : ')

    if ans =="1":
        try:
            ip = input('Target IP : ')
            port = input('Target Port : ')
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect(ip, port)
            banner = s.recv(1024)
            f = open(grablist.txt, a)
            f.write(banner)
            print('Banner saved. ')
            ans == True
                     
        except :
                print('##Error. Target is offline or port is not open.')

    if ans =="2":
        try:
            ip = input('Enter Target IP : ')
            for port in p:

                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect(ip, p)
                banner = s.recv(1024)

                if banner == s.recv(1024):
                    
                    f = open('grablist.txt', a)
                    f.write(banner)
                    print('Banner saved. ')
                    ans == True
                
        except :
                print('##Error. Target is offline or a port is closed.')


    if ans =="3":
        try :
            addport = int(input('Enter port to append in list : '))
            p.append(addport)
            print('Port added to list.')
            
        except :
            print('##Error when adding port to list.')

    if ans=="4":
          quit()
    else:
          ans = True
            
        







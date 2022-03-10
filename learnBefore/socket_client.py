#coding:utf-8
import socket

IP_PORT = ('127.0.0.1', 9999)

sk = socket.socket()

sk.connect(IP_PORT)
while True:
    inp = input("请输入你要发送的信息")
    sk.sendall(inp.encode())

sk.close()


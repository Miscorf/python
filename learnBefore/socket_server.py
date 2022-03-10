import socket
import threading


def  link_handler(link,address):
    print('来自%s：%s的连接'% (address[0],address[1]))
    while True:
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print("结束与%s%s的通信"% (address[0],address[1]))
            break
        print('来自%s：%s的发来的信息%s'% (address[0],address[1],client_data))
        link.sendall('服务器已经收到你的信息'.encode())


IP_PORT = ('127.0.0.1', 9999)

sk = socket.socket()
sk.bind(IP_PORT)
sk.listen(5)


while True:
    conn,address=sk.accept()
    t = threading.Thread(target=link_handler,args=(conn,address))
    t.start()


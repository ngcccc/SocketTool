import socket
#创建socket对象
#SOCK_DGRAM    udp模式
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8340))  #绑定服务器的ip和端口

while True:
    data=server.recv(1024)  #一次接收1024字节
    print(data.decode())# decode()解码收到的字节
server.close()
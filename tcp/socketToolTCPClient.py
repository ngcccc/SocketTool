#-*-coding:utf-8-*-
import socket
client=socket.socket()#默认famliy=AF_INET(ipv4)地址簇  type=SOCK_STREAM (tcp/ip) 声明socket类型，同时生成socket连接对象
client.connect(("localhost",8340))

while True:
    msg=input("请输入:").strip()  #不能发送空数据
    if len(msg)==0:continue    #如果msg长度为0，就继续 ，重新发
    client.send(msg.encode("utf-8")) #3.x 只能发bytes类型数据，只能接收ASCII数据，汉字不行,要发汉字只能编码成utf-8格式
    data=client.recv(102400) #收102400字节数据
    print(data.decode("utf-8")) #bytes类型打印出来要解码

client.close()
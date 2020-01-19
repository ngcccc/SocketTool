#-*-coding:utf-8-*-
import socket
import struct

#将16进制数据当做字节流传递
def dataSwitch(data):
    str1 = ""
    str2 = "".encode("utf-8")
    while data:
        str1 = data[0:2]
        s = int(str1,16) #字符转换为16进制
        str2 += struct.pack('B',s) #转为字节流
        data = data[2:] #分割字符串，去掉字符串前两个字符
    return str2

#client=socket.socket()#默认famliy=AF_INET(ipv4)地址簇  type=SOCK_STREAM (tcp/ip) 声明socket类型，同时生成socket连接对象
#SOCK_DGRAM udp
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=input("请输入:").strip()  #不能发送空数据
    if len(msg)==0:continue    #如果msg长度为0，就继续 ，重新发
    client.sendto(dataSwitch(msg),("localhost",8340))
    #data=client.recv(102400) #收102400字节数据
    #print(data.decode("utf-8")) #bytes类型打印出来要解码

client.close()
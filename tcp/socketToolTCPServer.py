import socket
import os
server = socket.socket()
server.bind(('localhost',8340)) #绑定要监听地址和端口  如果是监听所有
server.listen(5) #监听

print("我要开始等电话了")
while True:
    conn, addr = server.accept()  # 等电话打进来      conn:服务端生成的实例,接受新实例,addr:客户端的地址
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    print("电话来了")
    # count = 0
    while True:
        data = conn.recv(1024)  #8192
        print("recv:",data)
        if not data:                             ###如果不判断，当client断开之后，server 就会死循环接受空数据.
            print("client has lost...")
            break
        # conn.send(data.upper())
        res = os.popen(data.decode("utf-8")).read()
        print(len(res))
        if len(res)==0:
            res="res is empty"
            # res=b"res has empty"

        #res = os.popen(data).read()   ###如果这么写就会报错。
       
        conn.send(str(len(res.encode())).encode("utf-8"))             ##发送到client数据的size
        client_ack = conn.recv(1024)                                  ##这两行是为了防止粘包
        print("准备发送了",client_ack.decode("utf-8"))
        conn.send(res.encode("utf-8"))
        # conn.send(res)                ###如果这么写就会报错
        
        # count+=1
        # if count >10:break

server.close()
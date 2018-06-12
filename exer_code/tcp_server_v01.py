import socket

def tcp_srv():
    # 1. 建立socket负责通讯，这个socket其实只负责接受对方的请求，真正通信的是链接后。。。。
    # 需要用到两个参数
    # AF_INET: 含义通udp一样（需要去看看）
    # SOCK_STREAM: 表明是使用的tcp进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定端口和地址
    addr = ("127.0.0.1", 10111)
    sock.bind(addr)
    # 3. 监听接入的访问socket
    sock.listen()

    while True:
        # 4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
        # accept 返回的是一个元组
        skt,addr = sock.accept()
        # 5. 接受对方的发送内容，利用接收到的 socket 接收内容
        # 500表示接收使用的buffer
        msg = skt.recv(500)

        dmsg = msg.decode()

        rst = "Receive msg: {0} from {1}".format(dmsg, addr)
        print(rst)
        # 6.如有必要，给对方发送反馈信息
        skt.send(rst.encode())

        # 7. 关闭链接通路
        skt.close()


if __name__ == "__main__":
    print("Start TCP server...........")
    tcp_srv()
    print("Stop TCP server...........")
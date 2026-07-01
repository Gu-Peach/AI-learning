# socket（套接字）是同一或不同电脑的进程（任务、应用软件）间通信的一个工具，进程之间想要进行网络通信需要基于socket。只要与网络相关的应用程序或者软件都使用到了socket。
# 套接字就是操作系统提供给程序的一种通信接口，可以把它理解成“网络通信的句柄”或者“通信端点”。

# 更直白一点：

# 进程想通过网络发消息，不能直接对着另一台机器“说话”
# 它要先创建一个 socket
# 然后通过这个 socket 连接对方、发送数据、接收数据
# 所以 socket 不是网络本身，而是程序访问网络的一种方式。

# 常见两类：

# TCP socket：面向连接，像打电话，先建立连接再通信
# UDP socket：无连接，像发快递，直接发出去，不保证一定到达
# 你在 Python 里看到的 socket，通常就是在做这些事：

# 创建套接字
# 绑定端口
# 监听连接
# 接收连接
# 发送和接收数据

# 使用
import socket

# AF_INET 用于 Internet 进程间通信；SOCK_STREAM 流式套接字，TCP
tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# AF_INET 用于 Internet 进程间通信；SOCK_DGRAM 数据报套接字，UDP
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 你如果直接打印它，常见会看到类似这样的形式：

# 或者 UDP 的类似输出：
<socket.socket fd=3, family=2, type=1, proto=0, laddr=('0.0.0.0', 0)>
# 这里几个字段可以这样理解：
<socket.socket fd=4, family=2, type=2, proto=0, laddr=('0.0.0.0', 0)>
# fd：文件描述符，操作系统分配的句柄编号
# AF_INET 是地址族，表示使用 IPv4 网络地址。

# 简单说，它告诉 socket：

# 我要用哪一类地址来通信
# AF_INET 就是用 IPv4，比如 127.0.0.1 这种形式
# family=2：表示 AF_INET
# type=1：表示 SOCK_STREAM，也就是 TCP
# type=2：表示 SOCK_DGRAM，也就是 UDP
# laddr：本地地址，刚创建时通常还没绑定，所以端口是 0
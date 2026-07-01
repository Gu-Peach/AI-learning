import socket

# AF_INET 用于 Internet 进程间通信；SOCK_STREAM 流式套接字，TCP
tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# AF_INET 用于 Internet 进程间通信；SOCK_DGRAM 数据报套接字，UDP
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

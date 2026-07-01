# UDP 编程

# 下面这张图展示了 UDP 服务端和客户端的基本通信流程。

# ![UDP 通信流程图](./udp.png)

# ## 流程说明

# UDP 是无连接协议，所以它和 TCP 不同，不需要先建立连接再通信。双方只要创建好套接字，就可以直接收发数据。

# ### 1. 服务端

# 1. `socket()`：创建 UDP 套接字。
# 2. `bind()`：绑定本机 IP 和端口，表示这个程序要在这个地址上等待数据。
# 3. `recvfrom()`：接收客户端发来的数据，并返回数据内容和发送方地址。
# 4. `sendto()`：把数据发回给客户端。
# 5. `close()`：关闭套接字，释放资源。

# ### 2. 客户端

# 1. `socket()`：创建 UDP 套接字。
# 2. `sendto()`：直接向服务端的 IP 和端口发送数据。
# 3. `recvfrom()`：接收服务端返回的数据。
# 4. `close()`：关闭套接字，释放资源。

# ## 结合图片理解

# 这张图里，左边是 UDP 服务端，右边是 UDP 客户端：

# - 服务端先 `bind()`，把自己固定到某个地址上，方便客户端找到它。
# - 客户端不需要 `connect()`，可以直接用 `sendto()` 把数据发给服务端。
# - 服务端收到数据后，再用 `sendto()` 把响应发回去。
# - 双方每次通信都可以独立完成，不需要像 TCP 那样维持一条长连接。

# ## 特点

# - 不需要建立连接，通信开销小。
# - 发送速度快，但不保证一定送达。
# - 不保证顺序，也不保证不重复。
# - 适合对实时性要求高、对丢包容忍度较高的场景，比如语音、视频、直播等。


## 案例
"""udp服务端"""

import socket

# 创建udp套接字
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 绑定ip和端口
# 服务端 bind(("127.0.0.1", 8080)) 绑定的是服务端自己这台机器上的本地 IP 和端口
udp_socket.bind(("127.0.0.1", 8080))
while True:
  # 接收数据
    #   udp_socket.recvfrom(1024) 是“接收 UDP 数据”的方法。

    # 它的作用是：

    # 从这个 UDP 套接字里接收数据
    # 最多接收 1024 字节
    # 返回两个值：
    # 接收到的数据
    # 数据是从哪个地址发来的
  recv_data, client_addr = udp_socket.recvfrom(1024)
  client_ip = client_addr[0]
  client_port = client_addr[1]
  print(f"{client_ip}:{client_port}>> {recv_data.decode("utf-8")}")
  # 发送数据
  udp_socket.sendto("你好".encode("utf-8"), client_addr)
# 关闭套接字
udp_socket.close()



"""udp客户端"""

import socket

# 创建udp套接字
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while True:
  try:
    # 发送数据
    server_ip = "127.0.0.1"
    server_port = 8080
    udp_socket.sendto(input(f"{server_ip}:{server_port}<< ").encode("utf-8"), (server_ip, server_port))
    # 接收数据
    recv_data, client_addr = udp_socket.recvfrom(1024)
    client_ip = client_addr[0]
    client_port = client_addr[1]
    print(f"{client_ip}:{client_port}>> {recv_data.decode("utf-8")}")
  except KeyboardInterrupt:
    break
# 关闭套接字
udp_socket.close()
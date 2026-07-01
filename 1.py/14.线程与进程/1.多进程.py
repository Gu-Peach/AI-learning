# 进程是操作系统进行资源分配的基本单位。
# 操作系统中一个正在运行的程序或软件就是一个进程。
# 每个进程都有自己独立的一块内存空间。
# 一个进程崩溃后，在保护模式下不会对其他进程产生影响。
# 多进程是指在操作系统中同时运行多个程序

## 1.使用multiprocessing.Process创建进程（py提供的一个跨平台的多进程模块），multiprocessing 模块提供了一个 Process 类来代表一个进程对象
# 1）process创建
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# group：应当始终为 None，它的存在仅是为了与 threading.Thread 兼容。
# target：由 run() 方法来发起调用的可调用对象，默认为 None。
# name：进程名称，默认为 None 则自动分配。
# args：针对目标调用的参数元组。
# kwargs：针对目标调用的关键字参数字典。
# daemon：是否为守护进程，True 或 False。默认为None则继承父进程。

# 2）Process 的属性和方法与其他常用方法
# name：获取进程名称。
# pid：获取进程号。
# daemon：判断或设置进程是否为守护进程。
# exitcode：获取子进程的退出状态码。
# start()：启动进程，调用传入 target 的对象。start() 只能被调用一次。
# run()：默认调用传入 target 的对象，如果子类化了 Process，可以重写此方法来自定义行为。
# join([timeout])：阻塞主进程，直到子进程结束或超时。timeout参数可选，意为阻塞多少秒。
# terminate()：强制终止子进程。
# kill()：杀死进程，与 terminate() 类似，但更彻底。
# is_alive()：检查进程是否仍在运行。
# os.getpid()：获取当前进程编号。
# os.getppid()：获取当前进程的父进程编号。


# case：同时读写文件
import time
import multiprocessing

# 向文件中写入数据
def write_file():
  with open("test.txt", "a") as f:
    while True:
      f.write("hello world\n")
      f.flush()
      time.sleep(0.5)

# 从文件中读取数据
def read_file():
  with open("test.txt", "r") as f:
    while True:
      time.sleep(0.1)
      print(f.read(1))

if __name__ == "__main__":
  # 创建一个子进程用于写文件
  p1 = multiprocessing.Process(target=write_file)
  # 创建一个子进程用于读文件
  p2 = multiprocessing.Process(target=read_file)
  # 启动子进程
  p1.start()
  # 启动子进程
  p2.start()


# 自定义Process子类创建进程
import os
import multiprocessing

class Worker(multiprocessing.Process):
  def run(self):
    print("进程id：", os.getpid(), "\t父进程id：", os.getppid())

if __name__ == "__main__":
  for i in range(5):
    p = Worker()
    p.start()



## 2.进程池
# 1）创建
multiprocessing.Pool([processes[,initializer[,initargs[,maxtasksperchild[,context]]]]])
# 这是文档里的可选参数表示法，不是 Python 代码。方括号表示“可选”，逗号仍然是参数之间的分隔符，所以看起来像是在方括号前有逗号。换成真实的函数签名更清晰：
# 等价且可运行的签名：
# multiprocessing.Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None, context=None)

# processes：要使用的工作进程数量。如果 processes 为 None 则使用 os.cpu_count() 所返回的数值。
# initializer：如果不为 None，则每个工作进程将会在启动时调用 initializer(*initargs)。
# maxtasksperchild：一个工作进程在它退出或被一个新的工作进程代替之前能完成的任务数量，为了释放未使用的资源。默认的 maxtasksperchild 是 None，意味着工作进程寿与池齐。
# context：可被用于指定启动的工作进程的上下文。通常一个进程池是使用函数 multiprocessing.Pool() 或者一个上下文对象的 Pool() 方法创建的。

# 2）进程池常用方法
# apply(func[, args[, kwds]])：使用 args 参数以及 kwds 命名参数同步调用 func , 在返回结果前阻塞。另外 func 只会在一个进程池中的一个工作进程中执行。
# apply_async(func[, args[, kwds[, callback[, error_callback]]]])：使用 args 参数以及 kwds 命名参数异步调用 func，并立即返回一个 AsyncResult 对象，不会阻塞。可以通过 callback 获取结果和通过 error_callback 处理异常。
# close()：阻止后续任务提交到进程池，当所有任务执行完成后，工作进程会退出。
# terminate()：不必等待未完成的任务，立即停止工作进程。当进程池对象被垃圾回收时，会立即调用 terminate()。
# join()：阻塞主进程，等待工作进程结束。调用 join() 前必须先调用 close() 或者 terminate()。

# 3）case
import os
import time
import multiprocessing

# 打印10个数字,每次间隔0.5秒
def func():
  for i in range(10):
    print(os.getpid(), i)
    time.sleep(0.5)

if __name__ == "__main__":
  # 指定进程池大小
  process_num = 5
  pool = multiprocessing.Pool(process_num)
  for p in range(process_num):
    # 阻塞式
    # pool.apply(func)
    # 非阻塞式
    pool.apply_async(func)
  pool.close()
  pool.join()
  print("end")


## 3.进程间通信
# 1）进程间不共享全局变量
import os
import multiprocessing

# 向list1中添加10个元素
def func(list1):
  for i in range(10):
    list1.append(i)
    print(os.getpid(), list1)

if __name__ == "__main__":
  list1 = []
  p1 = multiprocessing.Process(target=func, args=(list1,))
  p2 = multiprocessing.Process(target=func, args=(list1,))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print(os.getpid(), list1)
#   p1.join() / p2.join() 让父进程等待子进程结束。子进程结束后，父进程执行最后一行 print(os.getpid(), list1)，这时 os.getpid() 返回的是父进程的 PID，list1 仍然是父进程自己的空列表。
# 45448 [0]
# 45448 [0, 1]
# 45448 [0, 1, 2]
# 45448 [0, 1, 2, 3]
# 45448 [0, 1, 2, 3, 4]
# 45448 [0, 1, 2, 3, 4, 5]
# 45448 [0, 1, 2, 3, 4, 5, 6]
# 45448 [0, 1, 2, 3, 4, 5, 6, 7]
# 45448 [0, 1, 2, 3, 4, 5, 6, 7, 8]
# 45448 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 45449 [0]
# 45449 [0, 1]
# 45449 [0, 1, 2]
# 45449 [0, 1, 2, 3]
# 45449 [0, 1, 2, 3, 4]
# 45449 [0, 1, 2, 3, 4, 5]
# 45449 [0, 1, 2, 3, 4, 5, 6]
# 45449 [0, 1, 2, 3, 4, 5, 6, 7]
# 45449 [0, 1, 2, 3, 4, 5, 6, 7, 8]
# 45449 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 45446 []


# 2）使用queue通信
# multiprocessing.Queue([maxsize]) 返回一个使用一个管道和少量锁和信号量实现的共享队列（先进先出）实例。当一个进程将一个对象放进队列中时，一个写入线程会启动并将对象从缓冲区写入管道中。默认队列是无限大小的，可以通过 maxsize 参数限制。
# queue的常用方法
# qsize()：返回队列的大致长度。由于多线程或者多进程的上下文，这个数字是不可靠的。
# empty()：如果队列是空的返回 True。由于多线程或多进程的环境，该状态是不可靠的。
# full()：如果队列是满的返回 True。由于多线程或多进程的环境，该状态是不可靠的。
# put(obj[, block[, timeout]])：将 obj 放入队列。如果可选参数 block 是 True（默认值）而且 timeout 是 None（默认值），将会阻塞当前进程，直到有空的缓冲槽。如果 timeout 是正数，将会在阻塞了最多 timeout 秒之后还是没有可用的缓冲槽时抛出 queue.Full 异常。反之（block 是 False 时），仅当有可用缓冲槽时才放入对象，否则抛出 queue.Full 异常（在这种情形下 timeout 参数会被忽略）。
# put_nowait(obj)：相当于 put(obj, False)。
# get([block[, timeout]])：从队列中取出并返回对象。如果可选参数 block 是 True （默认值）而且 timeout 是 None（默认值），将会阻塞当前进程，直到队列中出现可用的对象。如果 timeout 是正数，将会在阻塞了最多 timeout 秒之后还是没有可用的对象时抛出 queue.Empty 异常。反之（block 是 False 时），仅当有可用对象能够取出时返回，否则抛出 queue.Empty 异常（在这种情形下 timeout 参数会被忽略）。
# get_nowait()：相当于 get(False)。

# 两个进程分别读写Queue
# 通过队列让两个进程之间同步数据
import time
import random
import multiprocessing

# 间隔随机时间向queue中放入随机数
def func1(queue):
  while True:
    queue.put(random.randint(1, 50))
    time.sleep(random.random())

# 从queue中取出数据
def func2(queue):
  while True:
    print("=" * queue.get())

if __name__ == "__main__":
  queue = multiprocessing.Queue()
  p1 = multiprocessing.Process(target=func1, args=(queue,))
  p2 = multiprocessing.Process(target=func2, args=(queue,))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
# 对于单个 multiprocessing.Process（你在 test.py 中的 p1,p2）：直接调用 p.start() 后，父进程可以直接 p.join() 等待子进程自然结束；不需要先 terminate() 或 close()。terminate() 是强制终止的方法，只有当你想提前结束子进程时才用。
# 对于 multiprocessing.Pool：pool.join() 要求先调用 pool.close()（表示不再接受新任务）或 pool.terminate()（立即停止所有 worker），否则 join() 会报错或永远阻塞。你在 1.多进程.py 已正确先 pool.close() 再 pool.join()。
# join() 的语义（简短）

# Process.join([timeout])：阻塞父进程，直到该子进程结束或超时；不终止子进程，只是等待。可以用 timeout 做有限等待，之后可检查 p.is_alive()。
# join() 的作用：阻塞父进程（或线程），直到指定子进程结束或到达超时。它不是终止子进程，只是“等待并回收/同步”。
# 不写 join() 会怎样：
# 父进程会立即继续执行后续代码（不会等待子进程完成）。
# 如果父进程随后退出：子进程通常会被重父（reparent）到系统 init/服务管理进程并继续运行（UNIX/macOS），不会自动被杀死；但你也会失去从父进程收集结果或状态的机会。
# 如果父进程在子进程退出前仍存活但不调用 join()，已退出的子进程会变成“僵尸进程”（zombie）直到父进程调用 join()/wait() 回收它们（由操作系统清理僵尸需要父进程做等待，或父进程自己退出让 init 回收）。

# 3）进程之间使用Manager().Queue 通信
import time
import random
import multiprocessing

# 间隔随机时间向queue中放入随机数
def func1(queue):
  while True:
    queue.put(random.randint(1, 50))
    time.sleep(random.random())

# 从queue中取出数据
def func2(queue):
  while True:
    print("=" * queue.get())

if __name__ == "__main__":
  queue = multiprocessing.Manager().Queue()
  pool = multiprocessing.Pool(2)
  pool.apply_async(func1, (queue,))
  pool.apply_async(func2, (queue,))
  pool.close()
  pool.join()
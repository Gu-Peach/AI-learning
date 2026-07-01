# 线程是处理器任务调度和执行的基本单位。
# 一个进程至少有一个线程，也可以运行多个线程。
# 多个线程之间可共享数据。
# 线程运行出错异常后，如果没有捕获，会导致整个进程崩溃。
# 多线程是指在同一进程中同时执行多个任务。


## 1.使用threading.Thread模块创建线程
# Python的标准库提供了两个模块：_thread 和 threading，_thread 是低级模块，threading是高级模块，对 _thread 进行了封装。绝大多数情况下，我们只需要使用 threading 这个高级模块。
# 1) thread的创建
threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# group：应为 None，保留给将来实现 ThreadGroup 类的扩展使用。
# target：用于 run() 方法调用的可调用对象。默认是 None，表示不需要调用任何方法。
# name：线程名称。 在默认情况下，会以 “Thread-N” 的形式构造唯一名称，其中 N 为一个较小的十进制数值，或是 "Thread-N (target)" 的形式，其中 “target” 为 target.__name__，如果指定了 target 参数的话。
# args：用于发起调用目标函数的参数列表或元组。 默认为 ()。
# kwargs：用于调用目标函数的关键字参数字典。默认是 {}。
# daemon：True 或 False 来设置该线程是否为守护模式。如果是 None （默认值），线程将继承当前线程的守护模式属性。

# 2) thread的属性方法
# name：线程的名称。
# daemon：线程是否为守护线程。
# ident：线程标识符。
# native_id：此线程的线程id（tid），由 OS（内核）分配。
# start()：启动线程，调用线程的 run() 方法。
# run()：定义线程的行为，默认调用传入的 target 对象。
# join([timeout=None])：阻塞主线程，直到当前线程运行完成或达到超时时间。
# is_alive()：线程是否在运行。
# threading.enumerate()：查看都有哪些线程。
# threading.current_thread()：返回当前线程实例。

# 3）case：两线程分别交替打印
import time
import threading

# 交替打印 00000 和 11111
def func():
  flag = 0
  while True:
    print(threading.current_thread().name, f"{flag}" * 5)
    flag = flag ^ 1 # 替换0和1
    time.sleep(0.5)

if __name__ == "__main__":
  t1 = threading.Thread(target=func, name="线程1")
  t2 = threading.Thread(target=func, name="线程2")
  t1.start()
  t2.start()
# 线程1 00000
# 线程2 00000
# 线程1 11111
# 线程2 11111
# 线程2 00000
# 线程1 00000
# 线程2 11111
# 线程1 11111
# 线程2 00000
# ........


## 2.自定义Thread子类创建线程
import time
import threading

class Worker(threading.Thread):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def run(self):
    flag = 0
    while True:
      print(f"\r{self.name}:{str(flag)*5}", end="")
      flag = flag ^ 1 # 替换0和1
      time.sleep(0.2)

if __name__ == "__main__":
  t1 = Worker("线程1")
  t2 = Worker("线程2")
  t1.start()
  t2.start()


## 3.线程池
# ThreadPoolExecutor 是 concurrent.futures 模块中的线程池实现，它允许我们轻松地提交任务到线程池，并管理任务的执行和结果。
# 1）线程池的创建
concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix="", initializer=None, initargs=())
# max_workers：线程池的最大线程数（默认取决于系统资源）。
# thread_name_prefix：线程名称前缀。
# initializer：可选的初始化函数。
# initargs：传递给初始化函数的参数。

# 2）线程池的常用方法
# submit(fn, *args, **kwargs)：提交一个任务到线程池，返回一个 Future 对象。可使用 Future.result() 获取任务结果。
# map(func, *iterables, timeout=None, chunksize=1)：类似于内置的 map() 函数，但在线程池中并行执行。Iterables为可迭代对象，传递给目标函数。chunksize 对 ThreadPoolExecutor 没有效果。
# shutdown(wait=True, cancel_futures=False)：关闭线程池，等待所有任务完成。wait 表示是否等待线程池中的所有线程完成任务。cancel_futures 表示是否取消尚未开始的任务。

# case
import concurrent.futures


def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end="")
    return word


if __name__ == "__main__":
    word = list("idmmn!vnsme")
    # 使用 with 语句来确保线程被迅速清理
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 注册三个任务并提交到线程池中执行
        future1 = executor.submit(func, "线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")
        # 等待结果
        # 如果任务还没执行完，就阻塞等待
        # 如果任务已经结束，就直接取返回值
        word = future1.result()
        word = future2.result()
        word = future3.result()
print("".join(word))  # hello world
# 流程：从这个结果来看就是，线程1先跑，然后某一时刻资源分配给了线程2，由于线程1刚刚已经对我让的重新赋值，然后线程2 就基于新值从word[0]开始处理，下一次资源又分给了线程1，线程1还是根据它当前的i来处理，依次类推
# 切换不是按“某一时刻刚好把资源完整交给另一个线程”这么整齐，而是操作系统在很多执行点都可能切走。对这段代码来说，线程1 可能先跑了几次，改了共享列表里的几个元素，然后被切到线程2。线程2 的确会从自己这次循环的 i=0 开始，基于当时共享的 word 当前状态继续改。

# 这种情况就是典型的共享可变数据竞争，通常需要互斥锁来保护。

# 你这段代码里，多个线程同时读写同一个 word 列表，问题不在“线程名一样”，而在“多个线程同时改同一个对象”。这会导致：

# 读到的值可能已经被别的线程改过
# 写入顺序不可预测
# 最终结果依赖调度，不能稳定复现
# 逻辑上看起来就像“线程互相干扰”

# 线程1: ['h', 'd', 'm', 'm', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程1: ['h', 'e', 'm', 'm', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程1: ['h', 'e', 'l', 'm', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程2: ['i', 'e', 'l', 'm', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程1: ['i', 'e', 'l', 'l', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程1: ['h', 'd', 'l', 'l', 'o', '!', 'v', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'l', 'l', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'l', 'o', '!', 'v', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'o', '!', 'v', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'n', ' ', 'v', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'n', ' ', 'w', 'n', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'n', ' ', 'w', 'o', 's', 'm', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'n', ' ', 'w', 'o', 'r', 'm', 'e']
# 线程1: ['h', 'd', 'm', 'm', 'n', '!', 'w', 'o', 'r', 'l', 'e']
# 线程3: ['h', 'e', 'l', 'l', 'n', '!', 'v', 'n', 's', 'm', 'e']
# 线程1: ['h', 'd', 'm', 'm', 'n', '!', 'v', 'o', 'r', 'l', 'e']
# 线程1: ['h', 'e', 'm', 'm', 'n', '!', 'v', 'n', 'r', 'l', 'e']
# 线程3: ['h', 'e', 'm', 'm', 'n', '!', 'v', 'o', 'r', 'l', 'e']
# 线程2: ['h', 'd', 'm', 'm', 'n', ' ', 'w', 'o', 'r', 'l', 'e']
# 线程3: ['h', 'e', 'l', 'm', 'n', '!', 'v', 'n', 'r', 'l', 'e']
# 线程2: ['h', 'e', 'l', 'm', 'n', '!', 'v', 'n', 'r', 'l', 'd']
# 线程3: ['h', 'e', 'l', 'l', 'n', '!', 'v', 'n', 'r', 'l', 'd']
# 线程3: ['h', 'e', 'l', 'l', 'o', '!', 'v', 'n', 'r', 'l', 'd']
# 线程1: ['h', 'e', 'l', 'l', 'o', '!', 'v', 'n', 's', 'l', 'd']
# 线程3: ['h', 'e', 'l', 'l', 'o', ' ', 'v', 'n', 's', 'l', 'd']
# 线程3: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'n', 's', 'm', 'd']
# 线程1: ['h', 'e', 'l', 'l', 'o', ' ', 'v', 'n', 's', 'm', 'd']
# 线程3: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 's', 'm', 'd']
# 线程1: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 's', 'm', 'e']
# 线程3: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'm', 'e']
# 线程3: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'e']
# 线程3: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# hello world


## 互斥锁
# 1）线程安全问题
# 线程之间共享数据会存在线程安全的问题。上面的案例是一个。再如下
import time
import threading

def func():
  global g_num
  for _ in range(10):
    tmp = g_num + 1
    # time.sleep(0.01)
    g_num = tmp
    print(f"{threading.current_thread().name}: {g_num}\n", end="")

if __name__ == "__main__":
  g_num = 0
  # 一次性创建了 3 个线程对象，放进列表里
  threads = [threading.Thread(target=func, name=f"线程{i}") for i in range(3)]
  [t.start() for t in threads]
  # 住线程阻塞，直到三个线程跑完
  [t.join() for t in threads]
  print(g_num) # 30
  # 结果为30，看似没有问题，这是因为这个修改操作花费的时间太短了，短到我们无法想象。所以，线程间轮询执行时，都能获取到最新的 g_num 值。因此暴露问题的概率就变得微乎其微。
  # 我们添加0.01秒的延迟时间：
import time
import threading

def func():
  global g_num
  for _ in range(10):
    tmp = g_num + 1
    time.sleep(0.01)
    g_num = tmp
    print(f"{threading.current_thread().name}: {g_num}\n", end="")

if __name__ == "__main__":
  g_num = 0
  threads = [threading.Thread(target=func, name=f"线程{i}") for i in range(3)]
  [t.start() for t in threads]
  [t.join() for t in threads]
  print(g_num) # 10

  # 可以看到最终结果并不是30。这是因为在修改 g_num 前，有0.01秒的休眠时间，某个线程延时后，CPU立即分配计算资源给其他线程。此时0.01秒的休眠还未结束，这个线程还未将修改后的数据赋值给 g_num，因此其他线程获取到的并不是最新值，所以才出现上面的结果。
  # 线程2: 1
  # 线程0: 1
  # 线程1: 1
  # 线程1: 2
  # 线程0: 2
  # 线程2: 2
  # 线程1: 3
  # 线程0: 3
  # 线程2: 3
  # 线程1: 4
  # 线程2: 4
  # 线程0: 4
  # 线程1: 5
  # 线程2: 5
  # 线程0: 5
  # 线程1: 6
  # 线程2: 6
  # 线程0: 6
  # 线程1: 7
  # 线程2: 7
  # 线程0: 7
  # 线程1: 8
  # 线程2: 8
  # 线程0: 8
  # 线程2: 9
  # 线程1: 9
  # 线程0: 9
  # 线程2: 10
  # 线程1: 10
  # 线程0: 10
  # 10


# 2）互斥锁的概念
# 某个线程要更改共享数据时，先将其锁定，此时其他线程不能更改。直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。

# 3）使用
# 可以通过 threading.Lock() 创建互斥锁。
# 使用 lock.acquire([blocking=True][, timeout=-1]) 来获取锁（blocking 如果为 True，线程会阻塞直到获取到锁。如果为 False，线程立即返回。获取锁成功返回 True，否则返回 False。timeout 为等待的超时时间，单位为秒。如果超时仍未获取到锁，则返回 False。）。
# 使用 lock.release() 释放锁。
import time
import threading

def func():
  global g_num
  for _ in range(10):
    lock.acquire() # 获取锁
    tmp = g_num + 1
    time.sleep(0.01)
    g_num = tmp
    lock.release() # 释放锁
    print(f"{threading.current_thread().name}: {g_num}\n", end="")

if __name__ == "__main__":
  g_num = 0
  lock = threading.Lock() # 创建锁
  threads = [threading.Thread(target=func, name=f"线程{i}") for i in range(3)]
  [t.start() for t in threads]
  [t.join() for t in threads]
  print(g_num) # 30

  # 线程1 第一次执行到 lock.acquire() 时，如果锁是空闲的，就会立刻拿到锁
  # 线程1 拿到锁之后继续往下执行
  # 其他线程也可能运行到 lock.acquire()，但因为锁已经被线程1占着，它们会在这里阻塞等待
  # 等线程1 执行完并调用 lock.release()，其他线程才有机会继续争抢这把锁

  # lock.acquire() 只会让“抢不到锁”的那个线程阻塞等待，不会把整个程序卡住。
  # 所以当线程2在等锁时，线程3仍然可能被操作系统调度去运行，甚至也走到 lock.acquire()，然后同样等待。线程1释放后2和3会竞争锁
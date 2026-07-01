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
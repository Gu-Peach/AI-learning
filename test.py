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
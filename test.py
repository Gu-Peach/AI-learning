import time
import threading

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

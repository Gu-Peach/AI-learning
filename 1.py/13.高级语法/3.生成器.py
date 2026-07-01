# 生成器（generator）是一个用于创建迭代器的简单而强大的工具。它的写法类似于标准的函数，但当它要返回数据时会使用 yield 语句。当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后的表达式作为当前迭代的值返回。
# 每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行（它会记住上次执行语句时的所有数据值），直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。

# 创建生成器
# 1）使用推导式创建生成器
# 调用for循环进行迭代，函数会从上次暂停的地方继续执行
generator = (x for x in range(5)) # 创建生成器，这是个生成器对象，可通过tuple(generator) 转换为元组
print(generator) # <generator object <genexpr> at 0x0000026C2066CB80>
for x in generator:
  print(x)

# 2）使用函数创建生成器
# 这个过程可以理解为“生成器保存现场，next 让它继续往下跑一步”。

# 你这段代码里，fibo() 不是普通函数，而是生成器函数，因为里面有 yield。调用 f = fibo() 时，并不会立刻执行完整个函数，只是创建了一个生成器对象，函数体此时还没真正开始跑。

# 运行时的过程是这样的：

# 第一次调用 next(f)：

# 函数从头开始执行
# a = 0, b = 1
# 进入 while True
# 执行到 yield b，先把当前的 b，也就是 1，返回出去
# 函数暂停在 yield 这一行，a 和 b 还没有执行更新
# 第二次调用 next(f)：

# 生成器从上次暂停的位置继续
# 这一次先执行 yield 后面的下一句：a, b = b, a + b
# 这里相当于把 a 变成 1，b 还是 1
# 然后再次进入下一轮 while True
# 再执行到 yield b，返回 1
# 第三次调用 next(f)：

# 从暂停处继续
# 先更新 a, b = b, a + b
# 这次 a 变成 1，b 变成 2
# 再 yield b，返回 2
# 后面同理，所以输出顺序就是：
# 1
# 1
# 2
# 3
# 5
def fibo(): # 斐波那契数列
  a, b = 0, 1
  while True:
    yield b
    a, b = b, a + b

f = fibo()
print(next(f)) # 1
print(next(f)) # 1
print(next(f)) # 2
print(next(f)) # 3
print(next(f)) # 5
# 如果我们要获取生成器中 return 的值，我们需要捕获 StopIteration异常：
def fibo(n): # 斐波那契数列
  a, b, counter = 0, 1, 0
  while counter < n:
    yield b
    a, b, counter = b, a + b, counter + 1
  return "done"

f = fibo(10)
try:
  while True:
    print(next(f))
except StopIteration as result:
  print("StopIteration", result) # StopIteration done



# send() 方法
# 1）向生成器发送值
# 恢复执行并向生成器函数“发送”一个值。 这个值作为当前 yield 表达式的结果。 send() 方法会返回生成器所产生的下一个值，或者如果生成器没有产生下一个值就退出则会引发 StopIteration。
# 使用 send() 发送任务id，使生成器交替执行两个任务：

# 按你的调用顺序看：

# 第一步：g = gen()

# 只是创建生成器对象
# 里面的代码还没真正执行
# 第二步：print(next(g))

# 生成器开始运行
# task_id 初始是 0，所以进入 case 0
# 执行 yield int_value，先返回 0
# 代码暂停
# 所以打印 0
# 第三步：print(g.send(1))

# 生成器从上次暂停的 yield 位置继续
# send(1) 传进来的 1 会赋给 task_id
# 然后执行 int_value += 1，此时 int_value 从 0 变成 1
# 回到 while True，task_id 现在是 1，所以进入 case 1
# 执行 yield char_value，返回 A
# 所以打印 A
# 第四步：print(g.send(0))

# 继续执行，send(0) 让 task_id 变成 0
# 上一轮是 case 1，所以先执行 char_value = chr(ord(char_value) + 1)
# A 变成 B
# 回到循环，task_id 是 0，进入 case 0
# yield int_value，返回 1
# 所以打印 1
# 第五步：print(g.send(1))

# task_id 变成 1
# 先执行 case 0 里的 int_value += 1，变成 2
# 回到循环，进入 case 1
# yield char_value，返回 B
# 所以打印 B
# 第六步：print(g.send(0))

# task_id 变成 0
# 先执行 case 1 里的 char_value 递增，B 变成 C
# 回到循环，进入 case 0
# yield int_value，返回 2
# 所以打印 2
def gen():
  task_id = 0
  int_value = 0
  char_value = "A"
  while True:
    # task_id 为 0 则 int_value +1，task_id 为 1 则 char_value +1
    match task_id:
      case 0:
        task_id = yield int_value # 返回 int_value，并接收 send() 发送来的值给 task_id
        int_value += 1
      case 1:
        task_id = yield char_value # 返回 char_value，并接收 send() 发送来的值给 task_id
        char_value = chr(ord(char_value) + 1)
      case _:
        task_id = yield # 返回 None


# g = gen() 这一句只是“调用生成器函数，拿到一个生成器对象”，但这时函数内部的代码还没有开始跑。因为 gen() 里有 yield，Python 会把它识别成生成器函数：调用它时，不是立刻把整段函数执行完，而是先返回一个可迭代的生成器。
g = gen()
print(next(g)) # 0
print(g.send(1)) # A
print(g.send(0)) # 1
print(g.send(1)) # B
print(g.send(0)) # 2
# 2）使用 send(None) 启动生成器
# 当调用 send() 来启动生成器时，它必须以 None 作为调用参数，因为这时没有可以接收值的 yield 表达式。
def gen():
  task_id = 0
  int_value = 0
  char_value = "A"
  while True:
    # task_id 为 0 则 int_value +1，task_id 为 1 则 char_value +1
    match task_id:
      case 0:
        task_id = yield int_value # 返回 int_value，并接收 send() 发送来的值给 task_id
        int_value += 1
      case 1:
        task_id = yield char_value # 返回 char_value，并接收 send() 发送来的值给 task_id
        char_value = chr(ord(char_value) + 1)
      case _:
        task_id = yield # 返回 None

g = gen()
print(g.send(None)) # 0
print(g.send(1)) # A
print(g.send(0)) # 1
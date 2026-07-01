# Python中的with语句用于异常处理，封装了try except finally编码范式，提供了一种简洁的方式来确保资源的正确获取和释放
# 语法
# with expression as variable:
#   # 代码块
# expression：通常是一个对象或函数调用，该对象需要是一个上下文管理器，即实现了 __enter__和__exit__方法。
# variable：是可选的，用于存储expression的__enter__方法的返回值。


# 工作原理
# 使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try finally 语句。
# 当执行with语句时，会调用expression对象的__enter__方法。
# __enter__ 方法的返回值可以被存储在 variable 中（如果有），以供 with 代码块中使用。
# 然后执行 with 语句内部的代码块。
# 无论在代码块中是否发生异常，都会调用 expression 对象的__exit__ 方法，以确保资源的释放或清理工作，这类似于 try-except-finally 中的 finally 子句。


# case：打开一个文件并向其中写入内容，验证出现异常后文件是否正常关闭
# 1）常规方式
try:
  file = open("test.txt", "w")
  file.write(a)
  file.close()
finally:
  print("文件是否关闭：", file.closed) # 文件是否关闭： False
# 2）使用 try finally
try:
  file = open("test.txt", "w")
  try:
    file.write(a)
  finally:
    file.close()
finally:
  print("文件是否关闭：", file.closed) # 文件是否关闭： True
# 3）使用 with
# 执行顺序
# 先执行 open("test.txt", "w")
# open 返回一个文件对象
# 对这个文件对象调用 enter()
# enter 的返回值赋给 f
# 进入 with 代码块
# 结束时调用 exit()

# open：负责“创建/打开资源”
# enter：负责“正式进入 with，并把可用对象交给变量”
# exit：负责“退出时清理资源”
try:
  with open("test.txt", "w") as f:
    f.write(a)
finally:
print("文件是否关闭：", f.closed) # 文件是否关闭： True

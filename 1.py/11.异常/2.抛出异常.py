# 1.raise语句抛出异常
# 当你想要在代码中明确表示发生了错误或异常情况时，可以使用raise来抛出异常。这可以帮助你在满足某些条件时停止程序的正常执行，并将控制权转移到异常处理部分。
# 1）语法
# raise 异常类型("异常描述")
# 2）案例
def int_add(x, y):
  if isinstance(x, int) and isinstance(y, int):
    return x + y
  else:
    raise TypeError("参数类型错误")

print(int_add(1, 2)) # 3
print(int_add("1", "2")) # TypeError: 参数类型错误

#2.assert语句断言异常
# 1）语法
# assert 表达式 [,异常描述]
# 等价于：
# if not 表达式:
#   raise AssertionError([异常描述])
# 2）案例
def int_add(x, y):
  assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
  return x + y

print(int_add(1, 2)) # 3
print(int_add("1", "2")) # AssertionError: 参数类型错误
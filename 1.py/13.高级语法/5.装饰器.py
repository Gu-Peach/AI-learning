# 装饰器允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能。装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。
# 语法
def decorator(func):
  def inner(参数):
    # 添加功能
    func(参数)
    # 添加功能

  return inner


# 1.闭包实现装饰器
from math import sqrt

def func(x):
  """开根号"""
  return sqrt(x)

def decorator(f):
  def inner(x):
    x = abs(x) # 求x的绝对值
    return f(x)

  return inner

func = decorator(func)
print(func(-4)) # 2.0



# 2.@decorator使用装饰器
# 当我们使用 @decorator 前缀在 func 定义前，Python会自动将 func 作为参数传递给 decorator，然后将返回的 inner 函数替换掉原来的 func。
# from math import sqrt

def decorator(f):
  def inner(x):
    x = abs(x) # 求x的绝对值
    return f(x)

  return inner

@decorator
def func(x):
  """开根号"""
  return sqrt(x)

print(func(-4)) # 2.0

# 多层装饰器
# 多个装饰器的装饰过程：离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰。
from math import sqrt

# 将参数转化为整型
def get_integer(f):
  def inner(x):
    x = int(x)
    return f(x)

  return inner

# 将参数转换为非负数
def get_absolute(f):
  def inner(x):
    x = abs(x)
    return f(x)

  return inner

@get_integer
@get_absolute
def func(x):
  """开根号"""
  return sqrt(x)

print(func("-4")) # 2.0


# 带参数的装饰器
from math import sqrt

# 求根号n次
def times(n):
  # 将参数转换为非负数
  def get_absolute(f):
    def inner(x):
      x = abs(x)
      for i in range(n):
        x = f(x)
      return x

    return inner

  return get_absolute

@times(2)
def func(x):
  """开根号"""
  return sqrt(x)

print(func(-16)) # 2.0



# 类装饰器
# 类装饰器是包含 __call__() 方法的类，它接受函数作为参数，并返回新的函数。
from math import sqrt

class DecoratorClass:
  def __init__(self, f):
    self.f = f

  def __call__(self, x):
    x = abs(x)
    return self.f(x)

@DecoratorClass
def func(x):
  """开根号"""
  return sqrt(x)

print(func(-4)) # 2.0
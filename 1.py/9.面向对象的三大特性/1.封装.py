## 封装
# 将变量和函数写入类中的操作即为封装，即类中封装了属性和方法。
# 通过封装，我们可以将一些细节隐藏起来（私有），只暴露出必要的接口供调用者使用。

# 1.私有化
# 有时为了限制属性和方法只能在类内访问，外部无法访问；或父类中某些属性和方法不希望被子类继承。可以将其私有化。
# 1）单下划线：非公开API
# 大多数Python代码都遵循这样一个约定：有一个前缀下划线的变量或方法应被视为非公开的API，例如 _var1。这种约定不具有强制力。
# 2）双下划线：名称改写
# 有两个前缀下划线，并至多一个后缀下划线的标识符，例如 __x，会被改写为 _类名__x。只有在类内部可以通过 __x 访问，其他地方无法访问或只能通过 _类名__x 访问。


# 2.私有属性（通过双下划线定义）
class Person:

  def __init__(self, name):
    self.__name = name

  def get_name(self):
    return self.__name

p = Person("张三")
print(p.get_name()) # 张三
print(p._Person__name) # 张三
print(p.__name) # 报错

# 3.私有方法（通过双下划线定义）
class Person:

  # 定义私有方法
  def __private_method(self):
    print("private method")

  # 定义实例方法，调用私有方法
  def do_something(self):
    self.__private_method()

p = Person()
p.do_something() # private method
p._Person__private_method() # private method
p.__private_method() # 报错


# 4.property
# property 的作用，是把“方法”伪装成“属性”来用，同时还能在背后控制读取、修改和删除的行为。
# 1）方法转换为属性
# 可通过@property装饰器将一个方法转换为属性来调用。转换后可直接使用 .方法名 来使用，而无需使用 .方法名() 。
class Person:

  def __init__(self, name):
    self.name = name

  @property
  def eat(self):
    print(f"{self.name} is eating...")

p = Person("张三")
p.eat  # 张三 is eating...
# 2）只读属性
# 将方法名设置为去掉双下划线的私有属性名，方法中返回私有属性。
# @property 把一个方法变成了“像属性一样访问”的接口
# 这个对外暴露的名字通常是公开的，比如 name
# 真正被私有化的是内部存储数据，比如 self.__name
class Person:

  def __init__(self, name):
    self.__name = name

  @property
  def name(self):
    return self.__name

p = Person("张三")
print(p.name) # 张三
p.name = "李四" # 报错
# 3）读写属性
# 将方法名设置为去掉双下划线的私有属性名，使用 属性名.setter 装饰。
class Person:

  def __init__(self, name):
    self.__name = name

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

p = Person("张三")
print(p.name) # 张三

p.name = "李四"
print(p.name) # 李四
# 也可以在写方法中设置一些拦截条件来规范私有属性的写入。
class Person:

  def __init__(self, name):
    self.__name = name

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    if name == "李四":
      print("不许叫李四")
    else:
      self.__name = name

p = Person("张三")
print(p.name) # 张三

p.name = "李四" # 提示 “不许叫李四”
print(p.name) # 张三

p.name = "王五"
print(p.name) # 王五
# 4）注意
# @property装饰的方法不要和变量重名，否则可能导致无限递归。
class Person:

  @property
  def name(self):
    return self.name

p = Person()
p.name # 报错：RecursionError: maximum recursion depth exceeded
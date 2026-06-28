## 实例方法
# 实例方法在类中定义，第一个参数为self，代表实例本身。

class Person:
  """人的类"""

  home = "earth"

  def __init__(self, name):
    self.name = name

  def instance_method(self):
    print(self.name, self.home, Person.home)

p = Person("张三")
p.instance_method() # 张三 earth earth，此时p中没有home实例属性，会去查找home类属性
Person.home = "venus" # 修改类属性
p.home = "mars" # 定义实例属性
p.instance_method() # 张三 mars venus

# dict下是实例属性，class下是类属性，索引时优先查找实例属性的内容，没有再查类属性

# p = {
#     "__class__": Person,
#     "__dict__": {
#         "name": "张三",
#         "home": "venus",
#     }
# }


## 类方法
# 类方法在类中通过 @classmethod 定义，第一个参数为cls，代表类本身。
class Person:
  """人的类"""

  home = "earth" # 定义类属性

  @classmethod
  def class_method(cls):
    print(cls.home)

Person.class_method() # 通过类调用类方法

p1 = Person() # 创建一个实例对象
p1.class_method() # 通过实例对象调用类方法


## 静态方法
# 静态方法在类中通过 @staticmethod 定义
# 可以通过类名或实例调用，但它不会访问类或实例的内部信息，更像是一个工具函数，只是为了方便组织代码，把它放在了类里面。
class Person:
  """人的类"""

  home = "earth" # 定义类属性

  @staticmethod
  def static_method():
    print("static method")

Person.static_method() # 通过类调用静态方法

p1 = Person() # 创建一个实例对象
p1.static_method() # 通过实例对象调用静态方法
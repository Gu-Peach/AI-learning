# self和this是有区别的

# Python 里的 self 是显式传入的第一个参数，谁调用方法，谁就作为 self 传进去。
# JavaScript 里的 this 通常是运行时根据“调用方式”决定的，不是方法定义时固定好的。
# 所以 self 更像“当前实例”的普通参数名，而 this 更像一种隐式绑定。

class Student:
  
  school = "atguigu"

  def __init__(self, name,age):
    self.name = name
    self.age = age

  def eat(self):
    print("eating...")

  def stand(self):
    print(f"年龄是{self.age}的小伙{self.name}站着听")

xjq=Student("xjq",20)

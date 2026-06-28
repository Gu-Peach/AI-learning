"""动态添加属性与方法"""

import types


# 1. 动态给对象添加属性
class Person:
    def __init__(self, name=None):
        self.name = name


p = Person("张三")
print(p.name)  # 张三

p.age = 18
print(p.age)  # 18


# 2. 动态给类添加属性
class Person:
    def __init__(self, name=None):
        self.name = name


p = Person("张三")
print(p.name)  # 张三

Person.age = 0
print(p.age)  # 0


# 3. 动态给实例添加方法
# 3.1 添加普通函数属性
class Person:
    def __init__(self, name=None):
        self.name = name


def eat():
    print("吃饭")


p = Person("张三")
p.eat = eat
p.eat()  # 吃饭


# 3.2 添加实例方法
# 给对象添加的实例方法只绑定在当前对象上，不对其他对象生效，调用时会自动传入 self。
class Person:
    def __init__(self, name=None):
        self.name = name


def eat(self):
    print(f"{self.name}在吃饭")


p = Person("张三")
p.eat = types.MethodType(eat, p)
p.eat()  # 张三在吃饭


# 4. 动态给类添加方法
# 给类添加的方法对所有对象都生效。类方法需要 cls，静态方法不需要。
class Person:
    home = "earth"

    def __init__(self, name=None):
        self.name = name


@classmethod
def come_from(cls):
    print(f"来自{cls.home}")


@staticmethod
def static_function():
    print("static function")


Person.come_from = come_from
Person.come_from()  # 来自earth

Person.static_function = static_function
Person.static_function()  # static function


# 5. 动态删除属性与方法
# del 对象.属性名
# delattr(对象, 属性名)


# 6. __slots__ 限制实例属性与实例方法
# __slots__ 用来限制实例能添加哪些属性。它只对当前类生效，对子类无效。
class Person:
    __slots__ = ("name", "age", "eat")

    def __init__(self, name=None):
        self.name = name


def eat(self):
    print(f"{self.name}在吃饭")


def drink(self):
    print(f"{self.name}在喝水")


p = Person("张三")

# 添加实例属性
p.age = 10
print(p.age)  # 10

# 添加实例方法
p.eat = types.MethodType(eat, p)
p.eat()  # 张三在吃饭

# 添加超出 __slots__ 限制的实例属性会报错
p.weight = 100  # AttributeError: 'Person' object has no attribute 'weight'

# 注意：这里应使用 types.MethodType，不是 type.MethodType
p.drink = types.MethodType(drink, p)

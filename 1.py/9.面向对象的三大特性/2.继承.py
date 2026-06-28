## 单继承
# 1）语法
# class 类名(父类):
#   类体
# 在类名后括号内指定要继承的父类。
# 2）案例
class Person:
    """人的类"""

    home = "earth"  # 定义类属性

    def __init__(self, name):
        self.name = name  # 定义实例属性

    def eat(self):
        print("eating...")


class YellowRace(Person):
    """黄种人"""

    #   子类自己定义__init__的时候直接覆盖父类
    def __init__(self, name):
        self.name = name
        color = "yellow"

        def run(self):
            print("runing...")


# 子类父类都给self.name赋值
class YellowRace2(Person):
    """黄种人"""

    #   子类自己定义__init__的时候直接覆盖父类
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    color = "yellow"

    def run(self):
        print("runing...")


class WhiteRace(Person):
    """白种人"""

    color = "white"  # 定义类属性


class BlackRace(Person):
    """黑种人"""

    color = "black"  # 定义类属性


y1 = YellowRace("张三")
print(y1.home)  # earth
print(y1.color)  # yellow
print(y1.name)  # 张三
y1.eat()  # eating...

w1 = WhiteRace("李四")
print(w1.home)  # earth
print(w1.color)  # white
print(w1.name)  # 李四
w1.eat()  # eating...

b1 = BlackRace("王五")
print(b1.home)  # earth
print(b1.color)  # black
print(b1.name)  # 王五
b1.eat()  # eating...


## 多继承
# 调用方法时先在子类中查找，若不存在则从左到右依次查找父类中是否包含方法。
# 对于 __init__ 来说，如果子类没有写自己的 __init__，就会先找到 MRO 中第一个父类的 __init__ 并调用。
# 如果不使用 super()，不会自动把参数继续传给后面的父类；参数超过第一个 __init__ 的形参个数时会直接报错。
# 如果使用 super() 并配合 *args、**kwargs，可以让多个父类的 __init__ 依次执行，这叫合作式多继承。
# 1）语法
# class 类名(父类1, 父类2, ...):
#   类体
# 2）案例
class Person:
    """人的类"""

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")


class YellowRace(Person):
    """黄种人"""

    color = "yellow"

    def run(self):
        print("runing...")


class Student(Person):
    """学生"""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("studying...")


class ChineseStudent(Student, YellowRace):  # 继承了Student和YellowRace
    """中国学生"""

    country = "中国"


y1 = ChineseStudent("张三", "三年级")
print(y1.home, y1.color, y1.country, y1.name, y1.grade)
y1.eat()
y1.run()
y1.study()


# 3）不使用 super() 时的情况
# ChineseStudent1 仍然只会先找到 Student1.__init__。
# 这里传 3 个参数时，会因为 Student1.__init__(name, grade) 只能接收 2 个参数而报错。
class Person1:
    home = "earth"

    def __init__(self, name):
        self.name = name


class YellowRace1(Person1):
    color = "yellow"

    def __init__(self, name, color):
        self.name = name
        self.color = color


class Student1(Person1):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class ChineseStudent1(Student1, YellowRace1):
    country = "中国"


# y2 = ChineseStudent1("张三", "三年级", "yellow")
# TypeError: Student1.__init__() takes 3 positional arguments but 4 were given


# 4）使用 super() 时的情况
# 配合 *args、**kwargs，参数会沿着 MRO 依次传递。
# super()是调用下一个类里面的方法
class Person2:
    home = "earth"

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


class YellowRace2(Person2):
    color = "yellow"

    def __init__(self, name, color, *args, **kwargs):
        self.color = color
        super().__init__(name, *args, **kwargs)

    def run(self):
        print("runing...")

# *args 用来接收多余的位置参数，收进一个元组
# **kwargs 用来接收多余的关键字参数，收进一个字典
# 所以这一步不是“解包”，而是“打包接收”。
class Student2(Person2):
    def __init__(self, name, grade, *args, **kwargs):
        self.grade = grade
        super().__init__(name, *args, **kwargs)

    def study(self):
        print("studying...")


class ChineseStudent2(Student2, YellowRace2):
    country = "中国"


y3 = ChineseStudent2("张三", "三年级", "yellow")
print(y3.home, y3.color, y3.country, y3.name, y3.grade)
y3.eat()
y3.run()
y3.study()



## 复用父类方法
# 子类可以在类中使用 super().方法名() 或 父类名.方法名() 来调用父类的方法。
# 1）super().方法名()
class Person:
  """人的类"""

  home = "earth"

  def __init__(self, name):
    self.name = name

  def eat(self):
    print("eating...")

class YellowRace(Person):
  """黄种人"""

  color = "yellow"

  def run(self):
    print("runing...")

class Student(Person):
  """学生"""

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  def study(self):
    print("先吃再学")
    super().eat() # 子类中调用父类的方法
    print("studying...")

class ChineseStudent(Student, YellowRace): # 继承了Student和YellowRace
  """中国学生"""

  country = "中国"

y1 = ChineseStudent("张三", "三年级")
print(y1.home, y1.color, y1.country, y1.name, y1.grade)
y1.study()
# 2）父类名.方法名()
class Person:
  """人的类"""

  home = "earth"

  def __init__(self, name):
    self.name = name

  def eat(self):
    print("eating...")

class YellowRace(Person):
  """黄种人"""

  color = "yellow"

  def run(self):
    print("runing...")

class Student(Person):
  """学生"""

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  def study(self):
    print("先吃再学")
    Person.eat(self) # 子类中调用父类的方法
    print("studying...")

class ChineseStudent(Student, YellowRace): # 继承了Student和YellowRace
  """中国学生"""

  country = "中国"

y1 = ChineseStudent("张三", "三年级")
print(y1.home, y1.color, y1.country, y1.name, y1.grade)
y1.study()


## 方法重写
# 在子类中定义与父类方法重名的方法，调用时会调用子类中重写的方法。
class Person:

  home = "earth"

  def __init__(self, name):
    self.name = name

  def eat(self):
    print("eating...")

class Chinese(Person):

  color = "yellow"

  # 重写父类方法
  def eat(self):
    print("用筷子吃")

y1 = Chinese("张三")
y1.eat()
# 注意：子类重写 __init__() 并调用时，不会执行父类的 __init__() 方法。如有必要，需在子类 __init__() 中使用 super().__init__() 来调用父类的 __init__() 方法。
class Person:

  def __init__(self, name):
    self.name = name

class Chinese(Person):

  def __init__(self, name, area):
    super().__init__(name) # 调用父类的__init__()
    self.area = area

y1 = Chinese("张三", "北京")
print(y1.name, y1.area)
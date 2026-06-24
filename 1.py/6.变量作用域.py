# 作用域
# Python中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。变量的作用域决定了哪一部分程序可以访问哪个变量，Python的作用域一共有4种，分别是：
# L （Local） 局部作用域
# E （Enclosing）嵌套作用域 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。以下案例演示各种作用域类型。

a = int(2.9) #  int() 是内建作用域的函数，a 是全局作用域的变量
b = 0 # 全局作用域
def outer():
  c = 1 # 嵌套作用域
  def inner():
    d = 2 #局部作用域
    print(d,c,b,a)
  return inner
in_func=outer()
in_func()



# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
# 分支,循环不会引入新的作用域
num = 2
if num > 1:
  msg = "helloWorld"
print(msg)

def test():
  msg_test = "welcome"
print(msg_test)
# 实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
# 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
# 从报错的信息上看，说明了 msg_inner 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。



## 全局变量&局部变量

# 1）使用global修改全局变量
# 定义了一个全局变量，如何在函数内对其进行修改？
# （1）直接在函数内修改
# ①通过var1 += 200修改。会报错
# 当你在函数内部对一个变量进行赋值操作时，Python 默认会把这个变量当作局部变量，即便全局作用域中已经存在同名变量。
var1 = 100
def function_a():
  var1 += 200 # 将var1当做局部变量处理，+=得先定义变量
function_a() # 报错
# ② 通过var1 = 200修改。全局变量var1的值并没被修改，仍是100。我们只是在function_a函数中新定义了一个局部变量var1并将其赋值为200。
var1 = 100

def function_a():
  var1 = 200
  print("var1:", var1)
print(var1) # 100
function_a() # var1: 200
print(var1) # 100

# （2）在函数内使用 global 声明全局变量
# 函数内使用 global 声明全局变量后，可以修改全局变量。
def function_a():
  global var1
  var1 = 200
  print("var1:", var1)
var1 = 100
print(var1) # 100
function_a() # var1: 200
print(var1) # 200


# 2）修改可变类型的全局变量
# 当全局变量为可变类型时，函数内不使用 global 声明，也可以对其进行修改。
def function_a():
  list1[0] = -1000
  print("list1:", list1)

list1 = [1, 2, 3]
print(list1) # [1, 2, 3]
function_a() # list1: [-1000, 2, 3]
print(list1) # [-1000, 2, 3]
# 在函数中不使用 global 声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
# 不可变类型的全局变量其指向的数据不能修改，所以不使用 global 无法修改全局变量。
# 可变类型的全局变量其指向的数据可以修改，所以不使用 global 也可修改全局变量。

# 3）使用nonlocal 也用作内部作用域修改外部作用域的变量的场景，不过此时外部作用域不是全局作用域而是嵌套作用域。
def function_outer():
  var1 = 1
  print(var1)
  def function_inner():
    nonlocal var1
    var1 = 200
  function_inner()
  print(var1)
function_outer() # var1: 1 -> 200



## 匿名函数
# 匿名函数的主要目的是用于简单的、一次性的函数操作，避免定义繁琐的普通函数。
# 6.11匿名函数
# 6.11.1语法
# Python使用 lambda 来定义匿名函数，所谓匿名，指其不用 def 的标准形式定义函数。
# lambda 参数列表: 表达式
# lambda 只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块，所以仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 6.11.2使用普通函数传参
# def operator(a, b):
#   return a + b
# def function(a, b, operator):
#   return operator(a, b)
# print(function(1, 2, operator))
# # 6.11.3使用匿名函数传参
# def function(a, b, operator):
#   return operator(a, b)
# print(function(1, 2, lambda x, y: x + y))
# # 6.11.4匿名函数作为内置函数的参数
# # 可以将匿名函数与常用的内置参数搭配使用。
# # 1）sorted()
# # 有三名学生的姓名和年龄，按年龄排序。
# student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]
# print(sorted(student_list, key=lambda x: x["age"]))
# 2）map()
# map() 函数对序列中元素逐一处理。
# map_result = map(lambda x: x * x, [0, 1, 3, 7, 9])
# print(list(map_result)) # [0, 1, 9, 49, 81]
# 3）filter()
# filter() 函数对序列中元素过滤。
# filter_result = filter(lambda x: x >= 0, [-0, -1, -3, 7, 9])
# print(list(filter_result)) # [0, 7, 9]
# 4）reduce()
# reduce() 函数对序列中元素进行累积。
# from functools import reduce

# reduce_result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# print(reduce_result) # 120
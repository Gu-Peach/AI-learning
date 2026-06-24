## 函数的参数传递
# 1）必须参数
def func(a, b, c):
 print(a, b, c)
func(1, 2, 3) # 1 2 3

# 2）关键字参数
'''
   该案例演示了函数调用时的关键字参数
'''
def printInfo(name,age) :
  print("姓名:",name)
  print("年龄:",age)


# 3）默认值参数

def printInfo(name,age = 20) :
  print("姓名:",name)
  print("年龄:",age)

printInfo("zhangsan")

printInfo("lisi",30)

printInfo(age = 40,name = "wangwu")
# 4）不定长参数
# 参数的个数是不确定的。
# （1）语法：
# def 函数名([普通参数,] *var_args_tuple ):
#    函数体
# （2）案例：

def printInfo(num,*vartuple):
  print(num)
  print(vartuple)

printInfo(70,60,50)

print("-" * 20)
# 如果不定长的参数后面还有参数,必须通过关键字参数传参
def printInfo1(num1,*vartuple,num) :
  print(num)
  print(num1)
  print(vartuple)

printInfo1(10,20,num = 40)

print("-" * 20)
# 如果没有给不定长的参数传参,那么得到的是空元组
printInfo1(70,num = 60)
# （3）注意：
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 如果形参中出现了不定长参数，那么在调用函数的时候，先通过位置进行必须参数的匹配，然后不定长参数后面的参数必须通过关键字参数匹配
# 如果不定长的参数后面还有参数,必须通过关键字参数传参
# 还有一种就是参数带两个星号 **的可变长参数，基本语法如下：
# def 函数名([普通参数,] **var_args_dict ):
#    函数体
# 加了两个星号 ** 的参数会以字典的形式导入，后面就不能再有其他参数了
'''
  该案例演示了函数调用时的不定长参数
'''
def printInfo(num,**vardict):
  print(num)
  print(vardict)
  # return

printInfo(10,key1 = 20,key2 = 30)
printInfo(10,a = 20,b = 30)



## 解包传参
# 若函数的形参是定长参数，可以通过 * 和 ** 对列表、元组、字典等解包传参。
def func(a, b, c):
  return a + b + c
tuple11 = (1, 2, 3)
print(func(*tuple11))
# 字典中key的名称和参数名必须一致
dict1 = {"a": 1, "b": 2, "c": 3}
print(func(**dict1))


## 6.5.6强制使用位置参数或关键字参数
# / 前的参数必须使用位置传参，* 后的参数必须用关键字传参。
# 位置传参就是按参数的位置顺序来传值；关键字传参就是按“参数名=值”来传值。
def f(a, b, /, c, d, *, e, f):
  print(a, b, c, d, e, f)

f(1, 2, 3, d=4, e=5, f=6)


## 防止函数修改列表
# 有时要函数对列表进行处理，又不希望函数修改原列表，可以使用 copy.deepcopy()。
import copy

def multiply2(var1):
  var1[3].append(400)
  print("函数内处理后：", var1)

list1 = [1, 2, 3, [100, 200, 300]]
print("函数外处理前：", list1)
multiply2(copy.deepcopy(list1))
print("函数外处理后：", list1)

## 6.6函数说明文档
# 编写了函数说明文档后，可以通过 help(函数名) 获取函数说明文档。
def adult(age=18):
  """根据年龄判断是否成年"""
  result = "未成年"[age >= 18 :]
  return result

help(adult)
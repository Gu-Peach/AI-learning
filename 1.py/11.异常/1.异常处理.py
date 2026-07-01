# 1.try-except语句
# 可根据捕获的异常类型进行不同的处理
try:
  result = 3 / 0
  print("发生异常了")
except ZeroDivisionError as e:
  print(e)
except (RuntimeError, TypeError, NameError) as e:
  print(e)
except:
  print("Unexpected error")
print("End")


## else
# try:
#   可能发生异常的代码
# except 异常类型1 as 变量名1:
#   异常处理的代码
# except 异常类型2 as 变量名2:
#   异常处理的代码
# else:
#   没有异常时执行的代码
try:
  result = x / y
except ZeroDivisionError:
  print("除数不能为零！")
else:
  print(f"结果是: {result}")



## finally
# try:
#   可能发生异常的代码
# except 异常类型1 as 变量名1:
#   异常处理的代码
# except 异常类型2 as 变量名2:
#   异常处理的代码
# else:
#   没有异常时执行的代码
# finally:
#   无论是否发生异常都会执行的代码
try:
  result = 3 / 0
except ZeroDivisionError as e:
  print(e)
else:
  print(result)
finally:
  print("finally")
print("End")
输出结果：
division by zero
# 当存在 try 嵌套或函数嵌套时，若内层出现了异常且在内层无法处理，会将异常一层一层向外传递，直到异常被处理或程序报错。
try:
  try:
    try:
      print(1 / 0)  # ← 发生 ZeroDivisionError
    except NameError as e:
      print("第三层", e)  # 不匹配，无法捕获
  except TypeError as e:
    print("第二层", e)    # 不匹配，无法捕获
except Exception as e:
  print("第一层", type(e), e)  # ← 在这里被捕获！
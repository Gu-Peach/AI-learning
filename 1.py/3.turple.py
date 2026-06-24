# 元组
# 1.创建元组，元组中的元素可以重复
tuple1 = (100, 200, 300, 400, 500)
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用。
tuple1 = (100,)
# 也可以通过元组推导式创建元组。不是证据的推导式，而是创建一个生成器对象，此时它还没有把元素都算出来，只是保存了“怎么生成”的规则。
tuple_generator = (x for x in range(10)) # 获取生成器对象
print(tuple_generator)
tuple2 = tuple(tuple_generator) # 转换为元组
print(tuple2)

# 特点：元组的不可变
# 元组的不可变指的是元组所指向的内存中的内容不可变，但可以重新赋值。
# 可重新赋值体现在第一行创建了一个元组对象 (100, 200, 300)，tuple3 指向它。
# 第二行 tuple3 + (1, 2, 3) 会生成一个新的元组 (100, 200, 300, 1, 2, 3)，然后把 tuple3 这个变量改为指向这个新对象。
tuple3 = (100, 200, 300)
print(id(tuple3), tuple3)
# id() 是用来查看一个对象的“身份标识”的。
# 在 Python 里，它通常可以理解成这个对象在内存中的地址标识，用来区分是不是同一个对象。
tuple3 = tuple3 + (1, 2, 3)
print(id(tuple3), tuple3)
# 如果元组中元素是可变数据类型，其嵌套项可以被修改。
tuple4 = (100, 200, 300, [1, 2, 3])
tuple4[3].append(4)
print(tuple4) # (100, 200, 300, [1, 2, 3, 4])


    # 方法通list
        # 5.4.2访问元组
        # tuple1 = (100, 200, 300, 400, 500)
        # print(tuple1[2])
        # print(tuple1[-1])
        # print(tuple1[2:4])
        # 5.4.3元组相加
        # tuple1 = (100, 200, 300)
        # tuple2 = ("a", "b", "c")
        # print(tuple1 + tuple2)  # (100, 200, 300, 'a', 'b', 'c')
        # 5.4.4元组乘法
        # tuple1 = (100, 200, 300)
        # print(tuple1 * 2)  # (100, 200, 300, 100, 200, 300)
        # 5.4.5检查成员是否为元组中元素
        # tuple1 = (100, 200, 300, 400, 500)
        # print(300 in tuple1)  # True
        # 5.4.6获取元组长度
        # tuple1 = (100, 200, 300, 400, 500)
        # print(len(tuple1))  # 5
        # 5.4.7求元组中元素的最大值、最小值、加和
        # tuple1 = (100, 200, 300, 400, 500)
        # print(max(tuple1))  # 500
        # print(min(tuple1))  # 100
        # print(sum(tuple1))  # 1500
        # 5.4.8遍历元组
        # tuple1 = (100, 200, 300, 400, 500)

        # for i in tuple1:
        #     print(i)

        # for i in range(len(tuple1)):
        #     print(i, tuple1[i])

        # for i, val in enumerate(tuple1):
        #     print(i, val)
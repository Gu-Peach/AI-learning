# 链表遍历
# 1）直接遍历列表元素
list1 = [100, 200, 300, 400, 500]
for i in list1:
  print(i)
# 2）通过下标遍历列表
list1 = [100, 200, 300, 400, 500]
for i in range(len(list1)):
  print(i, list1[i])
# 3）使用enumerate()同时获取列表的下标和元素
# enumerate() 是用来在遍历序列时，同时拿到元素的下标和元素值 的。
list1 = [100, 200, 300, 400, 500]
for i, val in enumerate(list1):
  print(i, val)


# 删除指定元素或者切片
list1 = [100, 200, 300, 400, 500]
del list1[2]


# 列表推导式
# 列表推导式是 Python 中一种简洁创建列表的方式，它将一个可迭代对象（如列表、元组、集合、字符串等）的元素通过某种运算或条件筛选后生成一个新的列表。
# （1）基础的列表推导式
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
# （2）带条件的列表推导式
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)   # [0, 4, 16, 36, 64]
# （3）使用现有列表的列表推导式
list1 = [1, 2, 3, 4, 5]
squares = [x**2 for x in list1]
print(squares)   # [1, 4, 9, 16, 25]
# （4）包含多个循环的列表推导式
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
tuple_list = [(i, j) for i in list1 for j in list2]
# [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (1, 'e'),
#  (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (2, 'e'),
#  (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (3, 'e'),
#  (4, 'a'), (4, 'b'), (4, 'c'), (4, 'd'), (4, 'e'),
#  (5, 'a'), (5, 'b'), (5, 'c'), (5, 'd'), (5, 'e')]
print(tuple_list)


# zip函数
# zip() 函数可将多个可迭代对象中对应元素打包为一个个元组。
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
zipped = zip(list1, list2)
print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# 补充一下，zip() 会按最短的那个序列结束；如果两个列表长度不一样，后面的多余部分会被丢掉。

# zip(list1)的结果
# [(1,), (2,), (3,), (4,), (5,)]
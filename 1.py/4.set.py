# 5.5.1创建集合
# 可以通过{}或set()创建集合，但创建空集合需要使用set()而非{}，因为{}会创建空字典。
set1 = {1, 2, 3}
set2 = set([1, 2, 3]) # 使用set()函数从列表创建集合
set3 = set()
print(set1, set2, set3)
# 也可以通过集合推导式创建集合。
set1 = {x for x in range(10) if x % 2 == 0}
print(set1) # {0, 2, 4, 6, 8}
# 5.5.2向集合中添加元素
set1 = {1, 2, 3}
set1.add(4)
set1.add(5)
print(set1)
# 5.5.3从集合中删除元素
set1 = {1, 2, 3}
set1.remove(2)
print(set1)
# 5.5.4检查成员是否为集合中元素
set1 = {1, 2, 3, 4, 5}
print(2 in set1) # True
# 5.5.5获取集合长度
set1 = {1, 2, 3, 4, 5}
print(len(set1)) # 5
# 5.5.6求集合中元素的最大值、最小值、加和
set1 = {1, 2, 3, 4, 5}
print(max(set1)) # 5
print(min(set1)) # 1
print(sum(set1)) # 15
# 5.5.7遍历集合
my_set = {1, 2, 3, 4, 5}
for item in my_set:
  print(item)
# 5.6.1创建字典
# 可以通过{}或dict()创建字典。
dict1 = {}
dict2 = dict()
dict3 = {"name": "Alice", "age": 18, "gender": "male"}
dict4 = dict(name="Bob", age=20, gender="female")
dict5 = dict([("name", "Tom"), ("age", 22), ("gender", "male")])
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5) #{'name': 'Tom', 'age': 22, 'gender': 'male'}
# 也可以通过字典推导式创建字典。
squares = {x: x**2 for x in range(4)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9}
# 5.6.2访问字典
# 可通过 [] 访问字典中的元素。key不存在时会报错。
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
print(dict1["name"]) # Alice
print(dict1["age"]) # 18
print(dict1["gender"]) # male
print(dict1["address"]) # 报错
# 也可以通过get()获取字典中的元素。key不存在时会返回None，也可以指定默认值。
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
print(dict1.get("name")) # Alice
print(dict1.get("age")) # 18
print(dict1.get("gender")) # male
print(dict1.get("address")) # None
print(dict1.get("address", "earth")) # earth
# 5.6.3向字典中添加元素
# 为字典指定的key赋值value，若key原本不存在则会被添加。
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
dict1["address"] = "earth"
print(dict1)
# 5.6.4修改字典中元素
# 通过key修改对应的value。
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
dict1["name"] = "Bob"
print(dict1)
# 5.6.5检查成员是否为字典中的key
dict1 = {"name": "Alice", "age": 81, "gender": "male"}
print("name" in dict1) # 检查key是否存在
print("Alice" in dict1) # 无法直接检查value是否存在
# 5.6.6获取字典长度
dict1 = {"name": "Alice", "age": 81, "gender": "male"}
print(len(dict1)) # 3
# 5.6.7遍历字典
my_dict = {'Name': 'Tom', 'Age': 17}
# 遍历出所有k
keys = my_dict.keys()
for k in keys:
 print (k) 
print("-" *20)
# 遍历出所有v
vals = my_dict.values()
print(vals)
for v in vals:
 print (v) 
print("-" *20)
# k-v遍历
keys = my_dict.keys()
for k in keys:
 print (k + "---" + str(my_dict[k])) 
print("-" *20)
kv = my_dict.items()
for i in kv:
 print(i)
# 5.6.8删除字典元素
my_dict = {'Name': 'Tom', 'Age': 17}
del my_dict['Name'] # 删除键 'Name'
# my_dict.clear()     # 清空字典
# del my_dict         # 删除字典

print (my_dict)
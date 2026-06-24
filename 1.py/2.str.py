# 所有的字符串按照字面意思处理，没有转义字符。需在字符串前加上r / R。
print("hello\nworld")
print(r"hello\nworld")
# hello
# world
# hello\nworld


# 常用方法
# str.replace(old,new[,max])
# str.split([x][,n])
# x.join(seq)
# str.removeprefix()
# str.removesuffix()


# 1）replace：替换字符串内容
text = "hello world"
print(text.replace("world", "python"))
print("banana".replace("a", "A", 2))
# hello python
# bAnAna


# 2）split：按指定分隔符切分字符串
text = "apple,banana,orange"
print(text.split(","))
print(text.split(",", 1))
# ['apple', 'banana', 'orange']
# ['apple', 'banana,orange']



# 3）join：把多个字符串拼接成一个字符串
items = ["a", "b", "c"]
print("-".join(items))
print("".join(items))
# a-b-c
# abc



# 4）removeprefix：删除字符串开头的指定前缀
text = "unhappy"
print(text.removeprefix("un"))
print(text.removeprefix("re"))
# happy
# unhappy



# 5）removesuffix：删除字符串结尾的指定后缀
text = "photo.jpg"
print(text.removesuffix(".jpg"))
print(text.removesuffix(".png"))
# photo
# photo.jpg
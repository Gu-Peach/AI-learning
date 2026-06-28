# 同一事物在不同场景下呈现不同状态。
class Animal:
  def go(self):
    pass

class Dog(Animal):
  def go(self):
    print("跑")

class Fish(Animal):
  def go(self):
    print("游")

class Bird(Animal):
  def go(self):
    print("飞")

def go(animal):
  animal.go() # 将不同的实例传入，执行不同的方法

dog = Dog()
fish = Fish()
bird = Bird()
go(dog)
go(fish)
go(bird)
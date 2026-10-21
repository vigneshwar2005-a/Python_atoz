# Polymorphism 

'''Python allows differnet classes to have methods with the same name
Advantage: To increase the readability of the program.'''

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('I am a cat. My name is',self.name,'and my age is',self.age)
    def make_sound(self):
        print('meow')
class Dog:
    def __init__(self,name,age):
            self.name = name
            self.age = age
    def info(self):
        print('I am a Dog. My name is',self.name,'and my age is',self.age)
    def make_sound(self):
        print('whow')
obj = Cat('Subu',10)
obj.info()
obj.make_sound()
obj1 = Dog('Somu',5)
obj1.info()
obj1.make_sound()

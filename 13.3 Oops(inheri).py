# Inheritance

'''Python supports class level inheritance 
It allows us to create a new class from an existing one 
The newly Created class is known as subclass (Child or derived)
The existing class from which the child class inherits is known as the super class (parent or base)

Advantage 

---> Code reusable

Syntax

class Superclass:
    attributes and methods
class subclass(suerclass):
    attributes and methods

'''

class Animal:
    name='' 
    def Eat(self):
        print('I can eat')
class Dog(Animal):
    def Display(self):
        print('My name is',self.name)
obj=Dog()
obj.name='Subramani'
obj.Eat()
obj.Display()

# Single, Multi level, Multiple, Hierarchy

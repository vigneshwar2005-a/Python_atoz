# Classes and objects

'''Python classes

A class is a collection of objects.

Syntax

Class Classname:
    Classdefinition

Class Bike:
    name = ""
    gear = 0
    
Here the name and gear are attributes (variables) whereas Bike is class name.
Class name should always start with a capital letter '''

''' Python Object

An object is called an instance of a class.

Syntax:

Object name = Class name ()

Access class atributes using Object(.notation)
object name.='Royal Enfield'
'''

class Bike:
    name=''
    gear=0
obj = Bike()
obj.name='Royal Enfield'
obj.gear=5
print(obj.name,obj.gear)

obj2 = Bike()
obj2.name='Yamaha'
obj2.gear='3'
print(obj2.name,obj2.gear)





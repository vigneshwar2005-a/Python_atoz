# Access Modifiers

'''There are three types of access modifiers in python 

---> Public modifier

These attributes and methods are accesible from anywhere, Both inside and outside the class.
These are the default types used in many programs 

---> Protected modifier

These attributes and methods are intended for internal use within the class and it's subclass 
Prefixed with a single underscore (_)

---> Private modifier

These attributes and methods are used only within the class
They are prefixed with two underscore (__)

'''

# Encapsulation

''' It refers to the bundling of attributes and methods inside a single class.
It prevents outer classes from accesing the changing attributes and methods of a class.
It also helps to achieve data hiding '''

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_info(self):
        print(self.name,self.salary)
    def __display (self):
        print('Welcome to python')
    def _disp (self):
        print('Welcome to java')
emp=Employee("vignesh",120000)
emp.display_info()
#emp.__display()
emp._disp()
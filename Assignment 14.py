class Student:
    def __init__(self,name,age,rollnumber):
        self.name=name
        self.age=age
        self.rollnumber=rollnumber
    def insert(self):
        print('My name is:',self.name)
        print('My age is:',self.age)
        print('My rollnumber is:',self.rollnumber)
obj = Student('Vigneshwar',18,43111009)
obj.insert()

class Student2:
    def __init__(self,name,age,rollnumber):
        self.name=name
        self.age=age
        self.rollnumber=rollnumber
    def insert(self):
        print('My name is:',self.name)
        print('My age is:',self.age)
        print('My rollnumber is:',self.rollnumber)
obj = Student2('Yash',28,43111019)
obj.insert()

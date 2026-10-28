# Modules

# Create a Module
'''To create a module just save the code we want in a file with the 
extension ".py" '''

# Use the modeule
'''We can use the module just created by using the import statement '''

def greeting(name):
    print('Hello',name)

class Employee:
    def empdetails(self,name,salary):
        self.name= name
        self.salary=salary
        print(self.name,self.salary)
        
emp = Employee()


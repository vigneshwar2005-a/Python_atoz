# Constructors 

''' It is a special function which is used to intialise the object '''

class Bike:
    def __init__(self,name,colour):
        self.name = name 
        self.colour = colour
        print(self.name)
        print(self.colour)
obj = Bike ('Royal Enfield','Blue')
obj1 = Bike ('KTM','Black')
        
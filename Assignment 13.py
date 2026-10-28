class Bike:
    name=''
    def Model(self):
        print('This is a BS6 Model')
class Type(Bike):
    def Type(self):
        print('The bikes name is',self.name)
class Uin(Type):
    def Uin(self):
        print('I am the engine')
obj = Uin()
obj.name= 'Royal Enfield'
obj.Model()
obj.Type()
obj.Uin()



    




    
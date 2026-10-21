class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print('The selling price',self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
obj=Computer()
obj.sell()

obj.__maxprice=1000
obj.sell()

# Using setter function

obj.setmaxprice(2000)
obj.sell()
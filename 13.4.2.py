class Computer:
    def __init__(self):
        self._maxprice=900
    def sell(self):
        print('The selling price',self._maxprice)
    def setmaxprice(self,price):
        self._maxprice=price
obj=Computer()
obj.sell()

obj._maxprice=1000
obj.sell()

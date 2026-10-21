class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def drive(self):
        return f'The {self.brand} {self.model}'
my_car=Car('Tesla',2025)
print(my_car.brand)
print(my_car.model)
print(my_car.drive())

class Scar(Car):
    def __init__(self, brand, model,feul):
        super().__init__(brand, model)
        self.fuel= feul 
    def charge(self):
        return f'Fueling the {self.fuel}'
sc=Scar('nissan','GTR',40)
print(sc.drive())
print(sc.charge())

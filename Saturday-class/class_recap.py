#class is a blueprint for creating an object
#while def a class, it has to start with a capital letter.
#call te class the same way you call a function.

class Car:

    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year =year


    def start(self):
        return "vroom" 
    def stop(self):
        return "shhh"

    def play_music(self):
        return "boom"
    
Mycar = Car ("Mercedes", "C350", 2015)
print(Mycar.make)

#Inheritance
class ElectricCar(Car):
    def __init__ (self, make, model, year):
        Car .__init__ (self, make, model, year)

    def charge(self):
        return f" I am charging {self.make} {self.model}"

myElectricCar = ElectricCar("Mercedes", "C350", 2020)
print(myElectricCar.charge())
    


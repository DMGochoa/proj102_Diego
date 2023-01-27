class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'THis car has {self.__odometer_reading} KM on it')
        
    def update_odometer(self, km):
        if km >= self.__odometer_reading:
            self.__odometer_reading = km
            
    def __private_function(self):
        print('This is a private function')

my_car = Car('Toyota', 'Tacoma', 2000)
print(my_car.get_descriptive_name())


# Inheritance
class ElectricCar(Car):
    # Constructor python 2.7
    # def __init__(self, make, model, year) -> None:
    #     super(ElectricCar, self).__init__(make, model, year)
    
    # Python 3.X
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)

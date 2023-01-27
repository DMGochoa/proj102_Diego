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
        print(f'THis car has {} KM on it')

my_car = Car('Toyota', 'Tacoma', 2000)
print(my_car.get_descriptive_name())

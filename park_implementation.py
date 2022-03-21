# Author: Palash Samir Haresh Gandhi
# ISDA: Python Developer Internship Test
# Date Of Writing: 21/03/2022
# Python File 1 of 2

from dataclasses import dataclass
from xmlrpc.client import Boolean

@dataclass
class Car:
    
    car_length: int
    car_time: int
    car_position: int = 0

    def __repr__(self) -> str:
        return f'Car -> Length: {self.car_length}, Time: {self.car_time})'

class Park:

    def __init__(self, park_length: int) -> None:
        self.park_length = park_length
        self.cars = []
        self.utilisation = [0 for i in range(park_length)]
        self.period = 0

    def park_car(self, car: Car) -> Boolean:
        for i in range(len(self.utilisation)-1):
            index = i + car.car_length
            if self.utilisation[i:index] == [0 for x in range(car.car_length)]:
                self.utilisation[i:index] = [1 for y in range(car.car_length)]
                car.car_position = i
                self.cars.append(car)
                return True
        return False
                
    def elapse_period(self) -> None:
        self.period += 1
        for i in range(len(self.cars)-1):
            if self.cars[i].car_time == self.period:
                pos = self.cars[i].car_position
                self.utilisation[pos:pos + self.cars[i].car_length] = [0 for x in range(self.cars[i].car_length)]
                self.cars.pop(i)

    def report_utilisation(self) -> None:
        used = 0
        for i in range(len(self.utilisation)-1):
            if self.utilisation[i] == 1:
                used += 1
        print("Park Utilisation:", used/self.park_length)


park = Park(10)

park.report_utilisation()

car1 = Car(2,2)
park.park_car(car1)
print(park.utilisation)
park.report_utilisation()

park.elapse_period()
car2 = Car(4,3)
park.park_car(car2)
park.report_utilisation()

park.elapse_period()
print(park.utilisation)
park.report_utilisation()
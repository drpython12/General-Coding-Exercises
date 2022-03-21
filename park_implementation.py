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

    def __repr__(self) -> str:
        return f'Car -> Length: {self.car_length}, Time: {self.car_time} )'

class Park:

    def __init__(self, park_length: int) -> None:
        self.park_length = park_length
        self.utilisation = 0
        self.period = 0

    def park_car(self, car: Car) -> Boolean:
        if car.car_length > (self.park_length-self.utilisation):
            return False
        else:
            self.utilisation += car.car_length
            return True

    def elapse_period(self) -> None:
        self.period += 1

    def report_utilisation(self) -> None:
        print(self.utilisation/self.park_length)
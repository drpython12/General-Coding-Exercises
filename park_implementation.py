# Author: Palash Samir Haresh Gandhi
# ISDA: Python Developer Internship Test
# Date Of Writing: 21/03/2022
# Python File 1 of 2

from dataclasses import dataclass
from xmlrpc.client import Boolean

@dataclass
class Car:
    
    car_length: int # Length of the car
    car_time: int # Number of periods car will be parked
    car_position: int = 0 # The starting position of the car in the parking array (default value 0)

    def __repr__(self) -> str:
        return f'Car -> Length: {self.car_length}, Time: {self.car_time}'

class Park:

    def __init__(self, park_length: int) -> None:
        self.park_length = park_length
        self.cars = [] # Array to store objects of type Car
        self.utilisation = [0 for i in range(park_length)] # Initialises array to park_length number of 0's

        '''
        self.cars stores instances of type car, this will help us access and manage
        the attributes of all cars inside the parking lot. 

        self.utilisation is initialised as an array consisting of park_length number
        of zeros. This array represents the 1-dimensional parking lot and will be
        used to track available parking spaces. 0 represents a free slot and 1
        represents a slot currently being used.
        '''

    def park_car(self, car: Car) -> Boolean:
        for i in range(len(self.utilisation)):
            index = i + car.car_length 
            if self.utilisation[i:index] == [0 for x in range(car.car_length)]: # Checks for consecutive 0's in parking array to fit the car passed as argument
                self.utilisation[i:index] = [1 for y in range(car.car_length)] # 0s in available space replaced by 1s to indicated parked car
                car.car_position = i # Start index of car instance in parking array is stored in car_position
                self.cars.append(car) # Car instance is appended to self.cars so we can access its attributes in other methods
                return True # True return if space found and car parked
        return False # False return if no consecutive 0s to fit car i.e. no space in lot for car of that length
                
    def elapse_period(self) -> None:
        to_pop = [] # Array to store index of Car instances to remove from self.cars once their periods have expired
        for i in range(len(self.cars)):
            self.cars[i].car_time -= 1 # Reduce car_time of each Car instance by 1 
            if self.cars[i].car_time == 0: # Check if parking time expired
                pos = self.cars[i].car_position
                self.utilisation[pos:pos + self.cars[i].car_length] = [0 for x in range(self.cars[i].car_length)] # Replace 1s with 0s indicating free slots
                to_pop.append(i) # Append index of Car instance to be removed
        for j in range(len(to_pop)):
            self.cars.pop(j) # Pop Car instances from self.cars array using indexes
            
    def report_utilisation(self) -> float:
        used = 0 # Number of used parking slots
        for i in range(len(self.utilisation)):
            if self.utilisation[i] == 1: 
                used += 1 # Incremented by one if a slot is not free
        return(float(used/self.park_length))

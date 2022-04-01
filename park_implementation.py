# Author: Palash Samir Haresh Gandhi
# ISDA: Python Developer Internship Test
# Date Of Writing: 31/03/2022
# Python File 1 of 2

from dataclasses import dataclass
from xmlrpc.client import Boolean

@dataclass
class Car:
    
    car_length: int # Length of the car
    car_time: int # Number of periods car will be parked

    start_position: int = 0 # The starting position of the car in the parking array (default value 0)
    end_position: int = 0 # The ending position of the car in the parking array (default value 0)

    def __repr__(self) -> str:
        return f'Car -> Length: {self.car_length}, Time: {self.car_time}, Start Position: {self.start_position}, End Position {self.end_position}'

class Park:

    def __init__(self, park_length: int) -> None:
        self.park_length = park_length
        self.cars = [] # Array to store object instances of type Car
        self.utilisation = 0 # Represents the number of slots currently being used

        '''
        self.cars stores instances of type car, this will help us access and manage
        the attributes of all cars inside the parking lot. 

        self.utilisation keeps track of the number of spots currently being used.
        '''

        ''' 
        Parking policy implemented:
        I chose to implement a "first fit" policy as I feel this is the most realistic representation and 
        simulation of a parking lot in real-time.
        '''

    def park_car(self, car: Car) -> Boolean:

        found = False 
        car.end_position = car.car_length - 1 # End position in best case scenario (empty parking)
        if self.utilisation == 0 and car.end_position < self.park_length: # If park is empty and car fits 
            self.utilisation += car.car_length # Add length of car to number of used spots
            self.cars.append(car) # Append Car object passed as argument to self.cars for later access
            return True # Return true as car parked successfully
        while(not found):
            for j in range(len(self.cars)): # Look through every car currently in park
                # While statement ensures that new car's start and end positions do not lie within
                # another car's start and end positions until we search all park slots
                while (self.cars[j].start_position <= car.start_position and self.cars[j].end_position >= car.start_position) or (self.cars[j].start_position <= car.end_position and self.cars[j].end_position >= car.end_position):
                    car.start_position += 1 # Increase start position by 1
                    car.end_position += 1 # Increase end position by 1
                    if car.end_position > self.park_length-1: # Return False if no space for car in park (prevents infinite loop)
                        car.start_position = -1 
                        car.end_position = -1 # Set to -1 to indicate no space found in park for car
                        return False
                                
                found = True # Parking found for car
        self.utilisation += car.car_length # Account for spots used by new car
        self.cars.append(car)
        return found
                    
    def elapse_period(self) -> None:
        i = 0 
        while i < len(self.cars):
            self.cars[i].car_time -= 1 # Reduce car_time of each Car instance by 1 
            if self.cars[i].car_time == 0: # Check if parking time expired
                self.utilisation -= self.cars[i].car_length
                del self.cars[i] # Delete instance of Car from array (car removed from park)
            i += 1
            
    def report_utilisation(self) -> float:
        return(float(self.utilisation)/self.park_length)

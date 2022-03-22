# Author: Palash Samir Haresh Gandhi
# ISDA: Python Developer Internship Test
# Date Of Writing: 21/03/2022
# Python File 2 of 2

import unittest
from park_implementation import Car, Park

# Test methods in the Park class
class TestParkMethods(unittest.TestCase):

    # Test the park_car method
    def test_park_car(self):
        park = Park(10)
        car1 = Car(2,2)
        self.assertEqual(park.park_car(car1), True)
        self.assertEqual(park.utilisation, [1,1,0,0,0,0,0,0,0,0])

        car2 = Car(4,2)
        self.assertEqual(park.park_car(car2), True)
        self.assertEqual(park.utilisation, [1,1,1,1,1,1,0,0,0,0])

        car3 = Car(5,4)
        self.assertEqual(park.park_car(car3), False)
        self.assertEqual(park.utilisation, [1,1,1,1,1,1,0,0,0,0])

    # Test the elapse_period method
    def test_elapse_period(self):
        park = Park(10)

        car1 = Car(2,2)
        park.park_car(car1)
        park.elapse_period()
        car2 = Car(4,3)
        park.park_car(car2)
        park.elapse_period()
        self.assertEqual(park.cars, [car2])
        self.assertEqual(park.utilisation, [0,0,1,1,1,1,0,0,0,0])

        park.elapse_period()
        park.elapse_period()
        park.elapse_period()
        self.assertEqual(park.cars, [])
        self.assertEqual(park.utilisation, [0,0,0,0,0,0,0,0,0,0])

    # Test the report_utilisation method
    def test_report_utilisation(self):
        park = Park(10)
        self.assertEqual(park.report_utilisation(), 0)

        car1 = Car(2,2)
        park.park_car(car1)
        self.assertEqual(park.report_utilisation(), 0.2)

        car2 = Car(4,3)
        park.park_car(car2)
        self.assertEqual(park.report_utilisation(), 0.6)

        park.elapse_period()
        park.elapse_period()
        self.assertEqual(park.report_utilisation(), 0.4)

if __name__ == '__main__':
    unittest.main()

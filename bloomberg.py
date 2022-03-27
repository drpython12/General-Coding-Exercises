'''

Bloomberg LP:
Practice Technical Interview Questions
Author: Palash Samir Haresh Gandhi

'''

'''
(1): Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
'''

from operator import truediv
from xmlrpc.client import boolean


def num_compare(*numbers) -> boolean:
    unique = True
    for i in range(len(numbers)-1):
        if numbers[i] in numbers[i+1:]:
            unique = False
    return unique

    
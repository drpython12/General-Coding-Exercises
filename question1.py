### Programming Assessment 2: Question 1

import math

value = int(input("Enter integer (0-99): "))
operation = str(input("Calculate additive or multiplicative persistance (a or m)? "))
count = 0
while value > 9:
    if operation == "a":
        value = math.floor(value/10) + (value%10)
    else:
        value = math.floor(value/10) * (value%10)
    count += 1
print("The persistence is:", count)
from math import pi

def radians_to_degrees(x):
    print(round((x * 180)/pi, 1))

radians_to_degrees(int(input("Enter radians: ")))
import math

x = int(input("sides = "))
y = int(input("lenght = "))

print("area of the polygoni", int( x * y**2 / (4 * math.tan(math.pi / x))))
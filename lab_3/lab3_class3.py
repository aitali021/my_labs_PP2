class Shape:
    def area(a):
        return 0
class Rectangle(Shape):
    def __init__(a, length, width):
        a.length = length
        a.width = width
    def area(a):
        return a.length * a.width

rect = Rectangle(33,1)
print("audany:", rect.area())

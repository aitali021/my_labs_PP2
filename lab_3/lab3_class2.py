class Shape:
    def area(a):
        return 0
class Square(Shape):
    def __init__(a, length):
        a.length = length
    def area(a):
        return a.length * a.length

sq = Square(12)
print("sharshi audany:", sq.area())

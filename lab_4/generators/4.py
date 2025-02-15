def kvadrat(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("a = "))
b = int(input("b = "))

for square in kvadrat(a, b):
    print(square, end = " ")
def generator(n):
    for i in range(1, n + 1):
        yield i ** 2

n = 3
for square in generator(n):
    print(square)
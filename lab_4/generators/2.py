def generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("n = "))
for even in generator(n):
    print(even, end = ", ")
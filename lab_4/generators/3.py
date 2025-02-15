def generator(n):
    for i in range(1, n + 1):
        if i % 3 == 0 & i % 4 == 0:
            yield i

n = int(input("n = "))
for ss in generator(n):
    print(ss, end = ", ")
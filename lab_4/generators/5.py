def generator(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("n = "))
for nolge_dein in generator(n):
    print(nolge_dein, end = " ")
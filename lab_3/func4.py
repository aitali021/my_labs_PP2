def primba_(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def tapp(numbers):
    return [num for num in numbers if primba_(num)]

print(tapp([10, 15, 3, 7, 19, 22, 29]))

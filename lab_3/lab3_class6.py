def jayma(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 7, 1000, 45, 19, 23, 1, -21]
prime_numbers = list(filter(lambda x: jayma(x), numbers))
print("jay san:", prime_numbers)

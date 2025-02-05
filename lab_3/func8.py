def spy_game(n):
    code = [0, 0, 7]
    for num in n:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

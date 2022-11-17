def multi(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multi((4, 3, 12, 5)))


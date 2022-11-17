def even_numbers(z):
    enum = []
    for n in z:
        if n % 2 == 0:
            enum.append(n)
    return enum


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

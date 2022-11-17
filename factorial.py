def factorial(z):
    if z == 0:
        return 1
    else:
        return z * factorial(z-1)


z = int(input("Enter a number to compute factorial : "))
print(factorial(z))


def factorial1(n):
    if not ((n >= 0) and (n % 1 == 0)):
        return "Number cannot be negative or floating point"
    return 1 if n == 0 else n * factorial(n - 1)


print("\nFactorial of 5: ", factorial1(5))
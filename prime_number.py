def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


n = int(input("enter number "))
print(test_prime(n))

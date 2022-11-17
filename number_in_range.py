def testo_range(n):
    if n in range(3, 12):
        print("  %s in the range" % str(n))
    else:
        print("Then number is outside given range")


n = input("enter number ")
testo_range(int(n))

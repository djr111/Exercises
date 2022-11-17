class MyClass:
    def __init__(self):
        self.num = 4
        self.message = "Hello"


def main():
    my_object = MyClass()
    print(my_object.message, my_object.num)


if __name__ == '__main__':
    main()

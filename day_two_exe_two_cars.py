class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def print_info(self):
        print("Model: " + self.model)
        print("Color: " + self.color)


if __name__ == "__main__":
    my_car = Car("Volvo", "Blue")
    my_car.print_info()
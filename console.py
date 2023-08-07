class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        print("Engine started!")

    def stop_engine(self):
        print("Engine stopped.")


def main():
    my_car = Car("Toyota", "Camry", 2023)
    print(my_car.get_info())
    my_car.start_engine()
    my_car.stop_engine()


if __name__ == "__main__":
    main()

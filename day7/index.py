class Car:
    # Class variable (shared among all instances)
    wheels = 4

    def __init__(self, brand, model, year, color):
        # Instance variables (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"The {self.color} {self.brand} {self.model} is now running.")

    def stop(self):
        self.is_running = False
        print(f"The {self.color} {self.brand} {self.model} has stopped.")

    def display_info(self):
        print(f"{self.year} {self.color} {self.brand} {self.model}, Wheels: {Car.wheels}")


# Creating and using car objects
car1 = Car("Toyota", "Corolla", 2020, "Red")
car2 = Car("Honda", "Civic", 2022, "Blue")

car1.start()
car1.display_info()
car1.stop()

car2.display_info()

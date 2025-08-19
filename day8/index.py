import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must override this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must override this method")

    def __str__(self):
        return f"{self.name} with area {self.area():.2f} and perimeter {self.perimeter():.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.__radius = radius  

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Radius must be positive.")

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.__radius + other.__radius)
        raise TypeError("Only circles can be added together")

    def __str__(self):
        return f"Circle with radius {self.__radius}, area {self.area():.2f}"



class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Rectangle')
        self._width = width    
        self._height = height  

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return f"Rectangle (W={self._width}, H={self._height}), area {self.area():.2f}"


def print_shape_info(shape):
    print(f"Shape Type: {shape.name}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()



if __name__ == "__main__":

    c1 = Circle(5)
    c2 = Circle(3)
    r1 = Rectangle(4, 6)

    
    print(c1)
    print(c2)
    print(r1)
    print()

    
    for shape in [c1, c2, r1]:
        print_shape_info(shape)

    print(f"Old radius of c1: {c1.get_radius()}")
    c1.set_radius(10)
    print(f"New radius of c1: {c1.get_radius()}")
    print()

    c3 = c1 + c2
    print(f"Added circles: {c3}")
    print()

    print(f"repr(c1): {repr(c1)}")
    print(f"repr(r1): {repr(r1)}")

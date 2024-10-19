from math import pi, sqrt

class Figure():

    sides_count = 0

    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if ((0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255)):
            return True
        else:
            return False

    def set_color (self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("Введенные цвета некорректны")

    def __is_valid_sides(self, *sides):
        if isinstance(all(sides), int) and all(sides) > 0 and len(sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(i for i in self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            self.__sides = (1)*self.sides_count


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides/(2*pi)

    def get_square(self):
        return (2 * pi * self.__radius**2)

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides = sides
        self.color = color

    def get_square(self):
        p = sum(self.sides) / 2
        return sqrt(p*(p - self.sides[0])*(p - self.sides[1])*(p - self.sides[2]))

class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, [sides]*self.sides_count)


    def get_volume(self):
        return self._Figure__sides[0]**3


circle1 = Circle((221, 121, 53), 12)
print(circle1.get_color())
print(circle1.get_sides())
print(circle1.get_square())
circle1.set_color(123, 32, 265)
print(circle1.get_color(), "\n")

tri = Triangle((123, 240, 187), (3, 4, 5))
print(len(tri))
print(tri.get_color())
print(tri.get_sides())
print(tri.get_square())
tri.set_sides(3)
print(tri.get_sides())
tri.set_color(123, 32, 225)
print(tri.get_color(), "\n")

cube = Cube((123, 240, 187), 6)
print(len(cube))
print(cube.get_color())
print(cube.get_sides())
print(cube.get_volume())
cube.set_color(123, 32, 225)
print(cube.get_color())
import math


class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = [None, None, None]
        self.filled = False
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.set_color(color[0], color[1], color[2])
        if self.sides_count == len(sides) and self.__is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):

        return self.__color

    def __is_valid_color(self, r, g, b):

        if  ((0 <= r <= 255) and (0 <= g <= 255) and  (0 <= b <= 255)):
            return True
        else:
            return False

    def set_color(self, r, g, b):

        if not self.__is_valid_color(r, g, b):
            return False
        else:
            temp = list()
            temp.append(r)
            temp.append(g)
            temp.append(b)
            self.__color = temp
            self.filled = True
            return True

    def __is_valid_sides(self, *args):
        flag = True
        if isinstance((args[0]),int) == True and len(args) == 1:
            return True
        else:
            for i in args:
                if i < 0:
                    flag = False
                    break
            if flag and len(args) == self.sides_count:
                return True
        return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides.clear()
            for j in sides:
                self.__sides.append(j)


   #def _len(self):
   #     return self.perimetr

    def get_sides(self):

        return self.__sides

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius =self.get_sides()[0] / 2 * math.pi

    def get_square(self):

        return math.pi * self.__radius**2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side_cub = sides * 12
        super().__init__(color, *side_cub)

    def get_volume(self):
        return self.get_sides()[0] ** 3

class Triangle(Figure):
    sides_count = 3

    def __init(self, color, *sides):
        super().__init(color, *sides)
        self.__height = self.get_height()

    def get_height(self):
        p = self.__len__()/2
        return (2 * math.sqrt(p * (p - self.get_sides()[0]) *
                         (p - self.get_sides()[1]) *
                         (p - self.get_sides()[2]))) / self.get_sides()[0]

    def get_square(self):
        return (self.get_sides()[0] * self.get_height()) / 2

    def set_sides(self, *sides):
        super().set_sides(*sides)
        if (self.get_sides()[0] + self.get_sides()[1] > self.get_sides()[2] and
            self.get_sides()[1] + self.get_sides()[2] > self.get_sides()[0] and
            self.get_sides()[2] + self.get_sides()[0] > self.get_sides()[1]):
            self.__height = self.get_height()

        else:

            self.set_sides(1, 1, 1)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

tria = Triangle((200, 200, 50), 30)
print((tria.get_color()))
print(tria.get_sides(),'tria')
tria.set_sides(45,56,78,9)
print(tria.get_sides())

tria.set_sides(45,56,78)
print(tria.get_sides())



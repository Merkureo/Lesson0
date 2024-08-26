# Задание "Они все так похожи":
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны
# и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b,
# который проверяет корректность переданных значений перед установкой нового цвета.
# Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
# возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
# False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны,
# если их количество не равно sides_count, то не изменять, в противном случае - менять.
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
#
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон,
# если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

import math


class Figure:
    sides_count = 0

    def __init__(self, filled=False):
        self.__sides = []
        self.__color = [None, None, None]
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return ((isinstance(r, int) or isinstance(g, int) or isinstance(b, int)) and
                0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
            self.filled = True

    def __is_valid_sides(self, *args):
        result = True
        for elements in args:
            if not isinstance(elements, int):
                result = False
        if len(args) != self.sides_count:
            result = False
        return result

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides[:])


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args):
        super().__init__()
        if isinstance(args[0], tuple | list) & 0 < len(args[0]) < 4:
            self.set_color(args[0][0], args[0][1], args[0][2])
            self.set_sides(*args[1:])
        else:
            self.set_sides(*args)
        self.__radius = self.__len__() / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.__len__() / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__()
        if isinstance(args[0], tuple | list) & 0 < len(args[0]) < 4:
            self.set_color(args[0][0], args[0][1], args[0][2])
            self.set_sides(*args[1:])
        else:
            self.set_sides(*args)

    def get_square(self):
        sides = super().get_sides()
        p = self.__len__() / 2

        return math.sqrt(p*(p - sides[0])*(p - sides[1])*(p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        super().__init__()
        if isinstance(args[0], tuple | list) & 0 < len(args[0]) < 4:
            self.set_color(args[0][0], args[0][1], args[0][2])
            self.set_sides(*args[1:])
        else:
            self.set_sides(*args)

    def set_sides(self, *new_sides):
        if 0 < len(new_sides) < 2:
            _new_sides = []
            for number_side in range(self.sides_count):
                _new_sides.append(new_sides[0])
            super().set_sides(*_new_sides)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0]*sides[1]*sides[2]


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта,
# тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors == other
        elif isinstance(other, str):
            if other.isdigit():
                return self.number_of_floors == int(other)
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(other)} не подходит для сравнения с типом {type(self)}')

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors < other
        elif isinstance(other, str):
            if other.isdigit():
                return self.number_of_floors < int(other)
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(other)} не подходит для сравнения с типом {type(self)}')

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors > other
        elif isinstance(other, str):
            if other.isdigit():
                return self.number_of_floors > int(other)
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(other)} не подходит для сравнения с типом {type(self)}')

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

# Все арифметические операции сделаны по заданию!
# НО я не согласен с логикой поставленной в задании!
# Закомментированные реализации - это моё видение логики работы арифметических операций

    def __add__(self, value):
        if isinstance(value, type(self)):
            # tmp = House(self.name, self.number_of_floors + value.number_of_floors)
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            # tmp = House(self.name, self.number_of_floors + value)
            self.number_of_floors += value
        elif isinstance(value, str):
            if value.isdigit():
                # tmp = House(self.name, self.number_of_floors + int(value))
                self.number_of_floors += int(value)
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит сложения с типом {type(self)}')
        # return tmp
        return self

    def __radd__(self, value):
        # в задании указано:
        # __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова)
        # поэтому сделал такую реализацию
        return self + value
        # поскольку метод __radd__ вызывается,
        # когда к типу данных отличному от типа данных нашего класса прибавляют объект нашего класса
        # считаю более логичным возвращать значение того же типа данных, что и объект с которым складываем
        # if isinstance(value, int):
        #     tmp = value + self.number_of_floors
        # elif isinstance(value, str):
        #     if value.isdigit():
        #         tmp = str(int(value) + self.number_of_floors)
        #     else:
        #         raise ValueError('переданное значение не является целым числом')
        # else:
        #     raise TypeError(f'Тип {type(value)} не подходит сложения с типом {type(self)}')
        # return tmp

    def __iadd__(self, value):
        return self + value

# остальные арифметические операции делаю по своему усмотрению

    def __sub__(self, value):
        if isinstance(value, type(self)):
            tmp = House(self.name, self.number_of_floors - value.number_of_floors)
        elif isinstance(value, int):
            tmp = House(self.name, self.number_of_floors - value)
        elif isinstance(value, str):
            if value.isdigit():
                tmp = House(self.name, self.number_of_floors - int(value))
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит для вычитания с типом {type(self)}')
        return tmp

    def __rsub__(self, value):
        if isinstance(value, int):
            tmp = value - self.number_of_floors
        elif isinstance(value, str):
            if value.isdigit():
                tmp = str(self.number_of_floors + int(value))
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит для вычитания с типом {type(self)}')
        return tmp

    def __isub__(self, value):
        return self - value

    def __mul__(self, value):
        if isinstance(value, type(self)):
            tmp = House(self.name, self.number_of_floors * value.number_of_floors)
        elif isinstance(value, int):
            tmp = House(self.name, self.number_of_floors * value)
        elif isinstance(value, str):
            if value.isdigit():
                tmp = House(self.name, self.number_of_floors * int(value))
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит для умножения с типом {type(self)}')
        return tmp

    def __rmul__(self, value):
        if isinstance(value, int):
            tmp = value * self.number_of_floors
        elif isinstance(value, str):
            if value.isdigit():
                tmp = str(self.number_of_floors * int(value))
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит для умножения с типом {type(self)}')
        return tmp

    def __imul__(self, value):
        return self * value

    def __truediv__(self, value):
        if isinstance(value, type(self)):
            tmp = House(self.name, self.number_of_floors / value.number_of_floors)
        elif isinstance(value, int):
            tmp = House(self.name, self.number_of_floors / value)
        elif isinstance(value, str):
            if value.isdigit():
                tmp = House(self.name, self.number_of_floors / int(value))
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит для деления с типом {type(self)}')
        return tmp

    def __rtruediv__(self, value):
        if isinstance(value, int):
            tmp = value / self.number_of_floors
        elif isinstance(value, str):
            if value.isdigit():
                tmp = str(int(value) / self.number_of_floors)
            else:
                raise ValueError('переданное значение не является целым числом')
        else:
            raise TypeError(f'Тип {type(value)} не подходит для деления с типом {type(self)}')
        return tmp

    def __itruediv__(self, other):
        return self / other

    def go_to(self, new_floors):
        if self.number_of_floors >= new_floors > 0:
            for i in range(1, new_floors + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
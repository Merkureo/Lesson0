# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и
# возвращать результаты сравнения по соответствующим операторам.
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения
# и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(len(h1))
print(len(h2))
print(h1)
print(h2)
print(h1 == h2)
print(h1 == 18)
print(h1 == '10')
# print(h2 == '10.2')
# print(h1 == [1, 2])
print(h1.number_of_floors)
print(h2.number_of_floors)
print(' сложение')
h3 = h1 + h2
h4 = h1 + 10
h5 = 8 + h2
h2 += h1
print(h1.number_of_floors)
print(h2.number_of_floors)
print(h3.number_of_floors)
print(h4.number_of_floors)
print(h5.number_of_floors)
print(' вычитание')
h3 = h1 - h2
h4 = h1 - 10
h5 = 8 - h2
h2 -= h1
print(h1.number_of_floors)
print(h2.number_of_floors)
print(h3.number_of_floors)
print(h4.number_of_floors)
print(h5)
print(' умножение')
h3 = h1 * h2
h4 = h1 * 10
h5 = 8 * h2
h2 *= h1
print(h1.number_of_floors)
print(h2.number_of_floors)
print(h3.number_of_floors)
print(h4.number_of_floors)
print(h5)
print(' деление')
h3 = h1 / h2
h4 = h1 / 10
h5 = 8 / h2
h2 /= h1
print(h1.number_of_floors)
print(h2.number_of_floors)
print(h3.number_of_floors)
print(h4.number_of_floors)
print(h5)

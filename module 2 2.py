# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0

# Вводим первое число
first = input('Введите первое целое число: ')

# Проверяем правильно ли ввели первое целое число
if not first.isdigit():
    print('Введеное значение не является целым числом. Программа завершается.')
    exit(-1)
else:
    first = int(first)

# Вводим второе число
second = input('Введите второе целое число: ')

# Проверяем правильно ли ввели второе целое число
if not second.isdigit():
    print('Введеное значение не является целым числом. Программа завершается.')
    exit(-1)
else:
    second = int(second)

# Вводим третье число
third = input('Введите третье целое число: ')

# Проверяем правильно ли ввели третье целое число
if not third.isdigit():
    print('Введеное значение не является целым числом. Программа завершается.')
    exit(-1)
else:
    third = int(third)

# Проверяем равны ли первое и второе число
if first == second and second == third:
    matches = 3
elif first == second or second == third or first == third:
    matches = 2
else:
    matches = 0

print('Введено одинаковых чисел:', matches)

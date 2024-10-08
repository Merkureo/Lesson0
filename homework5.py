# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

immutable_var = (1, 0.5, "test", True, [2, 1.5, 'test2', True, (3, 2.5, "test3", True)], (4, 3.5, "test4", True))
print(immutable_var)

# целые числа, дробные числа, строки, логические переменные - при изменении меняют адрес(создаются новые объекты), поэтому в кортеже их изменить нельзя
# будет ошибка, код не выполнится
# тут ошибка
# immutable_var[3] = False
# но если в картеже список, то его можно изменить. адресс самого списка не меняется, а меняется его содержимое
immutable_var[4][0] = 1000
immutable_var[4][1] += 10
immutable_var[4][2] = immutable_var[4][2] + '000'
immutable_var[4][3] = False
immutable_var[4][4] = (1,2,3)
# в списке можно заменить кортеж
# или увеличить его
immutable_var[4][4] += (0,9,8)
# но нельзя из менить значения внутри кортежа
# тут ошибка
# immutable_var[4][4][0] = 5
print(immutable_var)
# то же самое с кортежем в кортеже
# Тут ошибка
# immutable_var[5][0] = 5

mutable_list = [2, 1.5, 'test2', True, (3, 2.5, "test3", True)]
print(mutable_list)
mutable_list[0] = 1000
mutable_list[1] += 10
mutable_list[2] = mutable_list[4][2] + '000'
mutable_list[3] = False
mutable_list[4] = (1,2,3)
# в списке можно заменить кортеж
# или увеличить его
mutable_list[4] += (0,9,8)
# но нельзя из менить значения внутри кортежа
# тут ошибка
# mutable_list[4][0] = 5
print(mutable_list)
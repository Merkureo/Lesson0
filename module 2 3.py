# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор,
# пока не встретите отрицательное или не закончится список (выход за границу).

# список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# длинна списка
length = len(my_list)
# счетчик
i = 0
# цикл для перебора элементов
# работает пока не дойдём до конца списка
while i < length:
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1
# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению,
# в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    res = (len(string),string.upper(),string.lower())
    return res


# можно указывать тип данных который будем передавать в функцию, получается питон можно сделать стороготипизированым?
def is_contains(string: str, input_list: list[str]):
    count_calls()
    for i in range(len(input_list)):
        input_list[i] = input_list[i].lower()
    return string.lower() in input_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Все ученики урбана, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том,
# что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
# Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом:
# "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам
# - универсального решения для таких структур он не нашёл.


def calculate_structure_sum(*args):
    result = 0
    type_of_struct = args[0]
    # Данный подход не определяет тип bool, он считает его int (преобразование True в 1 и False в 0)
    # но в условии задачи его обработки нет, а если его обрабатывать как 0 и 1 то метод работает.
    # В задании рекомендуется использовать метод isinstance, но мне показалась такая реализация интереснее,
    # возможно тут тратиться больше ресурсов (я же создаю пустые объекты в каждом case),
    # но по записи мне больше понравилось (смотри вторую реализацию)
    match type_of_struct:
        case (int() | float()):
            result += args[0]
        case (str()):
            result += len(args[0])
        case (list() | tuple() | set()):
            for i in args[0]:
                result += calculate_structure_sum(i)
        case (dict()):
            for key, value in args[0].items():
                result += calculate_structure_sum(key)
                result += calculate_structure_sum(value)
    return result


def calculate_structure_sum_2(*args):
    result = 0
    type_of_struct = args[0]
    if isinstance(args[0], int | float):
        result += args[0]
    elif isinstance(args[0], str):
        result += len(args[0])
    elif isinstance(args[0], list | tuple | set):
        for i in args[0]:
            result += calculate_structure_sum_2(i)
    elif isinstance(args[0], dict):
        for key, value in args[0].items():
            result += calculate_structure_sum_2(key)
            result += calculate_structure_sum_2(value)
    return result


# это я тестировал свой метод на простых примерах
# print(calculate_structure_sum(5))
# print(calculate_structure_sum(5.0))
# print(calculate_structure_sum('5'))
# print(calculate_structure_sum(True))
# print(calculate_structure_sum(False))
# print(calculate_structure_sum([5, 4, 5]))
# print(calculate_structure_sum((5, 3, 4, 4, True)))
# print(calculate_structure_sum({5, 3, 4, 4}))
# print(calculate_structure_sum({'q': 5, 'w': 3, "e": 4, "r": 4}))

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

result = calculate_structure_sum_2(data_structure)
print(result)

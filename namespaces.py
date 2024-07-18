# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm.
# Запустите созданный проект
# Ваша задача:
# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function.
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# Полученный код напишите в ответ к домашнему заданию

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    # здесь inner_function успешно вызывается и выполняется, если есть вызов test_function
    # поскольку inner_function расположен в "локальной" области видимости функции test_function
    inner_function()


# test_function успешно выполнилась, поскольку находиться в "глобальной области видимости"
test_function()
# интерпретатор выдаёт ошибку:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# в "глобальной" области видимости нет функции с именем inner_function,
# поскольку она объявлена в "локальной" области видимости
inner_function()

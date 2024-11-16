# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings),
# которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions,
# где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

def custom_write(file_name, strings: list):
    strings_positions = dict()
    file = open(file_name, 'a+')
    # берем стартовую позицию
    # если файл не новый получим значение отличное от 0
    # значит нужно добавить перенос строки, что бы ранее записанное в файл не слиплось с новой строкой
    start_position = file.tell()
    number_line = 0
    if start_position != 0:
        # переносим курсор на начало файла, читаем весь файл и
        # считываем все строки
        # и добавляем строки в словарь (в задании нет, но решил добавить)
        file.seek(0)
        start_position = file.tell()
        string = file.readline()
        while string != '':
            number_line += 1
            strings_positions[(number_line, start_position)] = string
            start_position = file.tell()
            string = file.readline()
        # добавляем перенос строки для добавления новых строк
        file.write('\n')
    for line in strings:
        start_position = file.tell()
        number_line += 1
        strings_positions[(number_line, start_position)] = line
        file.write(line + '\n')
    file.close()
    file = open(file_name, 'ab')
    # в конце добавляется лишний перенос строки, использую truncate что бы удалить его
    # -2 это размер в байтах, многое зависит от используемой кодировки. есть более надежный способ?
    file.truncate(file.tell() - 2)
    file.close()
    return strings_positions


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

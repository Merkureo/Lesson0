# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# перобразуем множество в список
students = list(students)
# сортируем список в алфавитном порядке
students.sort()
# создаем словарь
average_mark = dict()
# проходим в цикле по студентам
for i in range(len(students)):
    # инициализируем переменную для хранения средней оценки
    # ? требуетсяли начальная инициализация? что будет в переменной если ее объявть mark:Float?
    mark = 0.0
    # вычисляем средний бал
    for j in range(len(grades[i])):
        mark += grades[i][j]
    mark = mark/len(grades[i])
    # добавляем в словарь имя студента и его средний бал
    average_mark[students[i]] = mark
# выводим список
print(average_mark)

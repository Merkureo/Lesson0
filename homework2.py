# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

cout_made_homework = 12
cout_spent_hours = 1.5
name_of_course = 'Python'
time_by_exercise = cout_spent_hours / cout_made_homework
# в задании после "задач:" нет пробеда перед числом. а после часов есть, предположил что опечатка!
final_string = 'Курс: ' + name_of_course + ', всего задач: ' + str(cout_made_homework) + ', затрачено часов: ' + str(cout_spent_hours) + ', среднее время выполнения ' + str(time_by_exercise) + ' часа.'
print(final_string)
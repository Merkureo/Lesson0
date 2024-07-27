# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы,
# где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.).
# Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
#
# Именно вам выпала возможность продемонстрировать их,
# написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
#
# Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой,
# каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
# time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы:
# nickname, password и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента:
# nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует".
# После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
# если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
# содержащих поисковое слово.
# Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
# В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
# т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

# Принял решение использовать hashlib,
# поскольку стандартная функция hash при каждом запуске генерирует разные хеши.
# Использую sha256
import hashlib
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        h = hashlib.new('sha256')
        h.update(password.encode())
        self.password = h.hexdigest()
        self.age = age


class Video:
    def __init__(self, title, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []

    def __init__(self, user=None):
        if user is not None:
            if user in self.users:
                self.current_user = user
            else:
                print(f'Пользователь {user.nickname} не найден')
                self.current_user = None
        else:
            self.current_user = None
            print('Вы не вошли в систему')

    def number_user_register(self, nickname):
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname:
                return i
        return -1

    def log_in(self, nickname, password):
        # Если нет зарегистрированных пользователей
        if len(self.users) == 0:
            print('Нет зарегистрированных пользователей!')
        number = self.number_user_register(nickname)
        if number >= 0:
            # Использовал для отладки. В ТЗ отсутствует
            # print(f'Пользователь {nickname} найден!')
            h = hashlib.new('sha256')
            h.update(password.encode())
            if self.users[number].password == h.hexdigest():
                self.current_user = self.users[number]
            else:
                print(f'Вы ввели не правильный пароль для пользователя {nickname}')
                self.current_user = None
        # Использовал для отладки. В ТЗ отсутствует
        # else:
            # print(f'Пользователь {nickname} не найден!')

    def register(self, nickname, password, age):
        number = self.number_user_register(nickname)
        if number >= 0:
            print(f'Пользователь {nickname} уже существует')
        else:
            u = User(nickname, password, age)
            self.users.append(u)
            self.log_in(nickname, password)
            # Использовал для отладки. В ТЗ отсутствует
            # print(f'Пользователь {nickname} успешно зарегистрирован, вход выполнен')

    def log_out(self):
        self.current_user = None
        print('Выход выполнен')

    def add(self, *args):
        is_new_video = True
        for i in range(len(args)):
            if isinstance(args[i], Video):
                for j in self.videos:
                    if j.title == args[i].title:
                        is_new_video = False
                if is_new_video:
                    self.videos.append(args[i])
                else:
                    print(f'Видео с названием {args[i].title} уже существует')
            else:
                print(f'Вы передали данные типа {type(args[i])}, а ожидается тип Video')

    def get_videos(self, search_word:str):
        result = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                result.append(i.title)
        return result

    def watch_video(self, video_name):
        for i in self.videos:
            if video_name == i.title:
                if self.current_user is not None:
                    if i.adult_mode and self.current_user.age >= 18:
                        for sec in range(i.duration):
                            i.time_now += 1
                            sleep(1.0)
                            print(i.time_now, end=' ')
                        print('Конец видео')
                        i.time_now = 0
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                break


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
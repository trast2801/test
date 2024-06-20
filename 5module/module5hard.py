import time
from os import remove
from random import random, randint


class Video:
    def __init__(self, title : str, duration : int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    count = 0
    def __init__(self, nickname: str, age: str, password: str):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)
        User.count += 1

class UrTube:

    def __init__(self, users: [], videos: [], current_user : User):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login: str, password: str):
        password = hash(password)
        for k in self.users:
            if k.nickname == login and k.password == password:
               self.current_user = k
        return
    def register(self, nickname: str, password: str, age: str):
        for k in self.users:
            if k.nickname == nickname:
                print(f'\nПользователь {nickname} существует ')
                return False
        user = User(nickname, age, password)
        self.users.append(user)
        self.current_user = user
        return True

    def show_users(self):
        for i in self.users:
            print(i.nickname, i.age, i.password)

    def fill_bd(self):
        #заполнение БД тестовыми данными
        for i in range (0,10):
            self.users.append(User('support' + str(i), randint(15, 90), 'passwd'+ str(randint(1,100))))

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for k in args:
            flag = False
            for l in self.videos:
                if l.title == k.title:
                    flag = True
                    break
            if flag:
                continue
            else:
                self.videos.append(k)

    def get_videos(self, substr: str):
        spisok = []
        for k in self.videos:
            if k.title.lower().find(substr.lower()) != -1:
                spisok.append(k.title)
        return spisok

    def list_video(self):
        for k in self.videos:
            print(k.title)

    def watch_video(self, title):
        for k in self.videos:
            if title == (k.title):

                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                    return

                if int(self.current_user.age) < 18 and (k.adult_mode == True):
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    for i in range(0, k.duration):
                        k.time_now = i
                        time.sleep(1)
                        print(k.time_now, end=" "),
                    k.time_now = 0


if __name__ == '__main__':

    ur = UrTube([],[],None)
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
    hill = UrTube
    while True:
        choice = input('\nДобро пожаловать в Свой YouTube\n'
                   '___________________________________\n'
                   'Нажмите 1 - для регистрации \n'
                   'Нажмите 2 - входа\n'
                   'Нажмите 3 - если хотите удалить пользователя\n'
                   'Нажмите 4 - для получения списка пользователей\n'
                   'Нажмите 5 - для выхода из Свой YouTube'    
                   'Нажмите 0 - если хотите закончить\n')
        if choice == '0':
            print('До свидания')
            exit()
        if choice == '1':
            login  = input('Введите логин:')
            passwd = input('Введите пароль:')
            age    = input('Введите Ваш возраст:')
            if hill.register(login, passwd, age):
                print ('Регистрация прошла успешно, Вы в системе')
            else:
                continue
        if choice == '2':
            hill.log_in(input('\nВведите логин:'), input('Введите пароль:'))
        if choice == 5:
            hill.log_out()
        if choice == '4':
            hill.show_users()

#КОД НИЖЕ ДЛЯ ТЕНИРОВКИ
class Database:

    def __init__(self, user: User):
        self.data = []

    def add_user(self, user: User):
        #self.data[username] = hash(password)
        #self.data = user
        self.data.append(user)

    def find_user(self, username):
    # перебор по слоавврю если найден, то возвращаю 1 иначе 0
        for k in self.data:
            if k.nickname == username:
                return True
        return False

    def dell_user(self, username):
        # сделать проверку на наличие ключа в БД, возвращает 0, если все успешно и -1 есди не найден
        for k in self.data:
            if k.nickname == username:
                self.data.remove(k)
                print('Пользователь удален')
                return True
        else:
            print('Пользователь не найден')
            return False

    def spisok_all_users_in_BD(self):
        for k in self.data:
            print(k.nickname, k.age, k.password)

    def fill_BD(self):

        for k in range (0,10):
           k = User('support' + str(k), randint(15, 90), hash(str(random() * 10) + ' password '))
           self.add_user(k)
        self.add_user(User("konst", 45, '123'))
    def log_in(self, username, password):
        for k in self.data:
            if k.nickname == username:
                if k.password == hash(password):
                    print('Прошёл')
                    return True
                else:
                    print('Пароль не совпадает')
                    return False


def reg(exemplar : Database):
    # проверка на наличие полльзователя в БД и регистрация нового
    while True:
        new_user_name = input ('Введите логин (или нажмите Enter для выхода):')
        if len(new_user_name) == 0:
            return False
        elif exemplar.find_user(new_user_name):
            print('такой пользователь уже зарегистрирован')
            continue
        else:
            #написать функцию, которая скрывает вводимы пароль
            password = input('Введите пароль:')
            check_pass = input('Введите пароль ещё раз:')
            if password == check_pass:

                exemplar.add_user(User(new_user_name, password, input('\nВаш возраст: ')))
                return True
            else:
                print('Пароли не совпадают, начните сначала')

'''
if __name__ == '__main__':
    user = User('www',23, 'dddf')
    exemplar = Database(user)
    exemplar.fill_BD() #заполнение БД тестовыми данными
    while True:
        ss = input('\nДобро пожаловать в Свой YouTube\n'
                   '___________________________________\n'
              'Наберите 1 - если хотите зарегистрироваться\n'
              'Наберите 2 - если регистрация уже прошла\n'
              'Наберите 3 - если хотите удалить пользователя\n'
              'Наберите 4 - для получения списка пользователей\n'     
              'Наберите 0 - если хоите закончить\n')
        if ss == '0':
            print('До свидания')
            exit()
        if ss == '1':
            reg(exemplar)
        if ss == '2':
            username = input('\n Введите логин:')
            if exemplar.find_user(username): #оптимизировать функцию поиска при регистраии и лоигне (использовать одну)
               password = input('\n Введите пароль:')
               exemplar.log_in(username, password)
            else:
                print('Такого пользователя в базе не зарегистрировано')
        if ss == '3':
            kk = input('Введите имя: ')
            exemplar.dell_user(kk)
        if ss == '4':

            exemplar.spisok_all_users_in_BD()
        else:
            continue
'''




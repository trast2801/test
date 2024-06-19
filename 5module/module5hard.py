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
    def __init__(self, nickname : str, age : int, password : int):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)
        User.count += 1

class UrTube:

    def __init__(self, users: [], videos: [], current_user: User):
        self.users = users
        self.video = videos
        self.current_user = current_user

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
    def login(self, username, password):
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
               exemplar.login(username, password)
            else:
                print('Такого пользователя в базе не зарегистрировано')
        if ss == '3':
            kk = input('Введите имя: ')
            exemplar.dell_user(kk)
        if ss == '4':

            exemplar.spisok_all_users_in_BD()
        else:
            continue





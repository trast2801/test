from random import random


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
        self.username = user.nickname
        self.age = user.age
        self.password = user.password

    def add_user(self, user: User):
        #self.data[username] = hash(password)
        #self.data = user
        self.data.append(user)

    def find_user(self, username):
    # перебор по слоавврю если найден, то возвращаю 1 иначе 0
        for k in self.data:
            if k == username:
                return True
        return False

    def dell_user(self, username):
        # сделать проверку на наличие ключа в БД, возвращает 0, если все успешно и -1 есди не найден
        if self.find_user(username):
                del self.data[username]
                print(' удален')
                return
        else:
            print('Пользователь не найден')

    def spisok_all_users_in_BD(self):
        for k in self.data:
            print(k.nickname, k.age, k.password)


    def fill_BD(self):
        for k in range (0,10):
           k = User('support' + str(k), 45, hash(str(random() * 10) + ' password '))
           self.add_user(k)
        #self.add_user(User('support3', 45, str(random() * 10) + ' password '))
        #for k in range(0,10):
           #self.add_user(User(k, k, str(random() * 10) +  ' password '))
           #self.add_user(k, str(random() * 10) +  ' password ')
        #for k in self.data:
        #    print(k)

    def login(self, username, password):
        for k in self.data:
            if k == username:
                if self.data[k] == hash(password):
                    print('Прошёл')
                    return True
                else:
                    print('Парль не совпадает')
                    return False


def reg(exemplar : Database):
    # проверка на наличие полльзователя в БД и регистрация нового
    while True:
        new_user_name = input ('Введите логин (nили нажмите Enter для выхода):')
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


if __name__ == '__main__':
    user = User('www',23, 'dddf')
    exemplar = Database(user)
    exemplar.fill_BD() #заполнение БД тестовыми данными
    while True:
        ss = input('Добро пожаловать в Свой YouTube\n'
              'Наберите 1 - если хотете зарегистрироваться\n'
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
            exemplar.dell_user(input('Введите имя: '))
        if ss == '4':

            exemplar.spisok_all_users_in_BD()
        else:
            continue





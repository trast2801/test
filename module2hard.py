from datetime import time
from random import random, randrange


def passWord(number, size_of_array):
    array =  [] # массив цифр из которых сосотит пароль
    result = ""
    i = 1
    while i <= size_of_array: # заполнение массива элементами пароля
        array.append(i)
        i += 1

    for i in range (1, 20):
        for j in range (i + 1, 20):
            if number % (i + j) == 0:
                result += str(i) + str(j)

    return (result)
def head():
    choice = None
    while True:
        choice = int(input ('\nВыберите как генерить число: '
                        '\n 1. случайно - введите 1, '
                        '\n 2. любое положительное число в интервале от 1 до 20'
                        '\n 3. 0 - для выхода: '))
        if choice == 1:
            choice = randrange(20)
            print(f'Сгенерили значение: - {choice}')

        if choice < 0 or choice > 20:
            print ('\nОшибка, Введите число в интервале от 1 до 20')
        else:
            if choice == 0:
                print('\nЗакончили, спасибо')
                break
            print(f'\nПароль - {passWord(choice, 20)}\n')

head()


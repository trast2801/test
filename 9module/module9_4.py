#первая версия задания
'''from curses.ascii import isupper
def all_variants(text, ind=0):
    for i in range(0, len(text)+1):
        j = i+1
        for k in range(j, len(text)+1):
            yield text[i:k]
print(sorted(list(all_variants('abc')), key = len))
int_list = (1,2.34, 6, 8, 10 ,3.3, 15, 20.34, 100)
result = map(lambda x: x * 10, int_list)
result = list(second)

#-----------------------------------
int_list = [1,2.34, 6, 8, 10 ,3.3, 15, 20.34, 100]
def one(n):
        def two(y):
                return n * y
        return two

by_5 = one(5)
print(by_5(y=42))


by_10 = one(1000)
print(list(map(by_10,int_list)))



int_list2 = [10, 23.4, 60, 80, 100, 33.0, 150, 203.4, 1000]


def mul(s):
        return s * 10
'''
#lambda
#------------------------------------
first  = 'Мама мыла раму'
second = 'Рамена мало было'

def tst (one, two):
        if one == two:
                return True
        else:
                return False

print (list(map(lambda x, y: True if x == y else False, second, first)))

#замыкание
#-----------------------------------
def  get_advanced_writer(file_name):
        def write_everything(*data_set):
                with open(file_name, 'w', encoding='utf8') as file:
                        for i in data_set:
                                file.write(f'{str(i)}\n')

        return  write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
#-----------------------------------

import random

class MysticBall:
        def __init__(self, *spisok):
                self.spisok = spisok
        def choice(self):
                return random.choice(self.spisok)
        def __call__(self):
                return random.choice(self.spisok)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())

#print("random.choice используется для выбора случайного элемента из списка - ", random.choice(lst2))
# 1 шаг
x = 8
print('hello')
if x < 0:
    print('меньше нуля')
print('Good bye')

# примеры

a, b = 10, 5

if a > b:
    print('a  > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000 ):
    print('успех')

if 5 < b and b < 10:
    print('успех')

# можно сравнивать и числа и строки и вообще ...

if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')

# нельзя сравнивать

if '6' >  5:
    print('успех')
if [5, 6] > 5:
    print('успех')
if '6' != 5:
    print('успех')

if '6' != 5:
    print('успех')

    print('успех')

# Дописал комментарий для гита
# test



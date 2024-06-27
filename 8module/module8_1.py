def add_everything_up(a,b):
    buffer = ''
    try:
        result = a + b
    except TypeError as err:
        if type(a) != str:
            a = str(a)
        if type(b) != str:
            b = str(b)
        result = a + b
        buffer = err
    else:
        buffer = ' '
    finally:

        result= (f' результат cложения двух переменных: {result}')
        if buffer == ' ':
            ret = result + (f'\n    операция сложения завершена корректно')
        else:
            ret = result + (f'\n    завершено корректно, но была обработана ошибка {buffer}:')
        return ret

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


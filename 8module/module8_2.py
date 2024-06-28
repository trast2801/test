class InvalidDataException (Exception):
    def __init__(self, message) :
        self.message = message


class ProcessingException (Exception):
    def __init__(self, message) :
        self.message = message


def slojenie(a, b):

    if (type(a) and type(b)) == str:
        raise ProcessingException('мы здесь цифры складываем, а не строки')

    if (type(a) or type(b)) != int:
        raise  InvalidDataException('Ждем int')

    return a + b

try:
    itog = slojenie('2', '2')
    err = None
except InvalidDataException as error:
    print (f'не корректный ввод, {error.message} ')
    err = 1
except ProcessingException as error:
    print(f'не корректный ввод, {error.message} ')
    err = 2
finally:
    if err == None:
        print('Завершено корректно ')
    else:
        print('Корректно отработаны ошибки.')


import inspect
import types


class Сhe_nitь:
    def __init__(self, чё = 12): #использование русских букв в названии- просто почувствовать
                                 # как пишется на языке носителя.
        self.чё = чё

    def conter(self, сколько):
        for i in range(сколько):
            print(f' {i} счетчик \n')


    def getname(self):
        for i, j in globals().items():
            if j is self:
                return i

def introspection_info(obj):
    dict ={}
    dict['тип обьекта'] = type (obj)
    #dict['аттрибуты объекта'] = dir(obj)
    metod = []
    attr = []
    method_list = []
    for attribute in dir(obj):
        attribute_value = getattr(obj, attribute)
        if callable(attribute_value):
            metod.append(attribute)
        else:
            attr.append(attribute_value)
    dict['Атрибуты'] = attr
    dict['Методы'] = metod
    dict['Модуль'] = inspect.getmodule(obj)
    return dict

что = Сhe_nitь()

dd = (introspection_info(что))

for i in dd.items():
    print(f'{i} - тип {type(i)}')


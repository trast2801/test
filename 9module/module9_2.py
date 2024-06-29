class Dibyzero (Exception):
    def __init__(self, message) :
        self.message = message
def create_operation(operation):
    if operation == "div":
        def div(x, y):
            if y == 0:
                raise Dibyzero ('Error: division by zero')
            return x / y
        return div
    elif operation == "mul":
        def mul(x, y):
            return x * y
        return mul
    elif operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "sub":
        def sub(x, y):
            return x - y
        return sub

try:
    err=None
    my_func_add = create_operation("div")
    print(f'Деление {my_func_add(1,0)}')
except Dibyzero as error:
    print(error)
    err = 1
finally:
    if err == None:
        pass
    my_func_add = create_operation("mul")
    print(f'Умножение {my_func_add(2, 3)}')

squaring = lambda x: x ** 2
print(f'лямбда  {squaring(2)}')
def squaring(x):
    return x ** 2
print(f'Функция {squaring(2)}')

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):

        return 'Стороны: '+ str(self.a) + str(self.b) + '\n' + 'Площадь: '+ str(self.a * self.b)

rectangle = Rect(2,4)
print(rectangle.__call__())





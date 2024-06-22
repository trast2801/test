

class Vehicle:


    def __init__(self, owner: str, __model: str,  __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        return ' Модель: ' + str(self.__model) + '\n'

    def get_horsepower(self):
        return 'Мощность двигателя: ' + str(self.__engine_power) + '\n'

    def get_color(self):
        return 'Цвет: ' + str(self.__color) + '\n'

    def print_info(self):
        print(self.get_model(),
              self.get_horsepower(),
              self.get_color(),
              'Владелец: ', self.owner )

    def set_color(self, new_color: str):
        for i in self.__COLOR_VARIANTS:
            if i.lower() == new_color.lower():
                self.__color = new_color
                return
        print(f' Нельзя сменить цвет на {new_color}.')





class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors

floor = 0

building = House()

while floor != '-1':
    print(f'Сейчас вы на {building.numberOfFloors} этаже')
    floor = input("Введите номер этажа, или -1 для выхода: ")
    if floor != '-1':
        building.numberOfFloors = floor
        print(f'Вы переместились на {building.numberOfFloors} этаж')

print(f'Вы вышли с {building.numberOfFloors} этажа')
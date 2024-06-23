class Vehicle:
    def __init__(self, vehicle_type = None):
        self.vehicle_type = vehicle_type

class Car(Vehicle):

    def __init__(self, price: object = 1000000, horse_power: object = 100) -> object:
        super().__init__()
        self.horse_power = horse_power
        self.price = price


    def horse_powers(self):

        return self.horse_powers

class Nissan(Car):
        def __init__(self):
            super().__init__()
            self.vehicle_type = 'Дизель'
            self.price = 2000000
            self.horse_power = 300
            super().horse_powers()

        def horse_powers(self):
            return self.horse_power


nissan = Nissan()
print(Nissan.mro())
print (nissan.vehicle_type, nissan.price, nissan.horse_powers())


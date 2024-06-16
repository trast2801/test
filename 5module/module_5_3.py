class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):

        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

bulding_one = Building(5, 'кирпич')
bulding_two = Building(5, 'кирпич')

print(bulding_one == bulding_two)

bulding_one = Building(6, 'кирпич')
bulding_two = Building(5, 'газоблок')

print(bulding_one == bulding_two)

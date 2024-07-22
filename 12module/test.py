import module12_2
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = module12_2.Runner('Усэйн', 10)
        self.runer_2 = module12_2.Runner('Андрей', 9)
        self.runer_3 = module12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key1, value1 in cls.all_results.items():
            for key, value in value1.items():
                #print(value1.items[key])
                print(f'{key}: {value.name}', end=' ', flush=True)
            print()

    def test_turn1(self):
        # test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #         [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = module12_2.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    def test_turn2(self):
        turn_2 = module12_2.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_turn3(self):
        turn_3 = module12_2.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

if __name__ == "__main__":

    unittest(module12_2)



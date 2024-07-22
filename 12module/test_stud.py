import unittest
import main


class Test_Student(unittest.TestCase):
    is_frozen = False
    def setUp(self):
        self.student  = main.Student('First')
        self.student1 = main.Student('Second')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for i in range(10):
            self.student.walk()
        self.assertEqual(self.student.distance,500,
                         f'\nДистанции не равны {self.student.distance} != 500')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.student.distance = 0
        for i in range(10):
            self.student.run()
        self.assertEqual(self.student.distance, 1000,
                         f'\nДистанции не равны {self.student.distance} != 1000')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_gonka(self):
        for _ in range(10):
            self.student1.run()
            self.student.walk()
        self.assertGreater(self.student1.distance, self.student.distance,
                           msg=f"{self.student1.distance} Бегущий должен преодолеть дистанцию больше,"
                               f" чем идущий {self.student.distance}")
import unittest
import test_stud
import test_tour

global_Test = unittest.TestSuite()

global_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_stud.Test_Student))
global_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tour.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(global_Test)



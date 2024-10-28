import unittest
import tests_12_1
import tests_12_2

marafon = unittest.TestSuite()
marafon.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
marafon.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(marafon)

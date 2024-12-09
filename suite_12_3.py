import unittest
import tests_12_3 #RunnerTest #TournamentTest


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(tests_12_3.RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(tests_12_3.TournamentTest))
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests(unittest.TestLoader(), None, None))

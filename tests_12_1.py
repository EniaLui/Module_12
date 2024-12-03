import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_name = Runner("RunnerName")
        for i in range (10):
            test_name.walk()
        self.assertEqual(test_name.distance, 50)

    def test_run(self):
        test_name2 = Runner("RunnerName")
        for i in range(10):
            test_name2.run()
        self.assertEqual(test_name2.distance, 100)

    def test_challenge(self):
        test_runner1 = Runner("RunnerName1")
        test_runner2 = Runner("RunnerName2")

        for i in range(10):
            test_runner1.run()
            test_runner2.walk()

        self.assertNotEqual(test_runner1.distance, test_runner2.distance)

if __name__ == '__main__':
    unittest.main()
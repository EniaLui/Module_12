import unittest
from runner2 import Runner, Tournament

def freeze_check(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_check
    def test_walk(self):
        test_name = Runner("RunnerName")
        for i in range (10):
            test_name.walk()
        self.assertEqual(test_name.distance, 50)

    @freeze_check
    def test_run(self):
        test_name2 = Runner("RunnerName")
        for i in range(10):
            test_name2.run()
        self.assertEqual(test_name2.distance, 100)

    @freeze_check
    def test_challenge(self):
        test_runner1 = Runner("RunnerName1")
        test_runner2 = Runner("RunnerName2")

        for i in range(10):
            test_runner1.run()
            test_runner2.walk()

        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


    class TournamentTest(unittest.TestCase):
        is_frozen = True

        @classmethod
        def setUpClass(cls):
            cls.all_results = {}

        def setUp(self):
            self.runner_usain = Runner("Усэйн", speed=10)
            self.runner_andrei = Runner("Андрей", speed=9)
            self.runner_nik = Runner("Ник", speed=3)

        @freeze_check
        def test_usain_and_nik(self):
            tournament = Tournament(90, self.runner_usain, self.runner_nik)
            result = tournament.start()
            TournamentTest.all_results["test_usain_and_nik"] = result
            self.assertTrue(result[max(result.keys())] == "Ник")

        @freeze_check
        def test_andrei_and_nik(self):
            tournament = Tournament(90, self.runner_andrei, self.runner_nik)
            result = tournament.start()
            TournamentTest.all_results["test_andrei_and_nik"] = result
            self.assertTrue(result[max(result.keys())] == "Ник")

        @freeze_check
        def test_usain_andrei_nik(self):
            tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
            result = tournament.start()
            TournamentTest.all_results["test_usain_andrei_nik"] = result
            self.assertTrue(result[max(result.keys())] == "Ник")

        @classmethod
        def tearDownClass(cls):
            for key, result in cls.all_results.items():
                print(f"{result}")



if __name__ == "__main__":
        unittest.main()

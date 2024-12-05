import unittest
from runner2 import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nik = Runner("Ник", speed=3)

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_usain_and_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_andrei_and_nik(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_andrei_and_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_usain_andrei_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_usain_andrei_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")


if __name__ == "__main__":
    unittest.main()

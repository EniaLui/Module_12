import unittest
import logging
from runner_12_4 import Runner

logging.basicConfig(
    # 1. Уровень - INFO.
    level=logging.INFO,
    # 2. Режим - запись с заменой
    filemode="w",
    # 3. Название файла - runner_tests.log
    filename='runner_tests.log',
    # 4. Кодировка - UTF-8
    encoding='utf-8',
    # 5. Формат вывода
    format='%(asctime)s | %(levelname)s | %(message)s'
)


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
        try:
            runner = Runner("TestRunner", -4)  #отрицательное число
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')
            self.fail(f'Test failed due to exception: {e}')

    @freeze_check

    def test_run(self):
        try:
            runner = Runner(1111, 5)  # Некорректное имя
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')
            self.fail(f'Test failed due to exception: {e}')

    @freeze_check
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.assertEqual(runner1.distance, 100)
        self.assertEqual(runner2.distance, 50)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
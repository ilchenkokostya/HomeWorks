import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


#####################################################


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("Kosta")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        print('Test_walk Ok')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Kosta')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
        print('Test_run OK')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('Kosta')
        runner_2 = Runner('Roman')
        for i in range(20):
            if i % 2 == 0:
                runner_1.run()
            else:
                runner_2.walk()
            self.assertNotEqual(runner_1.distance, runner_2.distance)
        print('Test_challenge OK')


if __name__ == '__main__':
    unittest.main()

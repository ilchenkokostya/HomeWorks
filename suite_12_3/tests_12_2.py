import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        # return self.name
        return f'{self.name} пробежал {self.distance}'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


#####################################################


class TournamentTest(unittest.TestCase):
    DISTANCE = 90
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = {
            'Usain': Runner("Усейн", 10),
            'Andrey': Runner("Андрей", 4),
            'Nick': Runner("Ник", 3),
        }

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}:')
            for place, runner_name in value.items():
                print(f'{place}: {runner_name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_a_usain_and_nick(self):
        turn = Tournament(self.DISTANCE, self.runners['Usain'], self.runners['Nick'])
        result = turn.start()
        self.assertTrue(result[sorted(result)[-1]] == "Ник")
        self.all_results["Результат Усейна и Ника"] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_b_andrey_and_nick(self):
        turn = Tournament(self.DISTANCE, self.runners['Andrey'], self.runners['Nick'])
        result = turn.start()
        self.assertTrue(result[sorted(result)[-1]] == "Ник")
        self.all_results["Результат Андрея и Ника"] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_c_all_participants(self):
        turn = Tournament(self.DISTANCE, *self.runners.values())
        result = turn.start()
        self.assertTrue(result[sorted(result)[-1]] == "Ник")
        self.all_results["Результат общего забега"] = result

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # def test_d_nick_andrey(self):
    #     """Ситуация когда Ник начинает бежать первым и побеждает!!!"""
    #     turn = Tournament(12, self.runners['Nick'], self.runners['Andrey'])
    #     result = turn.start()
    #     self.assertTrue(result[sorted(result)[-1]] == "Ник")
    #     self.all_results["Результат когда Ник побеждает"] = result
    #
    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # def test_e_identical_participants(self):
    #     """Ситуация когда участник бежит сам собой"""
    #     turn = Tournament(self.DISTANCE, self.runners['Nick'], self.runners['Nick'])
    #     result = turn.start()
    #     self.assertNotEqual(result[1].name, result[2].name, True)


if __name__ == '__main__':
    unittest.main()

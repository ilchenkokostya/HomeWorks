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

    def test_a_usain_and_nick(self):
        # turn_1 = Tournament(self.DISTANCE, self.runners['Usain'], self.runners['Nick'])
        turn_1 = Tournament(self.DISTANCE, self.runners['Nick'], self.runners['Usain'])
        result = turn_1.start()
        self.assertTrue(result[sorted(result)[-1]] == "Ник")
        self.all_results["Результат Усейна и Ника"] = result

    def test_b_andrey_and_nick(self):
        turn_2 = Tournament(90, self.runners['Andrey'], self.runners['Nick'])
        result = turn_2.start()
        self.assertTrue(result[sorted(result)[-1]] == "Ник")
        self.all_results["Результат Андрея и Ника"] = result

    def test_c_all_participants(self):
        turn_3 = Tournament(self.DISTANCE, *self.runners.values())
        result = turn_3.start()
        self.assertTrue(result[sorted(result)[-1]] == "Ник")
        self.all_results["Результат общего забега"] = result

    def test_d_difference_participants(self):
        self.assertNotEqual(self.runners['Andrey'].name, self.runners['Nick'].name, True)


if __name__ == '__main__':
    unittest.main()

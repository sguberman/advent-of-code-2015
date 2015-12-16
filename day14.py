import unittest
from collections import namedtuple


class TestExampleRace(unittest.TestCase):

    def test_example_result(self):
        self.assertEqual(race('day14.test', 1000), 1120)
        self.assertEqual(race('day14.test', 1), 16)
        self.assertEqual(race('day14.test', 10), 160)
        self.assertEqual(race('day14.test', 11), 176)
        self.assertEqual(race('day14.test', 12), 176)


Reindeer = namedtuple('Reindeer', 'name speed stamina rest')


def race(reindeer_file, seconds=1000):
    reindeer = get_reindeer_stats(reindeer_file)
    return max(compute_distance(r, seconds) for r in reindeer)


def get_reindeer_stats(reindeer_file):
    return [parse_reindeer(line) for line in open(reindeer_file, 'r')]


def parse_reindeer(line):
    line = line.split()
    name = line[0]
    speed = int(line[3])
    stamina = int(line[6])
    rest = int(line[-2])
    return Reindeer(name, speed, stamina, rest)


def compute_distance(reindeer, time):
    q, r = divmod(time, reindeer.stamina + reindeer.rest)
    return (q * reindeer.stamina + min(r, reindeer.stamina)) * reindeer.speed


if __name__ == '__main__':
    # unittest.main()
    print race('day14.input', 2503)

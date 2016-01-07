import unittest
from itertools import zip_longest


class TestDeliveries(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(deliver('>'), 2)
        self.assertEqual(deliver('^>v<'), 4)
        self.assertEqual(deliver('^v^v^v^v^v'), 2)


class TestTeamDeliveries(unittest.TestCase):

    def setUp(self):
        self.team = Team((0, 0), (0, 0))

    def test_example_1(self):
        self.assertEqual(self.team.deliver('^v'), 3)
        self.assertEqual(self.team.position()[0], [0, 1])
        self.assertEqual(self.team.position()[1], [0, -1])

    def test_example_2(self):
        self.assertEqual(self.team.deliver('^>v<'), 3)
        self.assertEqual(self.team.position()[0], [0, 0])
        self.assertEqual(self.team.position()[1], [0, 0])

    def test_example_3(self):
        self.assertEqual(self.team.deliver('^v^v^v^v^v'), 11)
        self.assertEqual(self.team.position()[0], [0, 5])
        self.assertEqual(self.team.position()[1], [0, -5])


class TestSanta(unittest.TestCase):

    def test_create_santa(self):
        s = Santa()
        self.assertEqual(s.position, [0, 0])
        self.assertEqual(s.history, [(0, 0)])

    def test_move_santa(self):
        s = Santa()
        s.move('^')
        self.assertEqual(s.position, [0, 1])
        self.assertEqual(s.history, [(0, 0), (0, 1)])


class Santa(object):
    def __init__(self, start=(0, 0)):
        self.position = list(start)
        self.history = [start]

    def move(self, direction):
        if direction == '^':
            self.position[1] += 1
        elif direction == 'v':
            self.position[1] -= 1
        elif direction == '>':
            self.position[0] += 1
        elif direction == '<':
            self.position[0] -= 1
        self.history.append(tuple(self.position))


class Team(object):
    def __init__(self, *args):
        self.members = [Santa(arg) for arg in args]

    def position(self):
        return [m.position for m in self.members]

    def update(self, sequence):
        for step, member in zip(sequence, self.members):
            member.move(step)

    def deliver(self, directions):
        for sequence in grouper(directions, len(self.members), 'x'):
            self.update(sequence)
        return len(set(pos for mem in self.members for pos in mem.history))


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def deliver(directions):
    x, y = 0, 0
    deliveries = [(x, y)]
    for move in directions:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        deliveries.append((x, y))
    no_repeats = set(deliveries)
    return len(no_repeats)


def test():
    unittest.main()


def part1():
    print(deliver(open('day03.input', 'r').read()))


def part2():
    team = Team((0, 0), (0, 0))
    print(team.deliver(open('day03.input', 'r').read()))


if __name__ == '__main__':
    part1()
    part2()

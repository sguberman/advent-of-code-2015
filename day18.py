import unittest
from collections import defaultdict


class TestLightGrid(unittest.TestCase):

    def setUp(self):
        self.mylights = LightGrid(lightfile='day18.test')
        stuck = ((0, 0), (0, 5), (5, 0), (5, 5))
        self.mystucklights = LightGrid(lightfile='day18.test', stuck_on=stuck)

    def test_initial_state(self):
        self.assertEqual(self.mylights.total(), 15)
        self.assertEqual(self.mystucklights.total(), 17)

    def test_one_step(self):
        self.mylights.step()
        self.mystucklights.step()
        self.assertEqual(self.mylights.total(), 11)
        self.assertEqual(self.mystucklights.total(), 18)

    def test_two_steps(self):
        self.mylights.step(2)
        self.mystucklights.step(2)
        self.assertEqual(self.mylights.total(), 8)
        self.assertEqual(self.mystucklights.total(), 18)

    def test_three_steps(self):
        self.mylights.step(3)
        self.mystucklights.step(3)
        self.assertEqual(self.mylights.total(), 4)
        self.assertEqual(self.mystucklights.total(), 18)

    def test_four_steps(self):
        self.mylights.step(4)
        self.mystucklights.step(4)
        self.assertEqual(self.mylights.total(), 4)
        self.assertEqual(self.mystucklights.total(), 14)

    def test_five_steps(self):
        self.mystucklights.step(5)
        self.assertEqual(self.mystucklights.total(), 17)


class LightGrid(object):

    def __init__(self, lightfile=None, lightdict=None, stuck_on=None):
        if lightfile:
            with open(lightfile, 'r') as lf:
                grid = defaultdict(bool)
                for y, line in enumerate(lf):
                    for x, point in enumerate(line.strip()):
                        grid[(x, y)] = True if point == '#' else False
            lightdict = grid
        if not lightdict:
            lightdict = defaultdict(bool)
        self.lights = lightdict
        self.stuck_on = stuck_on
        self.restick()

    def restick(self):
        if self.stuck_on:
            for stuck in self.stuck_on:
                self.lights[stuck] = True

    def adjacent_lit(self, x, y):
        adj_coords = ((x + i, y + j) for i in (-1, 0, 1)
                      for j in (-1, 0, 1) if not (i == j == 0))
        return sum(self.lights[coord] for coord in adj_coords)

    def total(self):
        return sum(self.lights.values())

    def step(self, n=1):
        for _ in range(n):
            nextgrid = defaultdict(bool)
            for coord, on in list(self.lights.items()):
                num_neighbors = self.adjacent_lit(*coord)
                if on:
                    if num_neighbors in (2, 3):
                        status = True
                    else:
                        status = False
                else:
                    if num_neighbors == 3:
                        status = True
                    else:
                        status = False
                nextgrid[coord] = status
            self.lights = nextgrid
            self.restick()


if __name__ == '__main__':
    # unittest.main()
    stuck = ((0, 0), (0, 99), (99, 0), (99, 99))
    mylights = LightGrid(lightfile='day18.input', stuck_on=stuck)
    mylights.step(100)
    print(mylights.total())

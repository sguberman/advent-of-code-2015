import unittest
from collections import defaultdict


class TestLightGrid(unittest.TestCase):

    def setUp(self):
        self.mylights = LightGrid(lightfile='day18.test')

    def test_initial_state(self):
        self.assertEqual(self.mylights.total(), 15)

    def test_one_step(self):
        self.mylights.step()
        self.assertEqual(self.mylights.total(), 11)

    def test_two_steps(self):
        self.mylights.step(2)
        self.assertEqual(self.mylights.total(), 8)

    def test_three_steps(self):
        self.mylights.step(3)
        self.assertEqual(self.mylights.total(), 4)

    def test_four_steps(self):
        self.mylights.step(4)
        self.assertEqual(self.mylights.total(), 4)


class LightGrid(object):

    def __init__(self, lightfile=None, lightdict=None):
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

    def adjacent_lit(self, x, y):
        adj_coords = ((x + i, y + j) for i in (-1, 0, 1)
                      for j in (-1, 0, 1) if not (i == j == 0))
        return sum(self.lights[coord] for coord in adj_coords)

    def total(self):
        return sum(self.lights.itervalues())

    def step(self, n=1):
        for _ in range(n):
            nextgrid = defaultdict(bool)
            for coord, on in self.lights.items():
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


if __name__ == '__main__':
    # unittest.main()
    mylights = LightGrid(lightfile='day18.input')
    mylights.step(100)
    print mylights.total()

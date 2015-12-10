import unittest
import itertools


class TestWrappingPaper(unittest.TestCase):

    def test_min_paper(self):
        self.assertEqual(min_paper('2x3x4'), 58)
        self.assertEqual(min_paper('1x1x10'), 43)


class TestRibbon(unittest.TestCase):

    def test_min_perimeter(self):
        self.assertEqual(min_perimeter('2x3x4'), 10)
        self.assertEqual(min_perimeter('1x1x10'), 4)

    def test_volume(self):
        self.assertEqual(volume('2x3x4'), 24)
        self.assertEqual(volume('1x1x10'), 10)

    def test_min_ribbon(self):
        self.assertEqual(min_ribbon('2x3x4'), 34)
        self.assertEqual(min_ribbon('1x1x10'), 14)


def lwh(dimensions):
    return (int(d) for d in dimensions.split('x'))


def min_paper(dimensions):
    l, w, h = lwh(dimensions)
    sides = (l*w, w*h, h*l)
    extra = min(sides)
    total = 2*sum(sides) + extra
    return total


def total_paper(boxes):
    return sum(min_paper(box) for box in boxes)


def min_perimeter(dimensions):
    return 2 * min(map(sum, itertools.combinations(lwh(dimensions), 2)))


def volume(dimensions):
    l, w, h = lwh(dimensions)
    return l * w * h


def min_ribbon(dimensions):
    return min_perimeter(dimensions) + volume(dimensions)


def total_ribbon(boxes):
    return sum(min_ribbon(box) for box in boxes)


if __name__ == '__main__':
    # unittest.main()
    print total_ribbon(open('day02.input', 'r').readlines())

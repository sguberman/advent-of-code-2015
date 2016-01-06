import unittest


class TestFinalFloor(unittest.TestCase):

    known_pairs = {'(())': 0,
                   '()()': 0,
                   '(((': 3,
                   '(()(()(': 3,
                   '))(((((': 3,
                   '())': -1,
                   '))(': -1,
                   ')))': -3,
                   ')())())': -3,
                   }

    def test_known(self):
        for k, v in self.known_pairs.items():
            self.assertEqual(final_floor(k), v)


class TestEnteringBasement(unittest.TestCase):

    def test_enter_basement(self):
        self.assertEqual(enter_basement(')'), 1)
        self.assertEqual(enter_basement('()())'), 5)


def final_floor(sequence):
    floor = 0
    for step in sequence:
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
    return floor


def enter_basement(sequence):
    floor = 0
    position = 0
    while floor != -1:
        if sequence[position] == '(':
            floor += 1
        elif sequence[position] == ')':
            floor -= 1
        position += 1
    return position


if __name__ == '__main__':
    unittest.main()
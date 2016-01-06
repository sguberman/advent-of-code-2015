import unittest


class TestExamples(unittest.TestCase):

    def test_say_once(self):
        self.assertEqual(say('1'), '11')
        self.assertEqual(say('11'), '21')
        self.assertEqual(say('21'), '1211')
        self.assertEqual(say('1211'), '111221')
        self.assertEqual(say('111221'), '312211')

    def test_say_n_times(self):
        self.assertEqual(say_n_times('1', n=5), '312211')


def say(sequence):
    previous = sequence[0]
    count = 1
    result = ''
    for num in sequence[1:]:
        if num == previous:
            count += 1
        else:
            result += str(count) + previous
            previous = num
            count = 1
    result += str(count) + previous
    return result


def say_n_times(sequence, n=1):
    previous = sequence
    for time in range(n):
        previous = say(previous)
    return previous


def part1():
    return len(say_n_times('1321131112', n=40))


def part2():
    return len(say_n_times('1321131112', n=50))


def test():
    unittest.main()


if __name__ == '__main__':
    # test()
    print(part1())
    print(part2())
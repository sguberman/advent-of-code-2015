import unittest
import string
import re


class TestRequirements(unittest.TestCase):

    def test_has_straight(self):
        self.assertTrue(has_straight('abc'))
        self.assertTrue(has_straight('bcd'))
        self.assertTrue(has_straight('cde'))
        self.assertTrue(has_straight('xyz'))
        self.assertFalse(has_straight('abd'))
        self.assertTrue(has_straight('hijklmmn'))
        self.assertFalse(has_straight('abbceffg'))
        self.assertFalse(has_straight('abbcegjk'))
        self.assertTrue(has_straight('abcdefgh'))
        self.assertTrue(has_straight('abcdffaa'))
        self.assertTrue(has_straight('ghijklmn'))
        self.assertTrue(has_straight('ghjaabcc'))

    def test_no_badchars(self):
        self.assertFalse(no_badchars('iol'))
        self.assertFalse(no_badchars('hijklmmn'))
        self.assertTrue(no_badchars('abbceffg'))
        self.assertFalse(no_badchars('ghijklmn'))
        self.assertTrue(no_badchars('ghjaabcc'))

    def test_has_two_pairs(self):
        self.assertTrue(has_two_pairs('aabb'))
        self.assertFalse(has_two_pairs('aabc'))
        self.assertFalse(has_two_pairs('hijklmmn'))
        self.assertTrue(has_two_pairs('abbceffg'))
        self.assertFalse(has_two_pairs('abbcegjk'))
        self.assertTrue(has_two_pairs('abcdffaa'))
        self.assertTrue(has_two_pairs('ghjaabcc'))
        self.assertFalse(has_two_pairs('aabaa'))


class TestValidation(unittest.TestCase):

    def test_is_valid(self):
        self.assertTrue(is_valid('abcdffaa'))
        self.assertTrue(is_valid('ghjaabcc'))
        self.assertFalse(is_valid('abcdefgh'))
        self.assertFalse(is_valid('ghijklmn'))
        self.assertFalse(is_valid('hijklmmn'))
        self.assertFalse(is_valid('abbceffg'))
        self.assertFalse(is_valid('abbcegjk'))
        self.assertFalse(is_valid('aa'))
        self.assertFalse(is_valid('ABCDFFAA'))

    def test_next_valid(self):
        self.assertEqual(next_valid('abcdezzz'), 'abcdffaa')
        self.assertEqual(next_valid('ghijklmn'), 'ghjaabcc')


class TestIncrementation(unittest.TestCase):

    def test_increment(self):
        self.assertEqual(increment('xx'), 'xy')
        self.assertEqual(increment('xy'), 'xz')
        self.assertEqual(increment('xz'), 'ya')
        self.assertEqual(increment('ya'), 'yb')
        self.assertEqual(increment('abcdezzz'), 'abcdfaaa')


def test():
    unittest.main()


def part1():
    return next_valid('vzbxkghb')


def part2():
    return next_valid(part1())


def increment(word):
    wrapped = True
    nextword = []
    for x in reversed(word):
        if wrapped:
            if x == 'z':
                nextchr = 'a'
            else:
                nextchr = chr(ord(x) + 1)
                wrapped = False
        else:
            nextchr = x
            wrapped = False
        nextword.append(nextchr)
    return ''.join(reversed(nextword))


def has_straight(word):
    abc = string.ascii_lowercase
    straights = zip(abc, abc[1:], abc[2:])
    return any(''.join(s) in word for s in straights)


def no_badchars(word, bad='iol'):
    return not any(x in word for x in bad)


def has_two_pairs(word):
    return len(set(re.findall(r'(.)\1', word))) >= 2


def is_valid(word):
    requirements = (has_straight, no_badchars, has_two_pairs)
    return all(req(word) for req in requirements)


def next_valid(password):
    password = increment(password)
    while not is_valid(password):
        password = increment(password)
    return password


if __name__ == '__main__':
    print(part2())

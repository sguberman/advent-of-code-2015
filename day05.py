import unittest
import re


class TestNaughtyOrNice(unittest.TestCase):

    def test_has_three_vowels(self):
        self.assertTrue(has_three_vowels('aei'))
        self.assertTrue(has_three_vowels('xazegov'))
        self.assertTrue(has_three_vowels('aeiouaeiouaeiou'))

        self.assertFalse(has_three_vowels('dvszwmarrgswjxmb'))

    def test_has_double_letter(self):
        self.assertTrue(has_double_letter('xx'))
        self.assertTrue(has_double_letter('abcdde'))
        self.assertTrue(has_double_letter('aabbccdd'))

        self.assertFalse(has_double_letter('jchzalrnumimnmhp'))

    def test_no_bad_string(self):
        self.assertFalse(no_bad_string('haegwjzuvuyypxyu'))

        self.assertTrue(no_bad_string('ugknbfddgicrmopn'))

    def test_examples(self):
        self.assertTrue(is_nice('ugknbfddgicrmopn'))
        self.assertTrue(is_nice('aaa'))

        self.assertFalse(is_nice('jchzalrnumimnmhp'))
        self.assertFalse(is_nice('haegwjzuvuyypxyu'))
        self.assertFalse(is_nice('dvszwmarrgswjxmb'))

    def test_rule1(self):
        self.assertTrue(rule1('xyxy'))
        self.assertTrue(rule1('aabcdefgaa'))
        self.assertFalse(rule1('aaa'))
        self.assertTrue(rule1('xxyxx'))
        self.assertTrue(rule1('qjhvhtzxzqqjkmpb'))
        self.assertTrue(rule1('uurcxstgmygtbstg'))

    def test_rule2(self):
        self.assertTrue(rule2('xyx'))
        self.assertTrue(rule2('abcdefeghi'))
        self.assertTrue(rule2('aaa'))
        self.assertTrue(rule2('xxyxx'))
        self.assertTrue(rule2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(rule2('ieodomkazucvgmuy'))

    def test_examples2(self):
        self.assertTrue(is_nice2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(is_nice2('xxyxx'))
        self.assertFalse(is_nice2('uurcxstgmygtbstg'))
        self.assertFalse(is_nice2('ieodomkazucvgmuy'))


def has_three_vowels(word):
    vowels = 'aeiou'
    return sum(letter in vowels for letter in word) >= 3


def has_double_letter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False


def no_bad_string(word):
    disallowed = 'ab cd pq xy'.split()
    return not any(sub in word for sub in disallowed)


def is_nice(word):
    criteria = (has_three_vowels, has_double_letter, no_bad_string)
    return all(check(word) for check in criteria)


def chunk(word, start, step):
    n = step
    return [word[i:i+n] for i in range(start, len(word), n)]


def rule1(word):
    prog = re.compile(r'(..).*\1')
    result = prog.search(word)
    return result


def rule2(word):
    prog = re.compile(r'(.).\1')
    result = prog.search(word)
    return result


def is_nice2(word):
    criteria = (rule1, rule2)
    return all(check(word) for check in criteria)


def test():
    unittest.main()


def part1():
    print(sum(is_nice(word) for word in open('day05.input', 'r').readlines()))


def part2():
    print(sum(is_nice2(word) for word in open('day05.input', 'r').readlines()))


if __name__ == '__main__':
    # test()
    part1()
    part2()
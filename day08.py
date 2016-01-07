import unittest


class TestExamples(unittest.TestCase):

    lines = open('day08.test', 'r').readlines()

    def test_codelength(self):
        answers = (2, 5, 10, 6)
        for line, answer in zip(self.lines, answers):
            self.assertEqual(codelength(line.strip()), answer)

    def test_stringlength(self):
        answers = (0, 3, 7, 1)
        for line, answer in zip(self.lines, answers):
            self.assertEqual(stringlength(line.strip()), answer)

    def test_total_string_difference(self):
        self.assertEqual(total_string_difference(self.lines), 12)

    def test_encode_difference(self):
        answers = (4, 4, 6, 5)
        for line, answer in zip(self.lines, answers):
            self.assertEqual(encode_difference(line.strip()), answer)

    def test_total_encode_difference(self):
        self.assertEqual(total_encode_difference(self.lines), 19)


def stringlength(line):
    count = 0
    enclosing_quotes = 2
    backslash = "\\"
    escaped = False
    hexed = False
    for char in line:
        if not escaped:
            if char == backslash:
                escaped = True
            else:
                count += 1
        else:
            if hexed:
                hexed = False
                escaped = False
            elif char == 'x':
                hexed = True
            else:
                count += 1
                escaped = False
    return count - enclosing_quotes


def codelength(line):
    return len(line)


def encode_difference(line):
    enclosing_quotes = 2
    backslashes = line.count('\\')
    quotes = line.count('\"')
    return enclosing_quotes + backslashes + quotes


def total_string_difference(lines):
    total_codelength = sum(codelength(line.strip()) for line in lines)
    total_stringlength = sum(stringlength(line.strip()) for line in lines)
    return total_codelength - total_stringlength


def total_encode_difference(lines):
    return sum(encode_difference(line.strip()) for line in lines)


def part1():
    lines = open('day08.input', 'r').readlines()
    return total_string_difference(lines)


def part2():
    lines = open('day08.input', 'r').readlines()
    return total_encode_difference(lines)


def test():
    unittest.main()


if __name__ == '__main__':
    print(part1())
    print(part2())

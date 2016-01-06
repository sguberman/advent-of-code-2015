import unittest
import hashlib


class TestHashing(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(mine('abcdef'), 609043)
        self.assertEqual(mine('pqrstuv'), 1048970)


def mine(key, starts='00000'):
    i = 1
    while not hashlib.md5((key+str(i)).encode('utf-8')).hexdigest().startswith(starts):
        i += 1
    return i


def test():
    unittest.main()


def part1():
    print(mine('ckczppom'))


def part2():
    print(mine('ckczppom', '000000'))


if __name__ == '__main__':
    # test()
    part1()
    part2()

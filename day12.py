import unittest
import json


class TestJSONSum(unittest.TestCase):

    def test_json_sum(self):
        self.assertEqual(json_sum('[1,2,3]'), 6)
        self.assertEqual(json_sum('{"a":2,"b":4}'), 6)
        self.assertEqual(json_sum('{"a":{"b":4},"s":-1}'), 3)
        self.assertEqual(json_sum('[[[3]]]'), 3)
        self.assertEqual(json_sum('{"a":[-1,1]}'), 0)
        self.assertEqual(json_sum('[-1,{"a":1}]'), 0)
        self.assertEqual(json_sum('[]'), 0)
        self.assertEqual(json_sum('{}'), 0)


class TestFlatten(unittest.TestCase):

    def test_flatten_list(self):
        self.assertEqual(list(flatten([1, 2, 3])), [1, 2, 3])
        self.assertEqual(list(flatten([[[3]]])), [3])
        self.assertEqual(list(flatten([])), [])
        self.assertEqual(list(flatten([-1,  [1]])), [-1, 1])

    def test_flatten_dict(self):
        self.assertEqual(list(flatten({"a": 2, "b": 4})), [2, 4])
        self.assertEqual(list(flatten({"a": {"b": 4}, "C": -1})), [4, -1])
        self.assertEqual(list(flatten([-1, {"a": 1}])), [-1, 1])
        self.assertEqual(list(flatten({})), [])


def test():
    unittest.main()


def part1():
    return json_sum(open('day12.json', 'r').read())


def part2():
    return json_sum(open('day12.json', 'r').read(), ignore='red')


def json_sum(json_text, ignore=None):
    data = json.loads(json_text)
    return sum(item for item in flatten(data, ignore))


def flatten(data, ignore=None):
    if isinstance(data, dict):
        if ignore in data.values():
            data = {}
        data = data.values()
    for item in data:
        if isinstance(item, list):
            for subitem in flatten(item, ignore):
                yield subitem
        elif isinstance(item, dict):
            if ignore in item.values():
                item = {}
            for subitem in flatten(item.values(), ignore):
                yield subitem
        elif isinstance(item, int):
            yield item


if __name__ == '__main__':
    print part2()

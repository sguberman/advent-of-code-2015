import unittest
from collections import defaultdict
from itertools import permutations, tee, islice, chain, izip


class TestExample(unittest.TestCase):

    def test_optimal_happiness(self):
        self.assertEqual(optimal_happiness('day13.test'), 330)


def optimal_happiness(preference_filename):
    preferences = parse_preferences(preference_filename)
    tables = possible_tables(preferences)
    return max(tables, key=happiness)


def parse_preferences(preference_filename):
    preferences = defaultdict(dict)
    with open(preference_filename, 'r') as prefs:
        for line in prefs:
            line = line.strip().strip('.').split()
            name = line[0]
            score = int(line[3])
            if line[2] == 'lose':
                score = -1 * score
            neighbor = line[-1]
            preferences[name][neighbor] = score
    return preferences


def possible_tables(preferences):
    tables = [[{name: preferences[name]} for name in table]
              for table in permutations(preferences.keys(), len(preferences))]
    return tables


def happiness(table):
    happiness = 0
    for left, name, right in neighbors(table):
        happiness += name[left['name']] + name[right['name']]
    return happiness


def neighbors(names):
    prevs, items, nexts = tee(names, 3)
    prevs = chain([names[-1]], prevs)
    nexts = chain(islice(nexts, 1, None), [names[0]])
    return izip(prevs, items, nexts)


if __name__ == '__main__':
    unittest.main()

import unittest
from collections import defaultdict, namedtuple
from itertools import permutations, tee, islice, chain, izip


class TestExample(unittest.TestCase):

    def test_optimal_happiness(self):
        self.assertEqual(optimal_happiness('day13.test'), 330)


Person = namedtuple('Person', 'name preferences')


def optimal_happiness(preference_filename, *additional_guests):
    guests = parse_guests(preference_filename) + list(additional_guests)
    tables = possible_tables(guests)
    return happiness(max(tables, key=happiness))


def parse_guests(preference_filename):
    preferences = defaultdict(lambda : defaultdict(int))
    with open(preference_filename, 'r') as prefs:
        for line in prefs:
            line = line.strip().strip('.').split()
            name = line[0]
            score = int(line[3])
            if line[2] == 'lose':
                score = -1 * score
            neighbor = line[-1]
            preferences[name][neighbor] = score
    guests = [Person(name, prefs) for name, prefs in preferences.iteritems()]
    return guests


def possible_tables(guests):
    tables = permutations(guests, len(guests))
    return tables


def happiness(table):
    happiness = 0
    for onleft, guest, onright in neighbors(table):
        happiness += sum(guest.preferences[name] for name in (onleft.name, onright.name))
    return happiness


def neighbors(names):
    prevs, items, nexts = tee(names, 3)
    prevs = chain([names[-1]], prevs)
    nexts = chain(islice(nexts, 1, None), [names[0]])
    return izip(prevs, items, nexts)


if __name__ == '__main__':
    # unittest.main()
    part1 = optimal_happiness('day13.input')
    myself = Person('me', defaultdict(int))
    include_myself = optimal_happiness('day13.input', myself)
    part2 = include_myself - part1
    print part2

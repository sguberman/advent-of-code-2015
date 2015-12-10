import unittest
from collections import defaultdict
import itertools


class TestRoutes(unittest.TestCase):

    distance_data = ("London to Dublin = 464",
                     "London to Belfast = 518",
                     "Dublin to Belfast = 141",
                     )

    def test_shortest_route(self):
        self.assertEqual(shortest_route(self.distance_data), 605)

    def test_longest_route(self):
        self.assertEqual(shortest_route(self.distance_data, func=max), 982)


def shortest_route(distance_data, func=min):
    cities, distances = parse_data(distance_data)
    routes = itertools.permutations(cities)
    scores = {route: compute_distance(route, distances) for route in routes}
    return func(scores.values())


def compute_distance(route, distances):
    return sum(distances[city1][city2] for city1,city2 in zip(route,route[1:]))


def parse_data(distance_data):
    cities = set()
    distances = defaultdict(dict)
    for line in distance_data:
        left, right = line.split(' = ')
        city1, city2 = left.split(' to ')
        distance = int(right)
        cities.add(city1)
        cities.add(city2)
        distances[city1][city2] = distance
        distances[city2][city1] = distance
    return cities, distances


def test():
    unittest.main()


def part1():
    distance_data = (line.strip() for line in open('day09.input', 'r'))
    return shortest_route(distance_data)


def part2():
    distance_data = (line.strip() for line in open('day09.input', 'r'))
    return shortest_route(distance_data, func=max)


if __name__ == '__main__':
    # test()
    # print part1()
    print part2()

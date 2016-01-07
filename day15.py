import unittest
import itertools


class TestExampleRecipe(unittest.TestCase):

    ingredients = ((-1, -2, 6, 3, 8),
                   (2, 3, -2, -1, 3))

    mix = (44, 56)

    def test_best_recipe(self):
        self.assertEqual(best_recipe('day15.test'), 62842880)
        self.assertEqual(best_recipe('day15.test', calories=500), 57600000)

    def test_read_ingredients(self):
        self.assertEqual(read_ingredients('day15.test'), self.ingredients)

    def test_score(self):
        recipe = self.mix, self.ingredients
        self.assertEqual(score(recipe), 62842880)

    def test_possible_recipes(self):
        good_recipe = self.mix, self.ingredients
        self.assertIn(good_recipe, possible_recipes(self.ingredients))
        bad_recipe = (100, 100), self.ingredients
        self.assertNotIn(bad_recipe, possible_recipes(self.ingredients))


def score(recipe, calories=None):
    mix, ingredients = recipe
    properties = zip(*ingredients)
    cookie = []
    for prop in properties:
        propscore = 0
        for amt, ingr in zip(mix, prop):
            propscore += amt * ingr
        cookie.append(propscore)

    if any(prop < 0 for prop in cookie):
        return 0
    elif calories and cookie[-1] != calories:
        return 0
    else:
        score = 1
        for prop in cookie[:-1]:
            score *= prop
        return score


def best_recipe(ingredients_file, calories=None):
    ingredients = read_ingredients(ingredients_file)
    return max(score(recipe, calories) for recipe in possible_recipes(ingredients))


def read_ingredients(ingredients_file):
    ingredients = []
    with open(ingredients_file, 'r') as f:
        for line in f:
            name, stats = parse_ingredient(line)
            ingredients.append(stats)
    return tuple(ingredients)


def parse_ingredient(line):
    n, _, c, _, d, _, f, _, t, _, cal = line.split()
    name = n.strip(':').lower()
    stats = tuple(int(num.strip(',')) for num in (c, d, f, t, cal))
    return name, stats


def possible_recipes(ingredients):
    for mix in parts(100, len(ingredients)):
        yield mix, ingredients


def parts(n, length=None):
    mixtures = itertools.permutations(range(n + 1), length)
    for mix in mixtures:
        if sum(mix) == n:
            yield mix


if __name__ == '__main__':
    # unittest.main()
    # print best_recipe('day15.input')
    print(best_recipe('day15.input', calories=500))

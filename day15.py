import unittest


class TestExampleRecipe(unittest.TestCase):

    def test_recipe_score(self):
        recipe = {'butterscotch': 44, 'cinnamon': 56}
        self.assertEqual(recipe_score(recipe), 62842880)

    def test_best_recipe(self):
        self.assertEqual(best_recipe('day15.test'), 62842880)


def recipe_score(recipe):
    pass


def best_recipe(ingredients_file):
    pass


if __name__ == '__main__':
    unittest.main()

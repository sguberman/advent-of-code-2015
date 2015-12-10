import unittest


class TestLights(unittest.TestCase):

    def test_create_light(self):
        light = Light()
        self.assertFalse(light.on)

    def test_turn_on(self):
        light = Light()
        light.turn_on()
        self.assertTrue(light.on)

    def test_turn_off(self):
        light = Light()
        light.turn_on()
        light.turn_off()
        self.assertFalse(light.on)

    def test_toggle(self):
        light = Light()
        light.toggle()
        self.assertTrue(light.on)
        light.toggle()
        self.assertFalse(light.on)


class Light(object):
    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()


class Light2(object):
    def __init__(self, brightness=0):
        self.on = brightness

    def turn_on(self):
        self.on += 1

    def turn_off(self):
        if self.on > 1:
            self.on -= 1
        else:
            self.on = 0

    def toggle(self):
        self.on += 2


class LightGrid(object):
    def __init__(self, kind=Light, x=1000, y=1000):
        self.lights = [[kind() for i in range(x)] for j in range(y)]

    def do(self, command, corner1, corner2):
        for x in range(corner1[0], corner2[0]+1):
            for y in range(corner1[1], corner2[1]+1):
                light = self.lights[x][y]
                methodToCall = getattr(light, command)
                methodToCall()

    def total(self):
        return sum(light.on for row in self.lights for light in row)


def parse_corner(word):
    return tuple(int(x) for x in word.split(','))


def parse_command(line):
    words = line.split()
    if words[0] == 'toggle':
        command = 'toggle'
        corner1 = parse_corner(words[1])
    else:
        command = 'turn_'+words[1]
        corner1 = parse_corner(words[2])
    corner2 = parse_corner(words[-1])
    return command, corner1, corner2


def part1():
    mylights = LightGrid()
    for line in open('day06.input', 'r'):
        mylights.do(*parse_command(line))
    print mylights.total()


def part2():
    mylights = LightGrid(Light2)
    for line in open('day06.input', 'r'):
        mylights.do(*parse_command(line))
    print mylights.total()


def test():
    unittest.main()


if __name__ == '__main__':
    # test()
    # part1()
    part2()

import unittest
import struct


class TestSimpleCircuit(unittest.TestCase):

    def test_example(self):
        gates = ('123 -> x',
                 '456 -> y',
                 'x AND y -> d',
                 'x OR y -> e',
                 'x LSHIFT 2 -> f',
                 'y RSHIFT 2 -> g',
                 'NOT x -> h',
                 'NOT y -> i',
                 )

        answer = {'d': 72,
                  'e': 507,
                  'f': 492,
                  'g': 114,
                  'h': 65412,
                  'i': 65079,
                  'x': 123,
                  'y': 456,
                  }

        for wire, signal in answer.iteritems():
            self.assertEqual(probe_circuit(gates, wire), signal)


def sixteenify(number):
    return struct.unpack('HH', struct.pack('i', number))[0]


operators = {'AND': int.__and__,
             'OR': int.__or__,
             'LSHIFT': int.__lshift__,
             'RSHIFT': int.__rshift__,
             'NOT': int.__invert__,
             'SELF': lambda x: x,
             }


def probe_circuit(instructions, wire, known_wires=None):
    gates = read_gates(instructions)
    if not known_wires:
        known_wires = dict()
    while wire not in known_wires:
        print 'looping...'
        for gate in gates:
            print gate
            if gate['output'] not in known_wires:
                if all(inp in known_wires or
                       inp in operators or
                       inp.isdigit()
                       for inp in gate['inputs']):
                    signal = trace_signal(gate, known_wires)
                    known_wires[gate['output']] = signal
    return sixteenify(known_wires[wire])


def read_gates(instructions):
    gates = []
    for line in instructions:
        gate = dict()
        left, right = line.split(' -> ')
        gate['output'] = right
        gate['inputs'] = left.split()
        gates.append(gate)
    return gates


def trace_signal(gate, known_wires):
    inputs = gate['inputs']
    if len(inputs) == 3:
        arg1, op, arg2 = inputs
        args = (arg1, arg2)
    elif len(inputs) == 2:
        op, arg = inputs
        args = (arg, )
    elif len(inputs) == 1:
        args = tuple(inputs)
        op = 'SELF'
    args = [known_wires[a] if a in known_wires else int(a) for a in args]
    return operators[op](*args)


def test():
    unittest.main()


def part1():
    instructions = (line.strip() for line in open('day07.input', 'r'))
    print probe_circuit(instructions, 'a')


def part2():
    instructions = (line.strip() for line in open('day07.input', 'r'))
    override = {'b': 46065}
    print probe_circuit(instructions, 'a', known_wires=override)


if __name__ == '__main__':
    # test()
    # part1()
    part2()

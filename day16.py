def read_suefile(filename):
    with open(filename, 'r') as suefile:
        sues = []
        for line in suefile:
            lineitems = line.split()
            properties = lineitems[2:]
            compounds = (comp.strip(':') for comp in properties[0::2])
            quantities = (int(qty.strip(',')) for qty in properties[1::2])
            sues.append(dict(list(zip(compounds, quantities))))
    return sues


ticker = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1,
          }


def part1(sues):
    for i, sue in enumerate(sues):
        if all(v == ticker[k] for k, v in sue.items()):
            return i + 1


def part2(sues):
    for i, sue in enumerate(sues):
        conditions = [0] * len(sue)
        for j, (k, v) in enumerate(sue.items()):
            if k in ('cats', 'trees'):
                conditions[j] = v > ticker[k]
            elif k in ('pomeranians', 'goldfish'):
                conditions[j] = v < ticker[k]
            else:
                conditions[j] = v == ticker[k]
            if all(condition for condition in conditions):
                return i + 1

if __name__ == '__main__':
    sues = read_suefile('day16.input')
    print(part1(sues))
    print(part2(sues))

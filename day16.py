with open('day16.input', 'r') as suefile:
    sues = []
    for line in suefile:
        lineitems = line.split()
        properties = lineitems[2:]
        compounds = (comp.strip(':') for comp in properties[0::2])
        quantities = (int(qty.strip(',')) for qty in properties[1::2])
        sues.append(dict(zip(compounds, quantities)))

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

# Part 1
for i, sue in enumerate(sues):
    if all(v == ticker[k] for k, v in sue.iteritems()):
        print i + 1


# Part 2
for i, sue in enumerate(sues):
    conditions = [0] * len(sue)
    for j, (k, v) in enumerate(sue.iteritems()):
        if k in ('cats', 'trees'):
            conditions[j] = v > ticker[k]
        elif k in ('pomeranians', 'goldfish'):
            conditions[j] = v < ticker[k]
        else:
            conditions[j] = v == ticker[k]
        if all(condition for condition in conditions):
            print i + 1

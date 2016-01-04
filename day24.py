from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in xrange(len(s)+1))


packages = []
with open('day24.input', 'r') as f:
    for line in f:
        packages.append(int(line.strip()))

# test packages
packages = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11)


solutions = []
group1s = powerset(reversed(sorted(packages)))
for group1 in group1s:
    if len(group1) in (0, len(packages), len(packages) - 1):
        continue
    if len(solutions) > 0:
        break
    g1sum = sum(group1)
    g1qe = reduce(lambda x, y: x*y, group1, 1)
    others = tuple(p for p in packages if p not in group1)
    group2s = powerset(others)
    for group2 in group2s:
        if len(group2) in (0, len(others)):
            continue
        g2sum = sum(group2)
        group3 = tuple(p for p in others if p not in group2)
        # print group1, group2, group3
        g3sum = sum(group3)
        if g1sum == g2sum == g3sum:
            solution = (len(group1), g1qe, g1sum, group1, group2, group3)
            solutions.append(solution)

print sorted(solutions)[0]

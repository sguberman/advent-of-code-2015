from itertools import chain, combinations, permutations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in xrange(len(s)+1))



packages = []
with open('day24.txt', 'r') as f:
    for line in f:
        packages.append(int(line.strip()))


group1s = powerset(packages)
for group1 in group1s:
    pass


solutions = []
for n in xrange(1, len(packages)):
    print n
    group1s = combinations(packages, n)
    for group1 in group1s:
        print group1
        others = tuple(p for p in packages if p not in group1)
        print others
        g1sum = sum(group1)
        print g1sum
        g1qe = reduce(lambda x,y: x*y, group1)
        print g1qe
        group2s = parts(g1sum, len(others))
        for group2 in group2s:
            print group2
            if all(p in others for p in group2):
                group3 = tuple(p for p in others if p not in group2)
                if sum(group3) == g1sum:
                    solution = (n, g1qe, g1sum, group1, group2, group3)
                    print solution
                    solutions.append(solution)

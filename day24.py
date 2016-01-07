from itertools import chain, combinations
from operator import mul
from functools import reduce


def powerset(iterable):  # recipe from itertools docs
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


with open('day24.input', 'r') as f:
    packages = sorted([int(line) for line in f], reverse=True)

n_groups = 4
target_weight = sum(packages) / n_groups

first_groups = (g for g in powerset(packages) if sum(g) == target_weight)
quantum_entanglements = (reduce(mul, g) for g in first_groups)

print(next(quantum_entanglements))

from itertools import combinations
from collections import defaultdict


def main():
    with open('day17.input', 'r') as containersfile:
        containers = sorted([int(line) for line in containersfile])

    solutions = defaultdict(list)
    for n in range(len(containers)):
        for combo in combinations(containers, n):
            if sum(combo) == 150:
                solutions[n].append(combo)

    print(len(solutions[min(solutions.keys())]))

if __name__ == '__main__':
    main()

from collections import defaultdict


def factors(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            yield n // i


minpresents = 34000000
maxdeliveries = 50
presents_per_elf = 11
deliveries = defaultdict(int)

for i in range(1, minpresents // presents_per_elf + 1):
    presents = 0
    elves = set(factors(i))
    for elf in elves:
        if deliveries[elf] < maxdeliveries:
            deliveries[elf] += 1
            presents += elf
    presents *= presents_per_elf
    if presents >= minpresents:
        break

print(i, presents)

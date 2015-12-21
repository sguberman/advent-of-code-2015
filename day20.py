def factors(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            yield n // i

minpresents = 34000000

for i in range(1, minpresents/10 + 1):
    presents = 10 * sum(set(factors(i)))
    if presents >= minpresents:
        print i
        break

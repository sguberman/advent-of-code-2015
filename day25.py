def code_number(row, col):
    n = sum(range(1, row)) + 1
    r = row
    c = 1
    nextrow = r + 1
    while not (r == row and c == col):
        r -= 1
        c += 1
        n += 1
        if r == 0:
            r = nextrow
            nextrow += 1
            c = 1
    return n


def code_generator(seed):
    current = seed
    yield current
    while True:
        current = current * 252533 % 33554393
        yield current


def code_lookup(row, col, seed):
    n = code_number(row, col)
    for i, code in enumerate(code_generator(seed)):
        if i + 1 == n:
            return code


print(code_lookup(3010, 3019, 20151125))

from collections import defaultdict
import re


replacements = defaultdict(list)
with open('day19.input1', 'r') as rf:
    for line in rf:
        atom, replacement = line.strip().split(' => ')
        replacements[atom].append(replacement)

with open('day19.input2', 'r') as mf:
    medicine = mf.read().strip()


def atomize(molecule):
    if molecule == 'e':
        return [molecule]
    return re.findall(r'[A-Z][^A-Z]*', molecule)


medicine_atoms = atomize(medicine)


# Part 1
def u_replace(current):
    unique_replacements = set()
    for i, atom in enumerate(current):
        if replacements[atom]:
            for replacement in replacements[atom]:
                molecule = current[:i] + [replacement] + current[i+1:]
                unique_replacements.add(''.join(molecule))
    return unique_replacements

print len(medicine_atoms)
print len(u_replace(medicine_atoms))


# This approach is too slow, too many possibilities?
'''
steps = defaultdict(set)
step = 0
steps[step].add('e')
while len(max(steps[step], key=len)) < len(medicine_atoms):
    current = steps[step]
    step += 1
    print step, len(current), len(max(current, key=len))
    for c in current:
        for r in replace(atomize(c)):
            steps[step].add(r)
print len(steps)
'''

# Maybe I need to work backwards...
revreplace = []
for key, value in replacements.items():
    for v in value:
        revreplace.append((len(v), v, key))
revreplace = tuple(sorted(revreplace, reverse=True))

current = medicine
target = 'e'
count = 0
while current != target:
    for _, old, new in revreplace:
        while current.replace(old, new, 1) != current:
            print current
            print 'replacing', old, 'with', new
            current = current.replace(old, new, 1)
            count += 1

print current, count

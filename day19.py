from collections import defaultdict
import re


replacements = defaultdict(list)
with open('day19.input1', 'r') as rf:
    for line in rf:
        atom, replacement = line.strip().split(' => ')
        replacements[atom].append(replacement)

with open('day19.input2', 'r') as mf:
    medicine = mf.read().strip()

medicine_atoms = re.findall(r'[A-Z][^A-Z]*', medicine)

distinct_replacements = set()
for i, atom in enumerate(medicine_atoms):
    if replacements[atom]:
        for replacement in replacements[atom]:
            molecule = medicine_atoms[:i] + [replacement] + medicine_atoms[i+1:]
            distinct_replacements.add(''.join(molecule))

print len(distinct_replacements)

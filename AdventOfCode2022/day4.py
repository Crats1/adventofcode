with open('day4input.txt', 'r') as f:
    lines = f.readlines()

pairs = [[[int(id) for id in section.split('-')] for section in line.strip().split(',')] for line in lines]

containedPairs = 0
for pair1, pair2 in pairs:
    if (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]) or (pair2[0] >= pair1[0] and pair2[1] <= pair1[1]):
        containedPairs += 1
print('Part 1:', containedPairs) # Answer is 576

overlappingPairs = 0
for pair1, pair2 in pairs:
    if len(range(max(pair1[0], pair2[0]), min(pair1[1], pair2[1]) + 1)):
        overlappingPairs += 1
print('Part2:', overlappingPairs) # Answer is 905

# Better solutions
print('Part1:', sum([1 for p1, p2 in pairs if set(range(*p1)) > set(range(*p2)) or set(range(*p2)) > set(range(*p1))])) # * is splat operator
print('Part1:', sum([1 for (s1, e1), (s2, e2) in pairs if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1)]))
print('Part2:', sum([1 for (s1, e1), (s2, e2) in pairs if len(range(max(s1, s2), min(e1, e2) + 1))]))
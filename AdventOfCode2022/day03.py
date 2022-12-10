with open('day3input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

priority = 0
for line in lines:
    half = len(line) // 2
    common =  (set(line[:half]) & set(line[half:])).pop()
    priority += ord(common) - (96 if common.islower() else 38)
print('Part 1:', priority)  # Answer is 7872

badgePriority = 0
for i in range(0, len(lines), 3):
    badge = (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    badgePriority += ord(badge) - (96 if badge.islower() else 38)
print('Part 2:', badgePriority) # Answer is 2497
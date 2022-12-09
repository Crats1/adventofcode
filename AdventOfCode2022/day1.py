# First solution
with open('day1input.txt', 'r') as f:
    lines = f.readlines()

elfCalories = []
calories = 0
for line in lines:
    if line == '\n':
        elfCalories += [calories]
        calories = 0
    else: calories += int(line) 
print('Part 1 most calories:', max(elfCalories))

elfCalories = sorted(elfCalories, reverse=True)
print('Part2 calories', sum(elfCalories[:3]))

# Clean solution
with open('day1_input.txt', 'r') as f:
    data = [sum(int(x) for x in line.split()) for line in f.read().split('\n\n')]
print('Part 1:', max(data))
print('Part 2:', sum(sorted(data, reverse=True)[:3]))
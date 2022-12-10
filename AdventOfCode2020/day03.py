def read_input():
    with open('day3input.txt') as f:
        return [line.strip() for line in f]

def trees_encountered(input, dx, dy):
    return sum([input[y][(int(y / dy) * dx) % len(input[0])] == '#' for y in range(dy, len(input), dy)])

def multiply_trees_encountered(input):
    paths = [(1, 1,), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for path in paths:
        result *= trees_encountered(input, path[0], path[1])
    return result

input = read_input()
print("Part1:", trees_encountered(input, 3, 1)) # Answer: 153
print("Part2:", multiply_trees_encountered(input)) # Answer: 2421944712
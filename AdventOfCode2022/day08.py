with open('day8input.txt', 'r') as f:
    lines = [[int(c) for c in line.strip()] for line in f.readlines()]

def part1():
    treesVisible = ((len(lines) - 2) * 2) + (len(lines[0]) * 2)
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[0]) - 1):
            current = lines[row][col]
            if max(lines[row][:col]) < current or max(lines[row][col + 1:]) < current: # Check row
                treesVisible += 1
            elif max([lines[i][col] for i in range(row)]) < current or max([lines[i][col] for i in range(row + 1, len(lines))]) < current: # Check column
                treesVisible += 1
    return treesVisible

print('Part1:', part1()) # Answer is 1543

def part2():
    highestScenicScore = 0
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[0]) - 1):
            current = lines[row][col]
            visibleUp = 0
            for i in range(row - 1, -1, -1):
                visibleUp += 1
                if lines[i][col] >= current: break

            visibleDown = 0
            for i in range(row + 1, len(lines)):
                visibleDown += 1
                if lines[i][col] >= current: break

            visibleLeft = 0
            for i in range(col - 1, -1, -1):
                visibleLeft += 1
                if lines[row][i] >= current: break

            visibleRight = 0
            for i in range(col + 1, len(lines[0])):
                visibleRight += 1
                if lines[row][i] >= current: break

            scenicScore = visibleUp * visibleDown * visibleLeft * visibleRight
            if scenicScore > highestScenicScore: highestScenicScore = scenicScore
    return highestScenicScore

print('Part2:', part2()) # Answer is 595080
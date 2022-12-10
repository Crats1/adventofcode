with open('day9input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    lines = [[step[0], int(step[1])] for step in lines]

dirOffsets = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def isTailTouching(head, tail):
    return (abs(head[0] - tail[0]) <= 1) and (abs(head[1] - tail[1]) <= 1)

visited = set()
headCoord = (0, 0)
tailCoord = (0, 0)
visited.add(tailCoord)
for dir, steps in lines:
    for _ in range(steps):
        offset = dirOffsets[dir]
        prevHeadCoord = headCoord
        headCoord = (headCoord[0] + offset[0], headCoord[1] + offset[1])
        if not isTailTouching(headCoord, tailCoord):
            tailCoord = prevHeadCoord
            visited.add(tailCoord)

print('Part1:', len(visited)) # Answer is 6269

def getAdjacentCoord(head, tail):
    for offset in dirOffsets.values():
        newCoord = (head[0] + offset[0], head[1] + offset[1])
        if isTailTouching(newCoord, tail): return newCoord
    return None

ROPE_LEN = 10
visited = set()
ropeCoords = [(0, 0) for _ in range(ROPE_LEN)]
for dir, steps in lines:
    for _ in range(steps):
        offset = dirOffsets[dir]
        prevHeadCoord = ropeCoords[0]
        ropeCoords[0] = (ropeCoords[0][0] + offset[0], ropeCoords[0][1] + offset[1])
        for i in range(1, ROPE_LEN):
            current = ropeCoords[i]
            if not isTailTouching(ropeCoords[i - 1], current):
                newCoord = getAdjacentCoord(ropeCoords[i - 1], current)
                ropeCoords[i] = newCoord if newCoord else prevHeadCoord
            prevHeadCoord = current
        visited.add(ropeCoords[-1])

print('Part2:', len(visited)) # Answer is 2557
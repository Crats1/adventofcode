with open('day7input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

class Node:
    def __init__(self, parent=None) -> None:
        self.directories = {}
        self.files = {}
        self.parent = parent
        self.size = 0

    def addFile(self, name, size):
        self.files[name] = int(size)
    
    def addDirectory(self, name):
        self.directories[name] = Node(parent=self)
    
    def changeDirectory(self, name):
        return self.directories[name]
    
    def moveToParent(self):
        return self.parent

root = Node()
current = root
for line in lines:
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '..': current = current.moveToParent()
        elif line[2] != '/': current = current.changeDirectory(line[2])
    elif line[0] == 'dir':
        current.addDirectory(line[1])
    elif line[0].isdigit():
        current.addFile(line[1], line[0])

def calculateDirSize(node):
    files = sum(node.files.values())
    if len(node.directories):
        node.size = files + sum([calculateDirSize(directory) for directory in node.directories.values()])
        return node.size
    node.size = files
    return node.size

totalSize = calculateDirSize(root)
print('Total size:', totalSize)

def part1(node):
    currentSize = node.size if node.size <= 100000 else 0
    return currentSize + sum([part1(directory) for directory in node.directories.values()])
print('Part1:', part1(root)) # Answer is 1391690

minimumRequiredSpace = 30000000 - (70000000 - totalSize)
def part2(node):
    currentSize = node.size if node.size >= minimumRequiredSpace else totalSize
    return min([currentSize] + [part2(directory) for directory in node.directories.values()])

print('minimumRequiredSpace:', minimumRequiredSpace)
print('Part2:', part2(root)) # Answer is 5469168
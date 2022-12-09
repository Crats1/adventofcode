with open('day6input.txt', 'r') as f:
    stream = f.readlines()[0]

def isBufferUnique(buffer):
    return len(set(buffer)) == len(buffer)

last4Chars = stream[:4]
for i, c in enumerate(stream[4:]):
    if len(set(last4Chars)) == len(last4Chars):
        print('Part1:', i + 4)
        break
    last4Chars = last4Chars[1:] + c

last14Chars = stream[:14]
for i, c in enumerate(stream[14:]):
    if len(set(last14Chars)) == len(last14Chars):
        print('Part2:', i + 14)
        break
    last14Chars = last14Chars[1:] + c


with open('day5input.txt', 'r') as f:
    moves = [line.strip().replace('move ', '').replace('from ', '').replace('to ', '').split(' ') for line in f.read().split('\n\n')[1].split('\n')]
    moves = [[int(i) for i in nums] for nums in moves]


stacks = ['ZTFRWJG', 'GWM', 'JNHG', 'JRCNW', 'WFSBGQVM', 'SRTDVWC', 'HBNCDZGV', 'SJNMGC', 'GPNWCJDL']
for num, source, dest in moves:
    moved = min(len(stacks[source - 1]), num)
    stacks[dest - 1] += stacks[source - 1][-moved:][::-1]
    stacks[source - 1] = stacks[source - 1][:len(stacks[source - 1]) - moved]

print('Part1:', ''.join([stack[-1] for stack in stacks if stack])) # Answer is CWMTGHBDW

stacks = ['ZTFRWJG', 'GWM', 'JNHG', 'JRCNW', 'WFSBGQVM', 'SRTDVWC', 'HBNCDZGV', 'SJNMGC', 'GPNWCJDL']
for num, source, dest in moves:
    moved = min(len(stacks[source - 1]), num)
    stacks[dest - 1] += stacks[source - 1][-moved:]
    stacks[source - 1] = stacks[source - 1][:len(stacks[source - 1]) - moved]

print('Part2:', ''.join([stack[-1] for stack in stacks if stack])) # Answer is SSCGWJCRB
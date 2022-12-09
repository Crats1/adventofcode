with open('day2input.txt', 'r') as f:
    lines = f.readlines()

opponentMoves = 'ABC'
yourMoves = 'XYZ'
moves = [line.strip().split(' ') for line in lines]
moves = [(ord(move[0]) - ord('A'), ord(move[1]) - ord('X')) for move in moves]

winningMoves = [3, 1, 2]
score = 0

for opponent, player in moves:
    score += player + 1
    if opponent == player: score += 3 # Draw
    elif winningMoves[player] == opponent + 1: score += 6 # Win

print('Part 1:', score) # Answer is 15572

score = 0
losingMoves = [2, 3, 1]
for opponent, player in moves:
    if player == 0: score += winningMoves[opponent] # Lose
    elif player == 1: score += 3 + opponent + 1 # Draw
    else:           score += 6 + losingMoves[opponent] # Win

print('Part 2:', score) # Answer is 16098
'''
A, X - Rock 1
B, Y - Paper 2
C, Z - Scissors 3
'''
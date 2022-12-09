def read_input():
    with open('day5input.txt') as f:
        return f.read().splitlines()

def calculateSeatIds(seats):
    seat_ids = []
    for seat in seats:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(seat[7:].replace('R', '1').replace('L', '0'), 2)
        seat_ids.append(row * 8 + col)
    return seat_ids

def calculateMySeat(ids):
    return [i for i in range(min(ids), max(ids)) if (i - 1) in ids and (i + 1) in ids and i not in ids]

seats = read_input()
seat_ids = calculateSeatIds(seats)
print('max ID:', max(seat_ids)) # Answer: 955
print('possible IDs:', calculateMySeat(seat_ids)) # Answer: 569
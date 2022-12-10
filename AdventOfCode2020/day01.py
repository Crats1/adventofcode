with open('day1input.txt') as f:
    entries = [int(line) for line in f.readlines()]

def part1():
    for entry1 in entries:
        new_entries = [entry for entry in entries if entry != entry1]
        for new_entry in new_entries:
            if entry1 + new_entry == 2020:
                print(entry1, new_entry, entry1 * new_entry)

def part2():
    for entry1 in entries:
        entries2 = [entry for entry in entries if entry != entry1]
        for entry2 in entries2:
            entries3 = [entry for entry in entries2 if entry != entry2]
            for entry3 in entries3:
                if entry1 + entry2 + entry3 == 2020:
                    print(entry1, entry2, entry3, '|', entry1 + entry2 + entry3, entry1 * entry2 * entry3)

print("---Part1---")
part1() # Answer 1020084
print("---Part2---")
part2() # Answer 295086480
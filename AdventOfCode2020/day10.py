def read_input():
    with open('day10input.txt') as f:
        return [int(i) for i in f.read().splitlines()]


def part1(joltages):
    outlet_joltage = 0
    device_joltage = max(joltages) + 3
    return

output_joltages = read_input()
print("P1:", part1(output_joltages))

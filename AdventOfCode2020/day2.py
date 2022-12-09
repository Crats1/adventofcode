def read_input():
    with open('day2input.txt') as f:
        content = f.readlines()
    parsed_content = []
    for x in content:
        item = x.strip().split(':')
        item[0] = item[0].split(' ')
        parsed_content.append(item)
    return parsed_content

def validate_passwords(input, fn):
    valid_passwords = 0
    for entry in input:
        if fn(entry[0], entry[1]):
            valid_passwords += 1
    return valid_passwords

def validate_password_part1(policy, password):
    # Test data 
    # Policy: ['6-10', 's'] Password: 'snkscgszxsssscss'
    # Policy: ['15-17', 'b'] Password: ' bbbbbbbbbbbbbbbbb'
    characterRange = policy[0].split('-')
    minimum = int(characterRange[0])
    maximum = int(characterRange[1])
    character = policy[1]
    character_count = password.count(character)
    return character_count >= minimum and character_count <= maximum

def validate_password_part2(policy, password):
    character_positions = policy[0].split('-')
    position1 = int(character_positions[0]) - 1
    position2 = int(character_positions[1]) - 1
    character = policy[1]
    password = password.replace(' ', '')
    return ((password[position1] == character) + (password[position2] == character)) == 1

input = read_input()
print('Part1:', validate_passwords(input, validate_password_part1)) # Answer: 414
print('Part2:', validate_passwords(input, validate_password_part2)) # Answer: 413
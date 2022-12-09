REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_EYE_COLOURS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def is_int_valid_year(n, minimum, maximum):
    return len(n) == 4 and n.isdigit() and int(n) >= minimum and int(n) <= maximum

def is_passport_valid(d):
    for field in REQUIRED_FIELDS:
        if field not in d:
            return False
    return True

def read_input():
    content = []
    with open('day4input.txt') as f:
        d = {}
        for line in f:
            if line.strip() == '':
                content.append(d)
                d = {}
            if line.strip():
                formatted_line = line.strip().split(' ')
                formatted_line = [field.split(':') for field in formatted_line]
                for item in formatted_line:
                    d[item[0]] = item[1]
        content.append(d)
    return content

def is_field_valid(d, field):
    def is_height_valid(d):
        if int(d[field][0:len(d[field]) - 2]) and d[field][len(d[field]) - 2:] in ('cm', 'in'):
            number = int(d[field][0:len(d[field]) - 2])
            measurement = d[field][len(d[field]) - 2:]
            return (measurement == 'cm' and number in range(150, 194)) or (measurement == 'in' and number in range(59, 77))
        return False
    try:
        if (field == 'byr' and is_int_valid_year(d[field], 1920, 2002)) or \
            (field == 'iyr' and is_int_valid_year(d[field], 2010, 2020)) or \
            (field == 'eyr' and is_int_valid_year(d[field], 2020, 2030)) or \
            (field == 'hgt' and is_height_valid(d)) or \
            (field == 'hcl' and d[field][0] == '#' and len(d[field]) == 7 and int(d[field][1:], 16)) or \
            (field == 'ecl' and d[field] in VALID_EYE_COLOURS) or \
            (field == 'pid' and len(d[field]) == 9 and int(d[field])):
            return True        
        return False
    except:
        return False

def are_fields_valid(d):
    for field in REQUIRED_FIELDS:
        if field not in d or not is_field_valid(d, field):
            return False
    return True

input = read_input()

valid_passports_part1 = 0
valid_passports_part2 = 0
for d in input:
    if is_passport_valid(d):
        valid_passports_part1 += 1
        if are_fields_valid(d):
            valid_passports_part2 += 1

print('p1:', valid_passports_part1)
print('p2:', valid_passports_part2)

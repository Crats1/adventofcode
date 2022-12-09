def read_input():
    with open('day7input.txt') as f:
        text = f.read().strip().replace(' ', '').replace('.', '').split('\n')
        text = [line.split('contain') for line in text]
        return dict([[rule[0], rule[1].split(',')]for rule in text])

def can_contain_shiny_gold_bag(rules_dict):
    valid_bags = set([key for key in rules_dict.keys() for content in rules_dict[key] if 'shinygoldbag' in content])
    bag_found = True
    while bag_found:
        bag_found = False
        for key in rules_dict.keys():
            contents = rules_dict[key]
            for content in contents:
                if content[-1] != 's':
                    content += 's'
                if content[1:] in valid_bags and key not in valid_bags:
                    bag_found = True
                    valid_bags.add(key)
    return len(valid_bags)

def count_bags_shiny_gold_bag(rules_dict):
    bags = [[bag[0], bag[1:]] for bag in rules_dict['shinygoldbags']]
    container_bags_count = 0
    contains_bags = True
    while contains_bags:
        contains_bags = False
        new_bags = []
        for bag in bags:
            if bag[1][-1] != 's':
                bag[1] += 's'
            bag_count = int(bag[0])
            bag_type = bag[1]
            if rules_dict[bag_type][0] != 'nootherbags':
                contains_bags = True
                container_bags_count += bag_count
                new_bags.extend([[int(new_bag[0]) * bag_count, new_bag[1:]] for new_bag in rules_dict[bag_type]])
            else:
                new_bags.append(bag)
        if contains_bags:
            bags = new_bags
    return sum([int(item[0]) for item in bags]) + container_bags_count

rules = read_input()
print("P1:", can_contain_shiny_gold_bag(rules)) # Answer: 213
print("P2:", count_bags_shiny_gold_bag(rules)) # Answer: 38426
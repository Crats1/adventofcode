def read_input():
    with open('day9input.txt') as f:
        return [int(i) for i in f.read().splitlines()]

def copy_and_remove(lst, x):
    copy = lst.copy()
    copy.remove(x)
    return copy

def find_invalid_number(nums):
    first_25_nums = numbers[:25]
    for i in range(25, len(nums)):
        if nums[i] not in [x + y for x in first_25_nums for y in copy_and_remove(first_25_nums, x)]:
            return nums[i]
        first_25_nums.pop(0)
        first_25_nums.append(nums[i])

def find_encryption_weakness(nums, invalid_num):
    for i in range(len(nums)):
        continguous_lst = [nums[i]]
        for j in range(i + 1, len(nums)):
            next_summation = sum(continguous_lst + [nums[j]])
            if next_summation > invalid_num:
                break
            continguous_lst.append(nums[j])
        final_summation = sum(continguous_lst)
        if len(continguous_lst) >= 2 and final_summation == invalid_num:
            return min(continguous_lst) + max(continguous_lst)

numbers = read_input()
invalid_number = find_invalid_number(numbers)
print("P1:", invalid_number) # Answer is 20874512
print("P2:", find_encryption_weakness(numbers, invalid_number)) # Answer is 3012420
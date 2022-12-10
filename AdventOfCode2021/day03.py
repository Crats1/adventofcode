def bitcount(a, bit):
	n = len(a[0])
	return [sum([1 for s in a if s[i] == bit]) for i in range(n)]

def part1(a):
        print("----Part 1----")
	gamma = ''
	epsilon = ''
	ones = bitcount(a, '1')
	zeroes = bitcount(a, '0')
	for i in range(len(a[0])):
		if ones[i] > zeroes[i]:
			gamma += '1'
			epsilon += '0'
		else:
			gamma += '0'
			epsilon += '1'
	print(int(gamma, 2) * int(epsilon, 2))

def part2(a):
        print("----Part 2----")
	n = len(a[0])
	oxygen = ''
	co2 = ''
	oxygenNums = [x for x in a]
	co2Nums = [x for x in a]
	for i in range(n):
		oxygenOnes = bitcount(oxygenNums, '1')
		oxygenZeroes = bitcount(oxygenNums, '0')
		oxygenBit = '1' if oxygenOnes[i] >= oxygenZeroes[i] else '0'		
		if len(oxygenNums) > 1:
			oxygen += oxygenBit
			oxygenNums = [x for x in oxygenNums if x[i] == oxygenBit]
		co2Ones = bitcount(co2Nums, '1')
		co2Zeroes = bitcount(co2Nums, '0')
		co2Bit = '0' if co2Zeroes[i] <= co2Ones[i] else '1'
		if len(co2Nums) > 1:
			co2 += co2Bit
			co2Nums = [x for x in co2Nums if x[i] == co2Bit]
	print("OXYGEN:", oxygen, oxygenNums)
	print("CO2:   ", co2, co2Nums)
	print(int(oxygenNums[0], 2) * int(co2Nums[0], 2))

with open('day3input.txt') as f:
	data = f.read().strip().splitlines()
part1(data)
part2(data)

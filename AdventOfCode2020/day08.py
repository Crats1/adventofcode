def read_input():
    with open('day8input.txt') as f:
        return [instruction.split(' ') for instruction in f.read().split('\n')]

def value_in_accumulator(instr):
    accumulator, commandIndex = 0, 0
    executedCommands = set()
    while commandIndex < len(instr):
        if commandIndex in executedCommands:
            return (accumulator, False)
        instruction = instr[commandIndex]
        executedCommands.add(commandIndex)
        if instruction[0] == 'jmp':
            commandIndex += int(instruction[1])
        elif instruction[0] == 'acc':
            accumulator += int(instruction[1])
            commandIndex += 1
        else:
            commandIndex += 1
    return (accumulator, True)
   
def accumulator_after_termination(original_instructions):
    for i in range(len(original_instructions)):
        instruction = original_instructions[i]
        if instruction[0] == 'jmp':
            accumulator, terminates = value_in_accumulator(original_instructions[:i] + [['nop', instruction[1]]] + original_instructions[i + 1:])
            if terminates: return accumulator
        elif instruction[0] == 'nop':
            accumulator, terminates = value_in_accumulator(original_instructions[:i] + [['jmp', instruction[1]]] + original_instructions[i + 1:])
            if terminates: return accumulator
    return -1

instructions = read_input()
print('P1:', value_in_accumulator(instructions)[0]) # Answer: 2051
print('P2:', accumulator_after_termination(instructions)) # Answer: 2304
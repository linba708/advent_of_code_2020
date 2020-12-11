import functools 

## part one
accumulator = 0
with open('data/day8.txt') as reader:
    operations = [line.strip() for line in reader.readlines()]
    operations_visited = set()

    i = 0
    while(i < len(operations)):
        [operation , argument] = operations[i].split(' ')
        if operations_visited.issuperset({i}):
            break
        operations_visited.add(i)
        if operation == 'acc':
            accumulator += int(argument)
            i += 1 
        elif operation == 'jmp':
            i += int(argument)
        else:
            i += 1
        # print('run command', operation, argument, accumulator)
        

    #print(instructions)
    print(accumulator)

## Part two
def execute_instruction(op_list, i, visited, acc, changed):
    # print(op_list[i],i, visited, acc)
    if i == len(op_list):
        return acc
    [operation , argument] = op_list[i].split(' ')
    if visited.issuperset({i}):
        return 0
    elif operation == 'acc':
        return execute_instruction(op_list, (i + 1), visited.union({i}), (acc + int(argument)), changed)
    elif operation == 'jmp':
        if changed == False:
            alt = execute_instruction(op_list, (i + 1), visited.union({i}), acc, True)
            if alt != 0:
                return alt
        return execute_instruction(op_list, (i + int(argument)), visited.union({i}), acc, changed) 
    elif operation == 'nop':
        if changed == False:
            alt = execute_instruction(op_list, (i + int(argument)), visited.union({i}), acc, True)
            if alt != 0:
                return alt
        return execute_instruction(op_list, (i + 1), visited.union({i}), acc, changed)

with open('data/day8.txt') as reader:
    op_list = [line.strip() for line in reader.readlines()]
def execute(i, visited, changed):
    if i == len(op_list):
        return visited
    if visited.issuperset({i}):
        return None
    [op, arg] = op_list[i].split(' ')
    next = i + 1
    jmp = i + int(arg)
    visited = visited.union({i})
    if op == 'acc':
        return execute(next, visited, changed)
    if (changed == False):
        alt_path = execute(next, visited, True) if op == 'jmp' else execute(jmp, visited, True)
        if alt_path is not None:
            return alt_path    
    return execute(next, visited, changed) if op == 'nop' else execute(jmp, visited, changed)

def accumilate(instruction):
    [op, arg] = instruction.split(' ')
    return int(arg) if op == 'acc' else 0

print(execute_instruction(op_list, 0, set(), 0, False))
correct_path = execute(0, set(), False)
print(functools.reduce(lambda a,b : a+b ,[accumilate(op_list[i]) for i in correct_path]))


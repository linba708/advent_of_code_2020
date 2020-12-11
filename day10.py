import functools

def find_permutations(list, acc):
    if len(list) < 3:
        return acc
    for i in range(len(list)):
        if i == len(list) - 2:
            return acc
        elif list[i + 2] - list[i] <= 3:
            acc += 1
            acc += find_permutations([list[i]] + list[i + 2:], 0)
    return acc

def split_adapters_to_parts(adapters):
    parts = []
    i = 0
    while i < len(adapters) - 1:
        if adapters[i + 1] - adapters[i] == 3:
            i += 1
            continue
        else:
            j = i
            while j < len(adapters) - 1:
                if adapters[j + 1] - adapters[j] == 3:
                    break
                j += 1
            if len(adapters[i:j + 1]) >= 3:
                parts.append(adapters[i:j + 1])
            i = j
    return parts

#read data
outlet = [0]
with open('data/day10.txt') as reader:
    adapters = [int(line.strip()) for line in reader.readlines()]
    

adapters.sort()
adapters = outlet + adapters + [adapters[len(adapters) -1] + 3]
print(adapters)

# print(adapters[:2] + adapters[3:])

# part one
jolt_diff_1 = 0
jolt_diff_3 = 0
for i, adapter in enumerate(adapters):
    if i == len(adapters) - 1:
        break
    elif adapters[i+1] - adapter == 3:
        jolt_diff_3 += 1
    elif adapters[i + 1] - adapter == 1:
        jolt_diff_1 += 1

print('Part one', jolt_diff_3 * jolt_diff_1)

parts = split_adapters_to_parts(adapters)


print(adapters)
print(parts)
print([find_permutations(part, 1) for part in parts])
print(functools.reduce(lambda a, b : a * b ,[find_permutations(part, 1) for part in parts]))

exit()


# part two
arrangements = 1  # original list
arrangements += find_permutations(adapters, [0])
print(arrangements)
part_one = adapters[:4]
part_two = adapters[4:]
# for i, adapter in enumerate(adapters):
#     for j in range(i + 2, len(adapters)):
#         if adapters[j] - adapter <= 3:
#             arrangements += find_permutations()
#         else:
#             break
# print(arrangements)

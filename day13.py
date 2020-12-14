import math
import functools

def Euclid(*integers):
    if type(integers[0])==list or type(integers[0])==tuple:
        integers = integers[0]
    if len(integers) == 2:
        a,b = integers[0],integers[1]
        while b != 0:
            a,b = b, a%b
        return a
    else:
 	    return Euclid(integers[0],Euclid(integers[1:]))

# Part one
#read data
with open('data/day13.txt') as reader:

    file_input = [line.strip() for line in reader.readlines()]

arrival = int(file_input[0])
busses = [int(buss) for buss in file_input[1].split(',') if buss != 'x']

wating_time = {}
for buss in busses:
    if arrival % buss == 0:
        print(buss, 0)
    wating_time[(math.floor(arrival / buss) + 1) * buss - arrival] = buss


for key in sorted(wating_time.keys()):
    print(key* wating_time[key])
    break
print(arrival)
print(busses)

#part two
with open('data/day13.txt') as reader:

    file_input = [line.strip() for line in reader.readlines()]

# arrival = int(file_input[0])
busses = [buss for buss in file_input[1].split(',')]
lines = [(int(buss), i) for i, buss in enumerate(busses) if buss != 'x']

increments = [buss[0] for buss in lines]
adjusted_increments = [(buss[0] * buss[1], buss[1]) if buss[1] in increments else (buss[0], buss[1]) for i, buss in enumerate(lines)]
adjusted_increments.sort(key=lambda tup: tup[0])
print('increments', adjusted_increments)
print(adjusted_increments[-1])




largest_buss =  adjusted_increments[-1]
print(largest_buss)
multiple = 1
to_check = 1068781
print(Euclid([line[0] for line in lines]))
print(functools.reduce(lambda a, b: a + b, [(to_check + buss[1]) % buss[0] for buss in lines]))

# while True:
#     to_check = (largest_buss[0] * multiple) - largest_buss[1]
#     if (functools.reduce(lambda a, b: a + b, [(to_check + buss[1]) % buss[0] for buss in lines])) == 0:
#         break
#     # print(to_check)
#     # print(multiple)
#     # print([(to_check + buss[1]) % buss[0] for buss in lines])
#     multiple += 1
# print([to_check + buss[1] % buss[0] for buss in lines])

# print(functools.reduce(lambda a, b: a + b, [(to_check + buss[1]) % buss[0] for buss in lines]))
# print(busses)
print('_______________')
print(to_check)
print(lines)

# code from https://github.com/q-viper/Adevent-Of-Code-2020
#Chinese Remainder Theorem

# LINES = file_input
# print(file_input)

# busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]

# print(busses)
# def part2():
#     mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
#     print(mods)
#     vals = list(reversed(sorted(mods)))
#     val = mods[vals[0]]
#     r = vals[0]
#     print(vals, val, r)
#     for b in vals[1:]:
#         while val % b != mods[b]:
#             val += r
#         r *= b
#     return val
# print(part2())


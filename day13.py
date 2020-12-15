import math
import functools

# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(tuple_list):
    sum = 0
    prod = functools.reduce(lambda a,b: a*b, [t[0] for t in tuple_list])
    for n_i, a_i in tuple_list:
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

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


busses = [(int(buss), i) for i, buss in enumerate(file_input[1].split(',')) if buss != 'x']
busses.sort(key=lambda buss: -buss[1])
last_buss_offset = busses[0][1]
# adjust_a_for_busses so that
busses_adjusted = [(buss[0], int(last_buss_offset) - int(buss[1])) for buss in busses]
print('answer', chinese_remainder(busses_adjusted) - last_buss_offset)

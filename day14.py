import functools
import re

# Part one
# find_number = re.compile(r"\d+")
# mem = {}

# one_mask = 0
# zero_mask = 0

# def create_masks(mask_as_string):
#     one_mask = ''.join([char if char=='1' else '0' for char in list(mask_as_string)])
#     zero_mask = ''.join([char if char=='0' else '1' for char in list(mask_as_string)])
#     return (one_mask, zero_mask)

# #read data
# with open('data/day14.txt') as reader:
#     for line in reader.readlines():
#         ins, val = line.strip().split(' = ')
#         if ins == 'mask':
#            one_mask, zero_mask = create_masks(val)
#         else:
#             val_masked = (int(val) | int(one_mask, 2)) & int(zero_mask, 2)
#             adress = int(find_number.findall(ins)[0])
#             mem[adress] = val_masked

# print(mem)
# print(functools.reduce(lambda a, b: a + b, mem.values()))

find_number = re.compile(r"\d+")
mem = {}

print(mem)
print(int('111111111111111111111111111111111111',2))
one_mask = ''
zero_mask = ''
adress_range = ''

def create_masks(mask_as_string):
    one_mask = ''.join([char if char=='1' else '0' for char in list(mask_as_string)])
    zero_mask = ''.join(['0' if char == 'X' else '1' for char in list(mask_as_string)])
    x_mask = ''.join(['X' if char == 'X' else '0' for char in list(mask_as_string)])
    amount_of_x = zero_mask.count('0')
    adress_range = []
    for n in range(2 ** amount_of_x):
        new_adress = x_mask
        for char in bin(n)[2:].zfill(amount_of_x):
            new_adress = new_adress.replace('X',char, 1)
        adress_range.append(int(new_adress, 2))
    # print('got here again', adress_range)
    return (one_mask, zero_mask, adress_range)

#read data
with open('data/day14.txt') as reader:
    for line in reader.readlines():
        ins, val = line.strip().split(' = ')
        if ins == 'mask':
           one_mask, zero_mask,adress_range = create_masks(val)
        else:
            val = int(val)
            adress = int(find_number.findall(ins)[0])
            adress_masked = (int(adress) | int(one_mask, 2)) & int(zero_mask, 2)
            for offset in adress_range:
                mem[adress_masked + offset] = val

# print(mem)
print(functools.reduce(lambda a, b: a + b, mem.values()))
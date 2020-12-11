import functools

def is_sum_of(number_to_check, list_of_numbers):
    for i, number in enumerate(list_of_numbers[:-1]):  
        complementary = number_to_check - number
        if complementary in list_of_numbers[i + 1:]:  
            return True
    return False

def find_sum_range(find, arr, max_range):
    for i in range(0,max_range):
        for j in range(i, max_range):
            sum = functools.reduce(lambda a, b: a + b, arr[i:j + 1])
            if sum > find:
                break
            if sum == find:
                return arr[i:j + 1]

## part one
preamble_length = 25
with open('data/day9.txt') as reader:
    numbers = [int(line)for line in reader.readlines()]

invalid_number = 0
max_range = 0
for i in range(preamble_length, len(numbers)):
    if not is_sum_of(numbers[i], numbers[i - preamble_length:i]):
        invalid_number = numbers[i]
        max_range = i
        break

print('Part one: invalid number', invalid_number)

sum_range = find_sum_range(invalid_number, numbers, max_range)
print(sum_range)
min, *_, max = sorted(sum_range)

print('Part two:', min + max)


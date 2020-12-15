import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
# Part one and two
def part_one(numbers, stop):
    i = len(numbers) + 1
    spoken_numbers = {num: (j + 1, j + 1) for j, num in enumerate(numbers)}
    to_speak = numbers[-1]
    previusly_spoken = spoken_numbers[to_speak]
    while i < stop + 1:
        to_speak = previusly_spoken[0] - previusly_spoken[1]
        if to_speak not in spoken_numbers:
            spoken_numbers[to_speak] = (i, i)
        else:
            spoken_numbers[to_speak] = (i,spoken_numbers[to_speak][0])
        previusly_spoken = spoken_numbers[to_speak]
        if (i % 5000000 == 0):
            print(i)
        i += 1
    print(to_speak)

def alternative(numbers, stop):
    i = len(numbers) + 1
    spoken_arr = [None]*stop
    for j, num in enumerate(numbers):
        spoken_arr[num] = (j + 1, j + 1)
    to_speak = numbers[-1]
    previusly_spoken = spoken_arr[to_speak]
    while i < stop + 1:
        to_speak = previusly_spoken[0] - previusly_spoken[1]
        if spoken_arr[to_speak] is None:
            spoken_arr[to_speak] = (i, i)
            previusly_spoken = (i, i)
        else:
            j = spoken_arr[to_speak][0]
            spoken_arr[to_speak] = (i,j)
            previusly_spoken = (i,j)
        if (i % 5000000 == 0):
            print('loop nr:',i)
        i += 1
    print(to_speak)    

numbers = []
#read data
with open('data/day15.txt') as reader:
    for line in reader.readlines():
        numbers = [int(n) for n in line.strip().split(',')]

testdict = {1: 'hello', 2: 'world'}
testdict[3] = []
print(testdict[3])
# part_one(numbers, 2020)
wrapped = wrapper(part_one, numbers, 2020)
print(timeit.timeit(wrapped,number=1))
wrapped = wrapper(part_one, numbers, 30000000)
print(timeit.timeit(wrapped,number=1))
wrapped = wrapper(alternative, numbers, 30000000)
print(timeit.timeit(wrapped,number=1))
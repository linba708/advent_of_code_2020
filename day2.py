import re

##part one
# correct_passwords = 0
# print('starting')
# with open('data/day2.txt') as reader:
#     for line in reader.readlines():
#         number, letterColon, password = line.strip().split(' ')
#         lowerBound, higherBound = [int(i) for i in number.split('-')]
#         letter = letterColon.split(':')[0]
#         if lowerBound <= password.count(letter) <= higherBound:
#             correct_passwords += 1
        
    
# print(correct_passwords)

## Part two
correct_passwords = 0
print('starting')

# reader = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
with open('data/day2.txt') as reader:
    for line in reader.readlines():
        number, letterColon, password = line.strip().split(' ')
        lowerBound, higherBound = [int(i) for i in number.split('-')]
        letter = letterColon.split(':')[0]

        if (password[lowerBound-1] == letter) != (password[higherBound-1] == letter) :
            correct_passwords += 1

    
    
print(correct_passwords)
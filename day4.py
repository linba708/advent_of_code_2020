from functools import reduce
import re
# ## Part One
# required_field = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
# valid_passports = 0

# with open('data/day4.txt') as reader:
#     passports = reader.read().split('\n\n')
#     for passport in passports:
#         if required_field.issubset(set([field.split(':')[0] for field in passport.split()])):
#             valid_passports += 1
# print('valid passports ', valid_passports)

## Part Two
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid(Passport ID) - a nine - digit number, including leading zeroes.
hgt_reg = re.compile("[0-9]+(in|cm)$")
hcl_reg = re.compile("#[0-9a-f]{6}$")
pid_reg = re.compile("[0-9]{9}$")

def hgt_func(x):
    if hgt_reg.match(x) is not None:
        unit = x[-2:]
        if unit == 'cm':
            return 150 <= int(x[0:-2]) <= 193
        if unit == 'in':
            return 59 <= int(x[0:-2]) <= 76
    return False

required_field = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: hgt_func(x),
    'hcl': lambda x: hcl_reg.match(x) is not None,
    'ecl': lambda x: ['amb','blu','brn','gry','grn', 'hzl', 'oth'].count(x) == 1,
    'pid': lambda x: pid_reg.match(x) is not None,
    }
valid_passports = 0

with open('data/day4.txt') as reader:
    passports = reader.read().split('\n\n')
    for passport in passports:
        passport_dict = dict(field.split(':') for field in passport.split())
        if set(required_field).issubset(set(passport_dict)):
            validated = [func(passport_dict[key]) for key, func in required_field.items()];

            # print(validated)
            # print(reduce(lambda a, b: a and b, validated))
            if reduce(lambda a, b: a and b, validated):
                valid_passports += 1
print('valid passports ', valid_passports)
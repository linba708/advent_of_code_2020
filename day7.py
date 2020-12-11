import re

##  Part one
# regex = re.compile(' contain |, ')

# searched_for = 'shiny gold bag'
# no_bag = 'no other bag'
# bad_rulse = dict()

# with open('data/day7.txt') as reader:
#     for line in reader.readlines():
#         bags = regex.split(line.strip('.\n').replace('bags', 'bag'))
#         if no_bag == bags[1]:
#             bad_rulse[bags[0]] = []
#         else:
#             bad_rulse[bags[0]] = [bag.split(' ', 1)[1] for bag in bags[1:]]
        
#         print([bag.split(' ', 1)[1] for bag in bags[1:]])
        
#         print(line.strip())

# result_set = set()
# looking_for = [searched_for]
# while len(looking_for) > 0:
#     new_results = set()
#     for bag in looking_for:
#         for rule in bad_rulse.keys():
#             if bad_rulse[rule].count(bag):
#                 new_results.add(rule)
#     result_set = result_set.union(new_results)
#     looking_for = list(new_results)
#     new_results = set()


# print(result_set)
# print(len(result_set))

def bagsInsideThis(key, bag_rules):
    inside_of_bag = bag_rules[key]
    if len(inside_of_bag) == 0:
        return 0
    else:
        result = 0
        for bag in inside_of_bag:
            amount_of_bags = int(bag.split(' ', 1)[0])
            name_of_bags = bag.split(' ', 1)[1]
            result += amount_of_bags + (amount_of_bags * bagsInsideThis(name_of_bags, bag_rules))
    return result
regex = re.compile(' contain |, ')

searched_for = 'shiny gold bag'
no_bag = 'no other bag'
bag_rulse = dict()

with open('data/day7.txt') as reader:
    for line in reader.readlines():
        bags = regex.split(line.strip('.\n').replace('bags', 'bag'))
        if no_bag == bags[1]:
            bag_rulse[bags[0]] = []
        else:
            bag_rulse[bags[0]] = [bag for bag in bags[1:]]
        
        # print([bag.split(' ', 1)[1] for bag in bags[1:]])


# print(bag_rulse)
print(bagsInsideThis(searched_for, bag_rulse))
# result_set = set()
# looking_for = [searched_for]
# while len(looking_for) > 0:
#     new_results = set()
#     for bag in looking_for:
        

#         for rule in bad_rulse.keys():
#             if rule == bag:
                
#             if bad_rulse[rule].count(bag):
#                 new_results.add(rule)
#     result_set = result_set.union(new_results)
#     looking_for = list(new_results)
#     new_results = set()


# print(result_set)
# print(len(result_set))
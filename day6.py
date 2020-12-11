from functools import reduce
import re

only_letters = re.compile("[^a-z]+")
# re.sub(r'[a-z]+', '', s)
# ## Part One
unique_chars = 0
chars_in_all_persons = 0
with open('data/day6.txt') as reader:
    groups = reader.read().split('\n\n')
    for group in groups:
        answer_set = None
        for person in group.split('\n'):
            if (answer_set is None):
                answer_set = {char for char in person.strip()} 
            else:
                answer_set = answer_set.intersection({char for char in person.strip()})
        unique_chars += len({char for char in only_letters.sub('', group)})
        chars_in_all_persons += len(answer_set)
        
        # print('group', len({char for char in only_letters.sub('',group)}))

print(chars_in_all_persons)
print(unique_chars)
import itertools
import re

rule_rows = True
messages = []
resolved_rules = {}
derived_rules = {}

with open('data/day19.txt') as data:
    for line in data.readlines():
        line = line.strip()
        if line == '':
            rule_rows = False
            continue
        if rule_rows:
            nr, rule = line.split(': ')
            letter = re.match('\"(\w)\"', rule)
            if not letter is None:
                resolved_rules[nr] = [letter.groups()[0]]
            else:
                arr = []
                for sub in rule.split(' | '):
                    arr.append(sub.split(' '))
                derived_rules[nr] = arr
        else:
            messages.append(line)

        
print(resolved_rules)
print(derived_rules)
while len(derived_rules) > 0:
    keys = list(derived_rules.keys())
    for key in keys:
        rules_set = set().union(*(set(l) for l in derived_rules[key]))
        if rules_set.issubset(set(resolved_rules.keys())):
            new_resolved_rules = []
            for rule in derived_rules[key]:
                for permuation in itertools.product(*(resolved_rules[i] for i in rule)):
                    new_resolved_rules.append(''.join(permuation))
            
            resolved_rules[key] = new_resolved_rules
            del derived_rules[key]


print(len(set(messages) & set(resolved_rules['0'])))

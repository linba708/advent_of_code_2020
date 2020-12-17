import functools

def handle_rules(new, existing):
    name, valid_ranges = new.split(': ')
    valid_numbers = []
    for r in valid_ranges.split(' or '):
        low, high = r.split('-')
        new_range = list(range(int(low), int(high) + 1))
        valid_numbers += new_range
    existing[name] = valid_numbers
    return set(valid_numbers)


input_part = 'rules'
#read data
rules = {}
valid_numbers = set()
found_invalid = []
your_ticket = []
valid_tickets = []
with open('data/day16.txt') as reader:
    for line in reader.readlines():
        line = line.strip()
        if(len(line) == 0):
            continue

        if line == 'your ticket:' or line == 'nearby tickets:':
            input_part = line
            continue
        
        if input_part == 'rules':
            valid_numbers = handle_rules(line, rules).union(valid_numbers)

        elif input_part == 'nearby tickets:':
            #count not valid tickets
            ticket = [int(n) for n in line.split(',')]
            new_invalid = list(set(ticket) - valid_numbers)
            found_invalid += new_invalid
            if len(new_invalid) == 0:
                if len(valid_tickets) == 0:
                    valid_tickets = [[n] for n in ticket]
                else:
                    for i, n in enumerate(ticket):
                        valid_tickets[i].append(n)

        elif input_part == 'your ticket:':
            # handle your ticket
            print('your ticket', line)
            your_ticket = [int(n) for n in line.split(',')]
# print(rules)

print('part one', functools.reduce(lambda a,b: a + b, found_invalid))


fields = []
for i,col in enumerate(valid_tickets):
    valid_fields = (i,[])
    for rule, valid in rules.items():
        if set(col).issubset(set(valid)):
            valid_fields[1].append(rule)
    fields.append(valid_fields)

fields.sort(key=lambda e: len(e[1]))            


ordered_fields = []
for f in fields:
    for k in f[1]:
        if k in rules:
            ordered_fields.append((f[0], k))
            del rules[k]
            break

ordered_fields.sort(key=lambda t: t[0])            
result = 1
for i,j in zip(ordered_fields, your_ticket):
    print(i[1], j)
    if i[1].startswith('departure'):
        result *= j

print(zip(ordered_fields, your_ticket))
print(result)



# del d[key]
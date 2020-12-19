
#part one
def eval_list(expressions, acc):
    last_operator = ''
    i = 0
    while i < len(expressions):
        e = expressions[i]
        if e == '(':
            j,e = eval_list(expressions[i +1:], 0)
            i += j
        elif e == ')':
            return (i + 1), acc
        if e in ('*', '+'):
            last_operator = e
        elif last_operator == '*':
            acc *= int(e)
        elif last_operator == '+':
            acc += int(e)
        else:
            acc = int(e)
        i += 1
    return i, acc


def eval_list_advance(expressions, acc):
    last_operator = ''
    # print(expressions)
    i = 0
    while i < len(expressions):
        e = expressions[i]
        if e == '(':
            j,e = eval_list(expressions[i +1:], 0)
            i += j
            # print('incremented', i, e )
        elif e == ')':
            # print('returning', acc)
            return (i + 1), acc
        # print(acc, last_operator)
        if e in ('*', '+'):
            last_operator = e
        elif last_operator == '*':
            acc *= int(e)
        elif last_operator == '+':
            acc += int(e)
        else:
            acc = int(e)
        i += 1
    return i, acc



results = 0
with open('data/day18.txt') as data:
    for y, line in enumerate(data.readlines()):
        list = line.strip().replace('(', '( ').replace(')', ' )').split(' ')
        _,result = eval_list(list, 0)
        results += result
        print('result',result)
        
print(results)


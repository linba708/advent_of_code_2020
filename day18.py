import functools

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


def eval_list_advance(expressions, result_list):
    last_operator = ''
    # print(expressions)
    i = 0
    last_number = 0
    while i < len(expressions):
        e = expressions[i]
        if e == '(':
            j,e = eval_list_advance(expressions[i +1:], [])
            i += j
            # print('incremented', i, e )
        elif e == ')':
            result_list.append(last_number)
            # print('returning', result_list)
            return (i + 1), functools.reduce(lambda a,b: a*b, result_list)
        # print(result_list, last_number,last_operator, e)
        if e == '+':
            last_operator = e
        elif e == '*':
            last_operator = e
            result_list.append(last_number)
        elif last_operator == '*':
            last_number = int(e)
        elif last_operator == '+':
            last_number += int(e)
        else:
            last_number = int(e)
        i += 1
        if i == len(expressions):
            result_list.append(last_number)
    return i, functools.reduce(lambda a,b: a*b, result_list)



results = 0
with open('data/day18.txt') as data:
    for y, line in enumerate(data.readlines()):
        list = line.strip().replace('(', '( ').replace(')', ' )').split(' ')
        _,result = eval_list_advance(list, [])
        results += result
        print('result',result)
        
print(results)


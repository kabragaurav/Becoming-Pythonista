def switch_case(x, operator, y):
    return {
        '+' : lambda : x+y,
        '-' : lambda : x-y
        }.get(operator, lambda : 'Operator not found')()

print(switch_case(1, '+', 2))
print(switch_case(1, '-', 2))
print(switch_case(1, '*', 2))

'''
Equivalent if-else will be

def if_else(x, operator, y):
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y
    return 'Operator not found'
'''


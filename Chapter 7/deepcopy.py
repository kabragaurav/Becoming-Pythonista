# deep copy example
'''
You can also write
from copy import *
But wildcard characters like * are not recommended since they make vague what are you exactly importing
'''
import copy
ls = [
    [1],
    ['A','Z']
    ]


deep = copy.deepcopy(ls)

print("deep = ", deep)
#change ls
ls[0] = [2]
print(ls, deep)
ls[1][0] = 'a'
print(ls, deep)

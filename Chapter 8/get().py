dc = {
    'one' : 'uni',
    'two' : 'bi'
    }

'''
Uncommenting below line throws error : KeyError: 'three'
'''
# print(dc['three'])

print(dc.get('three'))
print(dc.get('three', 'Key not found'))

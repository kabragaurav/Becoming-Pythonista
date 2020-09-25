'''
We want a list of cubes of even numbers from 1 to 10
'''

# Traditional way 
ls = []
for i in range(2, 11, 2):
    ls.append(i*i*i)
print(ls)

# Pythonic way

# way 1
ls = [x*x*x for x in range(2,11,2)]
print(ls)

# way 2
ls = [x*x*x for x in range(1,11) if x%2==0]
print(ls)

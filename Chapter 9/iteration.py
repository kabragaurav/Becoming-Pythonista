ls = [1,2,3]

# C-style

i = 0
# using for loop
for i in range(len(ls)):
    print(ls[i])

i = 0
# using while loop
while i < len(ls):
    print(ls[i])
    i += 1


# Using Python style

# printing item
for item in ls:
    print(item)
    
# printing item with index
for i, item in enumerate(ls):
    print(i, item)

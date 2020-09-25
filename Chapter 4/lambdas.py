ls = [1,2,3,4,5]

# Traditional way of adding all items of list
sum = 0
for _ in ls:
    sum += _
print("Sum is ", sum)

# Single line way to do it
from functools import reduce
print("Sum is ", reduce(lambda x,y : x+y, ls))

# if you want to break it down:
adder = lambda x,y : x+y           # x,y are arguments and x+y is returned value
sum = reduce(adder, ls)
print(sum)


# Example of lambda with filter()
# Note we use list() constructor to create list out of filter object returned by filter()
print("Odd numbers in ls are ", list(filter(lambda x: x%2!=0, ls)))


#Example using map()

print("Adding 1 to each member of list : ", list(map(lambda x: x+1, ls)))
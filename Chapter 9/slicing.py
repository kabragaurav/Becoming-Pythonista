ls = [1,2,3]

# print all items
print(ls)
print(ls[::])

# print last item
print(ls[-1])

# print items from index [1,3)
print(ls[1:3])

# print REVERSED list
print(ls[::-1])         # original list if unaffected

# clearning list
del ls[::]              #Same as del ls[:] or ls.clear()
print(ls)

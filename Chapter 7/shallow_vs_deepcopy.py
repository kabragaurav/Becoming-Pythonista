# shallow copy example

ls = [
    [1],
    ['A','Z']
    ]

sh = list(ls)

print("sh = ", sh)
#change ls
ls[0] = [2]
print(ls, sh)
ls[1][0] = 'a'
print(ls, sh)


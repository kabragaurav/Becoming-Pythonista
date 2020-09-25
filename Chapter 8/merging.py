dc1 = {'a' : 1}
dc2 = {'b' : 2}

# using naive approach
dc3 = dict()
for key, value in dc1.items():
    dc3[key] = value
for key, value in dc2.items():
    dc3[key] = value
print("Merged dict = ",dc3)

# using update()
dc4 = dict()
dc4.update(dc1)
dc4.update(dc2)
print("Merged dict = ",dc4)

# using **
dc5 = dict(**dc1, **dc2)
print("Merged dict = ",dc5)

dc = {
    'a' : 26,
    's' : 31,
    'd' : 15,
    'f' : 12
    }

print(dc)
# sort based on keys 
print(sorted(dc.items()))
# sort based on keys in descending fashion
print(sorted(dc.items(), reverse=True))
# sort based on values
print(sorted(dc.items(), key=lambda x : x[1]))

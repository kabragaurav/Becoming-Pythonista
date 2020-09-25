ls1 = [1,2]
ls2 = ls1

print("ls1 == ls2 : ", ls1 == ls2)  # == checks if ls1 and ls2 are identical,i.e., have same content
print("ls1 is ls2 : ", ls1 is ls2)  # is checks if ls1 and ls2 are identical AND point to same object 


ls3 = list(ls1)
print("ls1 == ls3 : ", ls1 == ls3)
print("ls1 is ls3 : ", ls1 is ls3)

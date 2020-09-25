class A:
    count = 0

    def __init__(self):
        self.count = A.count
        A.count += 1

a1 = A()
a2 = A()

print("Total instaces of class A are ",A.count)
print("Create number :",a1.count)
print("Create number :",a2.count)
        

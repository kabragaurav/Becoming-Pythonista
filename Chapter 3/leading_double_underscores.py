class A:
    def __init__(self):
        self.__foo = 'A __foo'
        self.foo = 'A foo'

class B(A):
    def __init__(self):
        self.__foo = 'B __foo'
        self.foo = 'B foo'

a = A()
b = B()
print(a.foo, b.foo)
'''
If you uncomment below line, it throws error : AttributeError: 'A' object has no attribute '__foo'
This is due to name mangling
'''
# print(a.__foo, b.__foo)

# Proper way to access is :
print(a._A__foo, b._B__foo)


# print attributes on object a
# notice _A__foo
print(dir(a))

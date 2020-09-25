'''
Without __str__ and __repr__
Prints : <__main__.Person object at ...>
'''
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

p = Person('Tony', 'Stark')
print(p)

# -----------------------

'''
With __str__
Prints : Printing __str__ for Mark
'''
class Person3:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "Printing __str__ for {}".format(self.fname)
p3 = Person3('Mark', 'Ruffalo')
print(p3)

# ------------------------

'''
With __str__ and __repr__
Prints " Printing __str__ for Chris
'''
class Person2:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "Printing __str__ for {}".format(self.fname)
    def __repr__(self):
        return "Printing __repr__ for {}".format(self.fname)
p2 = Person2('Chris', 'Evans')
print(p2)

# ---------------------------

'''
With __repr__
Prints " Printing __repr__ for Tom
'''
class Person4:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return "Printing __repr__ for {}".format(self.fname)
p4 = Person4('Tom', 'Holland')
print(p4)


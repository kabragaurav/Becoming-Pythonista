class Shape:
    def sayHi(self):
        print("Say Hi")
        
    def describe(self):
        print("I am Shape")


class Rectangle(Shape):
    def describe(self):
        print("I am Rectangle")


class Circle(Shape):
    def describe(self):
        print("I am Circle")

s = Shape()
r = Rectangle()
c = Circle()

s.describe()
r.describe()
c.describe()

s.sayHi()
r.sayHi()
c.sayHi()


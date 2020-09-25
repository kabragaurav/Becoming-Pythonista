# Let us override + operator

class Account:

    def __init__(self, amount):
        self.amount = amount
    # If you remove below method then
    # Following error will be thrown
    # TypeError: unsupported operand type(s) for +: 'Account' and 'Account'
    def __add__(self, other):
        return self.amount + other.amount


emilia = Account(9000)
kit = Account(8000)

print(emilia+kit)

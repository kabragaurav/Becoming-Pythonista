
# kwargs stands for key-word arguments...meaning (key,value) as in dictionary
def foo(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)
    print("------x--------------x-------------")

foo("My name is Anthony")  # works
foo("My name is Anthony", "My age is 23")
foo("My name is Anthony", "My age is 23", occupation='Software enginner', language='Python') # also works

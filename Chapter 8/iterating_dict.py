attendance_register = {
    101 : 'Alice',
    102 : 'Bob'
    }

# items() gives key, value pairs
for rollno, name in attendance_register.items():
    print(rollno, name)

# keys() gives keys
for rollno in attendance_register.keys():
    print(rollno)

# values() gives values in dict
for name in attendance_register.values():
    print(name)

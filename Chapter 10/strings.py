string = ' A solid foundation of string methods  '

print("Length, i.e., number of characters in string : ", len(string))
print('From 5th character onwards :', string[5:])
print('Membership test : ', 'lid found' in string)

print(string.upper())               # returns new string with all upper case letters
print(string.capitalize())          # returns new string with first letter case switched
print(string.lstrip())              # returns new string with removed extra newline, tab or spaces in left
print(string.strip())               # returns new string with removed extra newline, tab or spaces in left as well as right
print(string.startswith(' '))       # checks if string starts with provided substring
print(string.count('o'))            # how many times given character appears (case-sensitive)
print(string.find('id'))            # returns index of first occurrence of substring in entire string

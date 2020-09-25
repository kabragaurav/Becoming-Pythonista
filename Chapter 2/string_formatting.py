lang = 'Python'
future = 'future'

# Using format()

# Without using index
print('{} is future'.format(lang))
# Using index
print('{0} is future'.format(lang))
print('{} is {}'.format(lang, future))
print('{0} is {1}'.format(lang, future))
print('{1} is {0}'.format(future, lang))
# Using custom index names
print('{lang_name} is {tense}'.format(lang_name=lang, tense=future))



# Using f-strings

print(f'{lang} is {future}')

# We can evaluate something
print(f'1+2 is {1+2}')

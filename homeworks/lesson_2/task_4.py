string = input('Enter string: ')
print('String as list:')
string_list = string.split(sep=' ')
count = 1
for item in string_list:
    print(f'{count} {item[0:10]}')
    count += 1


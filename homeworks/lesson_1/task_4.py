
number = int(input('Enter number (integer): '))
if number > 0:
    max_digit = number % 10
    while number != 0:
        number = number // 10
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
else:
    print('Wrong data!!!')
print(f'The biggest digit is {max_digit}')

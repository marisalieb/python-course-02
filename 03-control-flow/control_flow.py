
print('  ')

for numberrr in range(1, 6, 2):
    print('attempt', numberrr + 1, (numberrr + 1) * '.')


print('  ')

successfully_send = True
for number in range(1, 4):
    print('attempt', number)
    if successfully_send:  # so if successfully send is True as specified above
        # the previous two lines will be executed every time the for loop runs, while the next two only if successfully_send is true
        print('Message successfully send.')
        break
else:  # this will only be executed if the loop completes without early termination, so only if it doesnt come to the break statement above
    print('attemted three times and failed')


number2 = 100.5
while number2 > 5:
    # on the first iteration its 100, then when teh next line is executed it's 100/2, etc.
    print(number2)
    number2 //= 2  # same as number2 = number2 //2


command = ''  # you need the empty string here so python know what this variable is in the next line
while command.lower() != 'quit':  # continues until user types 'quit'
    command = input('> ')  # here is the user input stored in command
    # here the input is printed and will iterate again until quit
    print('Your command is:', command)

print('end.')

# alternative version with an infinite loop which gives the same result as above >

# here you dont need to define command as an empty string
while True:  # if you use true here you need a break statment otherwise it will continue forever
    command = input('> ')
    print('Your command is:', command)
    if command.lower() == 'quit':
        break

print('end.')

for even_number in range(1, 10):
    if even_number % 2 == 0:  # to check for even numbers check if the remainder of the division by 2 equals 0, also frage ob die gleichung aufgeht ohne rest also gleich 0
        print(even_number)


count = 0
for even_number in range(1, 10):
    if even_number % 2 == 0:  # to check for even numbers check if the remainder of the division by 2 equals 0, also frage ob die gleichung aufgeht ohne rest also gleich 0
        print(even_number)
        count += 1
print(f'We have {count} even numbers.')

print('  ')

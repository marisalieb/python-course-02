# CONTROL FLOW	


### comparison operators:
<, >, <=, >=, == (equal), != (not equal)

you can compare strings, the first letters in alphabet are considered smaller than the later ones


### conditional statements
like if statements, they are executed when Boolean condition is true so eg the print function specified afte the if statement is only executed if condition is met/true >
temperature = 35
if temperature > 30:
	print('is is warm')
print('done')
#you end the if block with removing the indentation, so 'done' isn't part of the if statement anymore and will just be printed afterwards

elif is an alterative conditional statement

else is executed if neither if nor elif are true, it doesn't have specific conditions



### ternary operators
instead of if and else statements you can write ternary operatorslike so >
age = 22
message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)

they are also known as conditional expressions, theses operators evaluate something based on a condition being true or not



### logical operators
used to model more complex conditions: and, or, not(the not operator inverses the value of the Boolean, so use like this > if not high_income: ...) 
>
high_income = True
good_credit = True

if high_income and good_credit:   #here high_income is a Boolean so you don't need == True, it is redundant
	print('Eligible')
else:
	print('not eligble')

to combine differnt operators do this > if (high_income or good_credit) and not student_status: ...



### Short circuit evaluation
boolean operators like this (> if high_income and good_credit and not student_status: ...
) are short circuit, meaning when the python interpreter wants to evaluate this expression it starts with the first argument, if the first one is true it continues the evaluation; if one of them is false then the evaluation stops 


### Chaining comparison operators
same as in math you can chain comparison operators like this >
#age should be between 18 and 65
age = 22
if 18 <= age <= 65: ...




### Loops
loops are used to create repetition without having to repeat code in your program, what is indented after the for loop is all the statements that eill be repeated in that loop 

for loop; it needs a variable specifically an integer (can be called whatever) and then a range(), the integer will have a different value in each iteration of the for loop so it will start at 0 (if you dont specifiy the range differently) and go to the end of the loop
range shoul look like this > range(3) or range(1, 3) or range(1, 10, 2) is you want the range in steps of two

to jump out of the loop use a break statement or else: ...


nested loops can look like this >
for x in range(5): # this is the outer loop
	for y in range(3): # this is the inner loop
		print(f'({x}, {y})')
#on the first iteration of the outer loop the inner loop will be executed as many times as specified, in the second iteration of the inner loop the outer loop is still on it's first iteration and so forth; on the second iteration of the outer loop this will continue 



### Iterables
type() gives you the type of the number or object, 5 would be integer, range(5) would be range and so on; 
the range() function is iterable the range function returns a range object that is iterable(can be iterated over), like in a for loop where each iteration will have a differently valued variable (like x, will be differnt in each iteration)
strings are also iterable, if you iterate over a string with a for loop it will return each character of the string in an individual line
lists are iterable too, eg. [1, 2, 3, 4] each item in the list will be iterated over




### While loop
used to repeat something as long as something is True, the variable in the while loop is an integer if it is defined as one in the variable, can also be a float etc though
Example >
command = ''
while command.lower() != 'quit':  # continues until user types 'quit'
    command = input('> ')  # here is the user input stored in command
    # here the input is printed and will iterate again until quit
    print('Your command is:', command)
print('end.')





### Infinite Loops
will run forever unless broken, eg with a break statement >
#alternative version with an infinite loop which gives the same result as above >

#here you dont need to define command as an empty string
while True: #if you use true here you need a break statment otherwise it will continue forever
    command = input('> ')  
    print('Your command is:', command)
    if command.lower() == 'quit':
        break

print('end.')
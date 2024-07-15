## all notes (up to 08 modules until i started sorting them better)





#
#
#
#





 # Primitive Types
 
 
calling a function means executing it
- linting: shows you the problem with your code with red squiggly lines under your code, cntrl + shift + m gives you the Problems tab
- command palette: ctrl + sht + p 
- format code with autopep8 extention, it automatically fixes any formatting errors
 


python language:  specification that defines a set of rules and grammar to write python code
python implementation: program that understand those rules and can execute python code, cpython (written in C) is the default implementation


c compliler used to convert C into machine code so the computer can understand what we wrote


variables are used to store data in the computers memory, like count = 100


whats kinds of data can you store in memory? first look at built in or primitive types, they can be numbers(integer, float or floating point number), Booleans (check casing so True or False), strings


variable names should be descriptive, only in lower case and separated by _  


triple quotes are used to format a long string. text should be in its own line or lines between the start and end triple quotes 


function is a reuseable piece of code that carries out a task, like a button of a remote, like len for the length or charater number of a string (important that it's actually a string), then () to say that we are now using this function, some functions use additional data also called arguments and theses are then in put into those functions


if you want to access a specific character, use the [], this > 
students = 'hundred'
print(students[0])
#would print h

use -1 to access the last number, especially important if you don't know how many characters there are in the string

slice strings with start and end index like this [0:4], if you print this it would return the first 4 chacters of that string in a new string, the character at the end index is not included, if you do [0:] still will return the whole string in a new string since you didn't specify the end, same if you leave out start index it will just start at 0, if you leave out both start and end index like this [:] it will return a copy of the original string

escape character \ this is used to escape the character afterwards
escape sequence would be this for example \", \',\\,\n for a new line


formatted string like f'' or f"" or F'' or F"" , it doesn't have a constant value like a normal string (like name = 'Marisa', which does have a constant value), it is an expression that will be evaluated at run time, you use {} to print the value of that variable, you can put any valued expression between {} like you could put the len() function in to {} or an expression like (2 + 5)


functions behind a varable with a dot are called mathods like course.islower()

everything in python is an object and objects have functions we call methods that we can access using the . notation, the original object isn't changed by the method if you call it again without that method

#### some useful methods:
.upper() to convert into uppercase
.lower()
.title() to capitalise first letters of a word
.strip() to trim any white space at start or end of string, useful if you get input from user
.lstrip for left strip
.rstrip for right strip or end of string
.find() to find the index (or start character number) of whatever is passed as argument in ('') in your string, its case sensitive and if it cant find it in the string it will say -1
.replace('x', 'y') will replace all x with y in your string

in and not in: 'x' in object (like: 'code' in course): to check for the existence of character or sequence of characters, check if x is in the string stored in object, returns a boolean value; same with not in


numbers, normal woring +-*/ but if you want an integer from a / operation use //, then there is % or modulus which is the remainder of a division and ** which is exponent, augemented assignment operator like x += 2 instead of writing x = x + 2


built in functions to work with numbers:
round(3.2) # output 3
abs(-2.4) for absolute value of a number #returns 2.4

for more complex functions use the math module, a module is like a separate file with some python code, math in this program is an object so you can use . notation to see all the functions or more acurately all the methods available in this object; the complete list of math module methods can be found if you search for python 3 math module and go to docs
so >
math.ceil() to get the ceiling of a number like math.ceil(2.2) would return 3


useful built in functions
input()
type(x) gives you the type of date of x like integer, string, etc

two objects cant be concatenated if they are of different types so this >
x = input('x: ')
y = x + 1
#output would look like '1' + 1, so they are different types (x is a string) so you need to convert them

useful functions for this:
int(x)
float(x)
bool(x)
str(x) for string

important for boolean , there is a concept of truthy and falsy values in python. these are value that are not exactely a boolean true or false but they can be interpreted as a boolean true or false
falsy:
'' empty strings
0 number zero
None, the object None represents the absence of a value















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















# Functions:
Eg: print(), round(), etc.

to write your own functions is important to break up your code into smaller, more reuseable chunks of code and maybe even different files so it'll be easier to read later

start with def (this is the define keyword) then give the function a name (eg greet, should be meaningful, lower case and use underscore for multiple words) and () right after and :
>
def greet():
	print('…')


greet()
#add two empty lines after defining a function (before calling the function)


when you define a function, in between the () you can list the parameters like first_name, etc.; then when you call that function you need to supply values for those parameters or also called arguments; like so >
def greet(first_name, last_name):
    print('hi')


greet('Marisa', 'Lieb') # 'Marisa' and 'Lieb' are the arguments for this function while first_name and last_name above are the parameters
#this way the function is reusable since you can pass different parameters


parameter: is the input you define for your function
argument: is the actual value for a given parameter


there are two different types of functions
1. ones that perform a task, something like print() as it's printing on the terminal
2. ones that calculate and return a value, eg round() as it calculates and returns a value; these are more likely to be reusable


return is used to return a value from a statement

open(); built in function to write message to a file


use keyword arguments to make code more readable like here >
print(increment(number=2, by=1)) #here number and by are keyword arguments, they arent neccessary there but make it more readable for others



4.5
all the parameters defined for a function are required by default, so optional parameters have to come afterwards 



*arguments
useful when you want to create a function that takes a variable number of arguments

**arguments
when you use **arguments you can pass multiple keyvalue pairs or keyword arguments to a function and python will automatically package them into a dictionary



scope which refers to the region of the code where a variable is defined so >
def greet(name):
	message = 'a' # the scope of this message and name variables is the greet function since the variables only exist inside of this function 

so name and message are local variables, they only exist in this function 
global variables are accessible anywhere in the file so the scope of that variable is file it is in, global variable stay in memory longer since they might be used anywhere, so don't use to much so much better to create functions with parameters and local variables; you cant update a global variable with a local variable in a function, it will return to it's globale variable value; it is a bad practice to modify global variables in a function with the 'global' function 


### Debugging:
f9 inserts a break point
... see video 


### windows shortcuts:
press Pos1 to get to the beginning of the line
press Ende to get to the end of the line
press strg + pos1 to get to beginning of file
press strg + Ende to get to the end of the file
press ALt + up/down arrows to move a selected section up or down (instead of copy paste)
press shift + Alt + down arrow to duplicate a selected line
press strg + # to convert selected lines into a comment or revert back



#### fizz buzz exercise:
function fizz_buzz takes an input and depending on the input we give it, it returns different results 
rules:
if input is divisible by 3 return fizz 
by 5 return buzz
by 3 and 5 return fizzbuzz 
any other number it will just return that number 














# Data stuctures:

lists [], there can be objects of any types inside like strings, numbers, Booleans or even lists themselves 

thers is also the list function list() which takes an iterable as a parameter, so you can pass any iterable her and convert it to a list like this > list(range(1:20)), like range() or strings are also iterable 

 once you have a list you can use len() to get the number of items in that list

use []  to access an item in a list like this > letters[2] #this would give you the third item on the list
you can also use [] to modify items in the list like this > letters[-1] = 'a'
or to slice it like this [1:3] # this would give you items two and 3
when slicing a string you can also pass a step, like return every second element in the list like this > numbers[1:15:2] ; use [::-1] to return the list in reverse order

### list unpacking:
if you want to get individual item from the list and assign them variables do this > 
numbers = [1,2,3]
first = numbers[0] etc.
but the cleaner version is list unpacking:
first, second, third = numbers
important to have the same number of variables as items on the list
if you only need the first two fe do this >
first, second, *other = numbers or first, *other, last = numbers #everything else here will be stored in a separate list called other, the * here is basically packing the items back into another list
when you prefix a parameter with * then python get all the arbitrary argumetns and pack them into a list (see *args )


loop over lists 
example >
letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)

if you want to get the index of each item use enumerate function, this will return an enumerate object which is iterable, in each iteration this enumerate object will give you a tuple 
>
letters = ['a', 'b', 'c']
for letter in enumerate(letters): #returns a tuple with the first item being the indey and the second is the item of that index
    print(letter[0], letter[1]) #will give you the first and second item of the tuple


add or remove items from a list:
use the append method to add item at the end of a list
use insert method to add at beginning or middle
use pop method with empty () to remove items at the end of the list
use pop method with index in () to remove items at that index of the list
use remove mothod to remove without knowing the index
use clear method to remove all the items on the list 
you can also use the del or delete statement to remove a range of items based on index


finding items or index of object in a list
use the index method  >
letters = ['a', 'b', 'c']
print(letters.index('a'))

use in operator to check if item is even in the list >
letters = ['a', 'b', 'c']
if 'd' in letters:
    print(letters.index('d'))

use count method to return the number of appearance of the given item in that list


### Sorting lists:

use sort method with empty () to sort numbers in a list in ascending order 
the sort method takes two parameters, key and reverse, and it will modify the original list
use sort method with a keyword argument in the () and set to true to sort numbers in a list in descending order >
numbers.sort(reverse=True)

sorted() function, takes any iterable and will sort that by returning a new list which is sorted, it doesn't modify the original list, same here with the reverse argument set to true wil reverse the order of the list


sorting complex objects like a list of tuples , you need to define a function that python will use to sort the list
example > 
items = [
    ('Product01', 10),
    ('Product02', 5),
    ('Product03', 14)
]

def sort_item(item):  # this function takes an item and should return a value that will be used for sorting
    # to sort by price
    return item[1]  # accessing the second item in the tuple

#here you need to pass the sorting function, dont call the function with (), just pass a reference to the function
#you can only use keyword arguments here so you need to specify the argument and set it to sort_item
items.sort(key=sort_item)
#now when it sorts the list it'll get each item and pass it to the sort_item function
print(items)

### Lambda function:
but a better way of doing all this ^ is the lambda function: it's a one line anonymous function that w can pass to other functions 
example >
items = [
    ('Product01', 10, 13),
    ('Product02', 5, 532),
    ('Product03', 14, 234)
]

#this is telling lambda we are defining lambda/anonymous function, afterwards add parameters:expression
items.sort(key=lambda item: item[2]) #sorted by third item in tuple
print(items)

to transform a list of tuples with eg a name and a price into a list with just the prices :
option 1, you transform your original list into a new list with just the prices with the help of an empty list   >  
items = [
    ('Product01', 10, 13),
    ('Product02', 5, 532),
    ('Product03', 14, 234)
]
prices = []
for item in items:
	prices.append(item[1])
print(prices)

option 2, map function:
map() takes a function and one or more iterables, so you could pass first the lambda and second the list of items, this map function will iterate over the list and will call the lambda function on each item of this iterable


##### filter functions:
takes two parameters, a function and an iterable, so it will apply this function on each item of this iterable and if the item matches some criteria it will return it
a filter object is iterable so you have to loop over it and can convert it to a list


### list comprehension:
an alternative and cleaner way to write map and filter functions, it is also more performant; you basically define a new list
basic syntax: [expression for item in items]
>
items2 = [
    ('Product01', 10),
    ('Product02', 5),
    ('Product03', 14)
]
prices2 = [item_y[1] for item_y in items2]
filtered2 = [item_z for item_z in items2 if item_z[1] >= 10]
if you print them you get list with only price or only the filtered items



#### Zip function:
while the map and filter function only takes one iterable list, if you want to combine two or more lists into a single combined list of tuples for example, use the zip function
example >
list1 = [1, 2, 3, 4]
list2 = [40, 30, 20, 10]

print(list(zip(list1, list2)))
#the returned  zip object is iterable so you can pass it to the list function to convert it to a list
#you dont have to pass a list in the zip function you can also pass a string
print(list(zip('asdf', 'qwer')))



### Stacks:
Lifo - last in first out; imagine a stack of books and the book on top of the pile

example browser windows opening new ones and closing them 
>
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
#remove last tiem like closing a window:
last = browsing_session.pop()
print(last)  # this prints what is removed
print(browsing_session)
#now to take the user to the item on top of the stack use negative index
print('redirect:', browsing_session[-1])

#if stack becomes empty you need to disable the back button, check with falsy values so if you apply the not operator to a falsy object like an empty list you get a boolean true
browsing_session.clear()
if not browsing_session:
    print('disable back button')


Queues
fifo - first in first out, like a real world queue 
a module is like a bucket with a bunch  of reusable code
for queues use a deque object like this >
#wrap empty list with a deque object, so call deque and pass the empty list as an argument
queue = deque([])
#deque object has similar methods to list objects
queue.append(2)
queue.append(4)
queue.append(6)
queue.popleft()  # to remove item from beginning of the list
print(queue)

if not queue: #to check if queue is empty
    print('empty')



### Tuple:
is like a read only list
use () instead of [] for lists, or leave out (), python will still see this as a tuple
use the tuple function tuple() to convert a list or a string or any other iterable into a tuple , the function takes any iterable and it will return a tuple like > tuple([1, 2, 3])
access individual items with an index like point[-1] or a range point[0:2]
unpack a tuple like this >  
point = (1, 2, 3)
x, y, z = point
use in operator to check for existance of an item > if 10 is in point: ...
but since tuples are inmutable/unchangeable you don't have methods to add or remove item, unlike with list so this would not work > point[0] = 10
so use tuples if you want to make sure you don't accidentally change anything about their content





### swapping variables:
basic version >
#swap x and y
z = x
x = y
y = z
#this works because of the order it is executed from top downwards 

better version >
x, y = y, x #here on the right side of equation you define a tuple , on the left you are unpacking it
#x, y = (11, 10)  so it is unpacking the tuple
this way you can define multiple variables on the same line like > a, b = 1, 2



### Arrays:
if you have a large list and are having performance issues due to it, replace the list with an array, but only then don't replace if not necessary
>
from array import array # module called array and in it there is a class called array
#now call array function, first parameter is a typecode which is a string of one character that determines the type of object in your array, here use 'i' for signed integer
#then as the second arguement you pass a list of integers, now you get an array 
numbers_array = array('i', [1,2,3])

look up typecodes python to choose one, like integers, etc.
in this array object, similar to lists, you have methods of adding new objects, removing ones:
append() append a number to the end of the list
insert() to insert a number at a specific index 
pop()
remove()
can access items by their index like numbers_array[0] 
unlike lists though the items here are typed so every object should be the same type, in this case integers since that is the typecode we used when we created the array



### Sets:
is another type of data structure
collection with no duplicates written in {}
set is also a function, set() 
so to remove duplicates from a list convert it to a set like this >
numbers = [1, 1, 2, 2, 3, 4]
uniques = set(numbers) # call the set function and pass the numbers list, if you print this now you will get only unique items and no duplicates in {1, 2, 3, 4}
similar to list you can add or remove item to a set or use len() to get the number of items in a set 

the special thing about sets are the mathematical operations >
numbers = [1, 1, 2, 2, 3, 4]
first = set(numbers)
second = {1, 5}

#get a union of two set with |, this will return a new set that includes all the items in either the first or second set, only uniques items
print(first | second)

#get intersection of two sets, so returns all the items that are in both sets:
print(first & second)

#difference between two sets:
print(first - second)

#symmetric difference, returns what is wither in the first or second set but not both:
print(first ^ second)

#check for the existence of an item in a set > 
if 1 in first:
	print('yes')

unlike lists, sets are unorders collections (of unique items) so they are not in sequence, so you can use indexing to access items, so if you need indexing use sets




### Dictionaries:
is another data structure, it is a collection of key value pairs so it is used to map a key to a value, only inmutable types can be keys so often it is strings or numbers while value can be any type

with the dict() function you pass one or more keyword arguments

you can get the value associtated with a key using an index but the index has to be the name of a key because dict are collections of keyvalue pairs you cannot access an item using a numeric index > point2['x']
or set it to a new value > point2['x'] = 10
add a new key 

if you use an invalid key like a non-existent one, you get a keyerror
so either check for existence of this key first Y
if 'a' in point2:
	print(point2['a'])

or use the get() method, so pass name of the key, and if it doesn't exist you get the result None > 	print(point2.get('a'))      ; or you can pass a default value as a second argument so if you dont have an item with the key 'a' then return 0 by default > print(point2.get('a', 0)

use delete stament to delete an item > del point2['x']

loop over dictionaries >
for key in point2:
	print(key, point2[key])
or >
for key, value in point2.items():
	print(key, value)
#this will result in tuples with the key and the value and then you can unpack it right there


syntactical difference between a set and a dictionary since they both use {}
in set you just have values inside {} so sets > {2, 3, 4, 5}
in dictionaries you have keyvalue pairs that are separated by a : so > {1: 'a', 2: 'r'}

#### dictionary comprehension
use comprehension expressions to create dictionary objects
while this  would be a set > values2 = {x * 2 for x in range(5)}
this would be a dictionary > values2 = {x: x * 2 for x in range(5)}
so it all depends on whether there is a keyvalue pair



### Generator objects (like a tuple comprehension expression)
use these if you have large data sets and you dont want to store too many values in memory and have more efficient code then uses a generator expression to create a generator object
they are iterable like lists and in each iteration they generate a new value so unlike lists they dont store all the values in memory but they generate the new value in each iteration 

size of generator objects >
from sys import getsizeof #from the sys module import function getsizeof
values4 = (x * 2 for x in range(100000))
print('generator object size:', getsizeof(values4)) 
#this returns how much memory the generator object takes like 200bytes of memory, a list of that size would take 800000 bytes 


### Unpacking operator:
useful for data structures like lists, etc. or any other iterable, you unpack an iterable so take individual values; use the unpacking operator to take out individual values in any iterable
use like this >
numbers1 = [1, 2, 3]
print(*numbers1)
print(1, 2, 3)
#the last two line are now the same though the unpacking opertor *, wihtout it there you would have the list returned as a list

with * the  individual elements will be passed as arbitrary arguments to the print function

* is also useful when creating lists and unpacking strings
values5 = [*range(5), *'hello']

values6 = list(range(5))
values5 = [*range(5)]
#values5 == values6

also used to add lists together > 
values7 = [*values5, *values6]
print(values7)


Unpack dictionaries:
use ** >
first_dict = {'x': 2}
second_dict = {'x': 5, 'y': 345} 
combined_dict = {**first_dict, **second_dict, 'r': 234}
print(combined_dict)

if you have multiple items with the same key the last value will be used




Pprint:
use 'from pprint import pprint' to import pretter print functions eg for dictionaries
to use it as print call pprint() instead of print() and add a keyword argument width=1, width determines the number of characters on each line and if it doesn't fit more than it add a line break, so it will print each pair on one line






# EXCEPTIONS:

handles exceptions with a try block so the program can continue even if there are any errors like invalid user input, so python will try to run everything in try but if there are any exceptions it will execute the code in the except clause but the program at least doesn't crash, if there are no exception the code wont be executed, like so >
try:
    age = int(input('Age: '))
except ValueError as exception:  # add an except clause; as exception is optional
    print('You didn\'t enter a valid number for your age.')
    print(exception)  # you wouldnt show this to user just here to see how it works
    print(type(exception))  # same here, dont show to user
else:  # this will only be executed if no excetption is thrown in the try block code, so if except isnt triggered
    print('No exceptions were thrown.')
print('Execution continues.')  # check if program still runs after valueerror <


if you have multiple except clauses and any exceptions are thrown then only the first except clause will be executed, the other except clauses will be ignored

if you use any other resources like files in your code you should release them if you are done using them, otherwise another program or process might not be able to open/use that file
so if you want to close that file or execute any functions at the end of the block both if exceptions are thrown or not then add a finally block

with statement:
instead of using finally for some objects you can use the with statement which automatically closes/releases resources at the end
use like this >
 try:
    with open('app.py') as file:  #file object that the open() returns
	print()
    age = int(input('Age: '))
    xfactor = 100 / age
except (ValueError, ZeroDivisionError): 
    print('You didn\'t enter a valid number for your age.')
else:
    print('No exceptions were thrown.') <

magic methods have __ in front of them, __enter and __exit are important for the with statement; when an object has theses two methods then that object supports context management protocol, which also means you can use the with statement with it

if you have multiple files you are using you can add files to the with statement and it will relase them all at the end >
 try:
    with open('app.py') as file, open('text.txt) as text_file: <


### Raising exceptions:
you can raise or throw exceptions yourself but it come at a cost when building scalable applications because it might lead to performance issues, so think twice about raising exceptions
you can look up which types of exceptions there are, google python 3 built in exceptions, sufficient for most cases but you can also built your own exception type 
example >
 #raise exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 10/age 

try:
    calculate_xfactor(-100)
except ValueError as error:
    print(error)
<

to calcutlate the execution time of some python code, use timeit
> 
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 10/age 

try:
    calculate_xfactor(-100)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None # none is an object which represents the absence of a value
    return 10/age 

xfacter = calculate_xfactor(-100)
if xfactor == None: #instead of handling an exception you can compare this xfactor with none
	pass 
"""

print('first code: ', timeit(code1, number=10000)) #first argument pass the py code, then keyword argument number set it to the number of times you want to execute this code, this returns the execution time of this code after 10000 repetitions
print('second code: ', timeit(code2, number=10000)) # result: code2 much faster
<

use a pass statement in the except statement, pass doesnt do anything which makes it faster but fixes it since the except block cant be empty 











# CLASSES:

class: is a blueprint for creating new objects, like you have a class for creating integer, one for creating booleans, lists, dicts, etc.; so every obect in python is created using a class which is a blueprint for creating new objects of that type

object: is an instance of a class

while variables and functions have lowercases names and you separate multiple words with _ , classes have uppercase ones and new words just use another uppercase letter without _ 

example >
#this is a blueprint for creating point objects:
class Point:  # in this block define all functions relating to Point, like drawing a point, removing, moving etc
    def draw(self):  # all functions in your class should have at least one parameter and by convention this parameter is called self
        print('draw')  # every Point object thst we create will have the draw method


point = Point()  # this returns a Point object that we assign to a variable and then this variable can call the draw method
point.draw() #executes draw() function so prints 'draw'
print(type(point))
#isinstance is useful function to check if an object is an instance of a given class, like is point an instance of Point
print(isinstance(point, Point))
<


### Constructor:
which is a special method/magic method that is called when we create a new point object, __init__(self), it is executed when we create a new object of this class, eg a new Point object

all methods defined in a class should have at least one parameter called self, optionally you can add more parameters for initialising a Point object like x and y; or you can define attributes later when you need them, they don't all have to be defined in the constructor; theyes attributes are instance attributes so they belong to Point instances/objects, every point object can have different values for these attributes

 self here is a reference to a current Point object, python by default supplies a value for the self parameter, you only need to define other parameters like x and y;

the point object can also have attributes which are like variables that include data about that object so like attributes like x and y,

 classes can have attributes and functions 

a class or an object bundles data and functions related to that data into one unit

class attributes are defined at class level (vs instance attributes), they are the ysame across all instances of a class, you can read them via class or object reference, if you change them they will be changed for all instances

### class vs instance methods:
class method, sometimes it is a factory method as in a factory for new objects so cerating new object; instance methods are applied to an instance 
class methods are defined  after the__init__, first parameter is cls (like self in init) for class by convention, here you are not working with a class object or instance but with the class; you need to decorate it (a way to extend the behaviour of a method or a function) with @classmethod




### magic methods:
check out 'a Guide to Pythons magic methods rafekettler'
magic methods are called automatically by python interpreter depending on how you use your objects and classes; like__init__ , __str__ and __repr__



### comparison:
by default the equality operator == compares the refernces or addresses of two objects in memory
so >
point = Point(1, 2)
other = Point(1, 2)
print(point == other) #returns false <

so instead use a comparison magic method like >
def  __eq__(self, other)
	return self.x == other.x and self.y == other.y #now if you print point == other it returns true

using the greater than method will also work for less than, python will figure that out automatically what to do with the < operator



performing arithmetic operations:
use numeric magic methods like __add__



### Making custom containers:
default container types are list, dictionaries, etc.
so custom ones can have more functions than the default ones
example >
#making custom containers, keep track of the number of tags ona blog

class TagCloud:  # this class represents a container, it supports various operations around containers
    def __init__(self):  # define a constructor
        self.tags = {}  # initialise the tags attribute to an empty dictionary
        # dictionary becasue it allows you to quickly get the muber of given tags

    def add(self, tag):  # method that takes a tag and check if the tag is already in dict, so either set it to 1 or increment it by 1
        # get method to get an item by this key and supply a default value if we dont have it , now get the count and increment it by one and set the value for the key
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # read the count of a tag
    def __getitem__(self, tag):  # the key is tag
        # if you dont have it return 0 by default so it doesnt thrown an error if you dont have the python tag
        return self.tags.get(tag.lower(), 0)

    # to set the count of a tag like this: cloud['python'] = 10
    def __setitem__(self, tag, count):  # takes 3 parameters: self, key, value:
        self.tags[tag.lower()] = count

    # get number of items in the TagCloud, implement len magic method
    def __len__(self):
        return len(self.tags)

    # make it iterable, implement iter
    def __iter__(self):
        # use built in function iter to get iterator object (an object that walks a container and gets one item at a time)
        return iter(self.tags)
        # this function returns an iterator object which gives you one item at a time in a for loop

cloud2 = TagCloud()
cloud2.add('python')
cloud2.add('python')
cloud2.add('python')
print(cloud2.tags)
cloud2['python']  # read the count of a tag using []

cloud = TagCloud()  # create object
len(cloud)  # because it is a container you can get the number of items in the container
#you can get an item by its key eg number of articles tagged with 'python'
cloud['python']
cloud['python'] = 10  # and you can set the number
for tag in cloud:  # iterate over the container
    print(tag)

<




### Private members: 
are used to make it harder to access things inside the class from the outside, it's still possible but tells the user not to; __ is used for them 
example >
#put cursor on the attribute tags and press f2 to rename it everywhere, rename it __tags to make it private or inaccessible from the outside, no __tags cant be accessed easily anymore, to still access it do this
#so every class or object has a property named __dict__ which is a dictionary that holds all the attributes in the class so print

print(cloud.__dict__) # returns {'_TagCloud__tags': {}} , which means your attribute is now called _TagCloud__tags and is an empty dict, python automatically renamed it and prefixed it with the name of the class

print(cloud._TagCloud__tags) # returns {}, so this still works now
<




### Properties:
is an object that sits infront of an attribute and allows us to get or set the value of that attribute

a property looks like a regular attribute from the outside but internally it has two methods that are called a getter and a setter

when defining properties you don't always have to define a getter and a setter, eg if you don't have the setter it will be read only so you can only set a value initially but not set it again later on

>
#how to ensure that the products dont have a negative price

#Solution 1, unpythonic meaning its not using pythons best practices
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value

product = Product(10)
print(product.get_price())


#Solution 2, but get_price and set_price are stil accesible from the outside so are polluting the object interface
class Product2:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value

    # define class attribute with ideal name called price, call the built in property function which takes 4 optional parameters (fget, fset, fdel, doc)
    price = property(get_price, set_price)
    # with the parameters you dont call them, you only pass a refernce to them, so when you call the built in property function with these arguments the function will return a property object, that porperty object will use the get_price function for reading the value of the price attribute
    # now you have the price property available when calling outside of class

product2 = Product2(20)
product2.price = -3 #you can set it but it throws exception when value is negative
print(product2.price)


#Solution 3,  get_price and set_price are not accesible from the outside
#instead of calling the property function to create a property object, apply a property decorator

class Product3:
    def __init__(self, price):
        self.price = price

    @property  # apply property decorator to this method and rename the mothod to the ideal name so price
    def price(self):  # so when the methods get called, a property object called price will automatically be created
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value


product3 = Product3(20)
product3.price = 6
print(product3.price)

<





### Inheritance:
if you don't want to repeat code in different classes which have the same methods, attributes

if one class inherits from another, an instance of the child class is also an instance of the parent class

move all the repeated methods in a parent class and then call it in () when defining a new class like so
 >
#Animal: Parent, base
#Mammal: child, sub
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eating')

class Mammal(Animal):
    def walk(self):
        print('walking')

class Fish(Animal):
    def swim(self):
        print('swimming')

lion = Mammal()
lion.eat()
print(lion.age)
<


there is a base class called object that is the base class for all classes in python so even our created parent class has a parent class (called object), create an empty object >  o = object() <
so each class in python has magic methods inherited from the object base class 

use issubclass so figure out if a class derives from another class > print(issubclass(Mammal, Animal)) <





### Method overriding:
if a constructor in the animal class should be used but is overridden by one in the mammal class, so a method in the base class is being replaced or overridden, to still get access to / extend the functions of animal like .age use the super() function > 
class Mammal(Animal):
    def __init__(self):
        # get access to the base class with super() so you can still use .age, and call __init__
        super().__init__()
        self.weight = 3
<




### Multi-level inheritance:
avoid too long hierarchies, limit to one or two levels; it might get too complex or simply wrong at some point like class Chicken(Bird) when the chicken cant really fly but Bird has a fly function



### Multiple inheritance:
means a child class can have multiple base classes (class Manager(Employee, Person)), can make problems though like if you have multiple base classes with the same named functions; if the base classes are small and have nothing in common multiple inheritance can work 



Abstract base classes: 
to provide some common code to its derivatives but not be able to instance, cant instantiate them
 
abc module, abstract base class
ABC class
abstractmethod function

to make a class abstract derive it from ABC class






### Polymorphism:
objects of different classes to be treated as objects of a common superclass
makes code more reusable, maintainable, scalable

>
class Dog:
    def make_sound(self):
        return 'Wuff'

class Cat:
    def make_sound(self):
        return 'Miau'

#function that takes any animal and calls the make_sound method without knowing what specific animal it is
def animal_sound(animal):
    print(animal.make_sound())

#instances of each animal
dog = Dog()
cat = Cat()

#call function with different animals
animal_sound(dog) 
animal_sound(cat)
<

make_sound behaves differently depending on the object (animal) its called on

its flexible as in you can add more animals without changing the function

decoupling: the function doesn't need to know the specifics of each animal class. it only knows that whatever object it gets will have the make_sound method, for this it is useful to have an abstract bas class with abstract methods so all sub classes have the same method names



### Duck typing:
emphasises what an object can do rather than what it is, it makes code more flexible and maintainable, allowing objects to be used interchangeably as long as they support the required interfaces (like same methods and functions across different classes)



### Extending built in types:
you can extend the functions of built in types like lists and strings, like eg the append method of a list you can define in a new class the append method and add to it's function




### Data classes:
classes are used to bundle data and functionality into one unit
there are classes that only have data but no methods or other behaviour

print(id()) returns the address of memory where an object is stored

named tuple instance:
use for classes that only have data, but note that they are immutable so you cant change them later you would have to define them again at that point so create a new point object with the same name but different values
named tuples here have attributes in the point object just like attributes in a class 
>
#return a named tuple and store it in variable Point which represents a type like a class, so you can call it to create a new point object

from collections import namedtuple

#first argumetn name for this new type we want to create, passing a string; second argument pass an array of attribute names, point object should have two attributes x and y
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)  # here you should pass keyword arguments
p2 = Point(x=1, y=2)
print(p1 == p2)
<

makes more clear because you use keyword arguments, also you don't need to use a magic method to compare objects














# MODULES

a modules is a file that contains some python code

to import a modules use  >
from 'name of the modules (without .py)' import 'name of the function, name of other function or * to import all' #press cntrl + space you can see all the objects defined in that modules and variables that python automatically creates

to import an entire modules as an object use > import 'name of the module' and then you can use . for its methods

### Packages:
if you want to import from a different folder add a __init__.py file
when you add this file here python will treat the folder as a package which is a container for one or more modules (a package is mapped to a directory and a module is mapped to a file)

if you use import then you can prefix the name of the file you want to import with the name of the package 
so > import excercises.py_exercise_fizz_buzz
to use any of the functions you need to prefix them the same way and then add the function ()

if you use from … import … then you can just use the functions without prefix 
>
#either
from excercises.py_exercise_fizz_buzz import *
#function() 

#or
from excercises import py_exercise_fizz_buzz
py_exercise_fizz_buzz.__dict__
<


### Sub-packages:
add more folders in a folder and then add the __init__.py file to make it a package, to access this now add the new folder name to the first folder name like this
> 
ecommerce = folder, shopping = subfolder, sales = module
from ecommerce.shopping import sales




#### Intra-package References:
importing from sibling packages (so packages in the same parent folder), use an absolute or relative import statement; recommended are absolute imports, only use relative ones if it get too long or complicated with absolute one

absolute import: from ecommerce.customers import contact

relative import: from ..customer import contact
. represents the current package
second . takes us one level up so now we are at ecommerce package level which has two sub packages



The dir() function:
is used to get the list of attributes and methods defined in an object

when you run print(dir(sales)) you get an array of strings which has all the attributes and methods defined in an object, so magic attributes automatically created and your own created functions

examples of some of the magic attributes automatically created:
__name__ gives you the name of the module fully qualified with the name of its packages
__package__ name of the package
__file__  address/path of the file and file system



ctrl + p to look up files


### Executing Modules as Scripts:
you can add to the __init__.py files and that code will be executed if you import it anywhere else and print the name for ecample like print('Sales initialised', __name__) at the top of the sales file

the name of the modules that starts your program (the one you currently run) is always __main__

so if you want to run modules as scripts add this after you define your functions in your currently used file >
if __name__ == '__main__':
	print('sales initialised.')
	calc_tax()
#with this code you can make the file useable as a script as well as a reusable module that you can import into another module, so when run directly the name of the file will be main and there you can have the initialisation code or call one of the existing functions in the module

#but if you import this module into another module this code in the if statement will not be executed because there the name of the module wont be main anymore since main will be the current file










watch again or as needed:
xargs 5.6
debugging
8.2 compiled python files
8.3 module search path

comments:
subtitles bad, one of many examples is that 'named tuple instance' is 'main couple instance' in the subtitles which is super confusing; or 'defined' is subtitled as 'to find'

sometime the solution come in the next video so if you go video by video you can spend ages trying to make your code work but not know why it doesn't when there is a bug in it that will be addressed in the next video, so my advice if you follow along but cant figure it out after five minutes move on, the solution might be presented to you there
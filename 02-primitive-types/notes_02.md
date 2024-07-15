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
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



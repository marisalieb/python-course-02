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

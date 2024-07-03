print('  \n   ')

# exceptions
try:
    age = int(input('Age: '))
except ValueError as exception:  # add an except clause; as exception is optional
    print('You didn\'t enter a valid number for your age.')
    print(exception)  # you wouldnt show this to user just here to see how it works
    print(type(exception))  # same here, dont show to user
else:  # this will only be executed if no excetption is thrown in the try block code, so if except isnt triggered
    print('No exceptions were thrown.')
print('Execution continues.')  # check if program still runs after valueerror


# handling different exceptions
try:
    file = open('app.py')
    age = int(input('Age: '))
    xfactor = 100 / age
except (ValueError, ZeroDivisionError):
    print('You didn\'t enter a valid number for your age.')
else:
    print('No exceptions were thrown.')
finally:  # executes both with or without exceptions to release external resources
    file.close()
print('Execution continues.')


# raise exceptions (only raise exceptions when really neccessary)
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 10/age


try:
    calculate_xfactor(-100)
except ValueError as error:
    print(error)

# what to do instead of raising exceptions, much faster execution time


def calculate_xfactor(age):
    if age <= 0:
        return None  # none is an object which represents the absence of a value
    return 10/age


xfacter = calculate_xfactor(-100)
if xfactor == None:  # instead of handling an exception you can compare this xfactor with none
    pass


print('  \n   ')

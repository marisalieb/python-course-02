print('  ')


def greet(first_name, last_name):
    print(f'hi {first_name} {last_name}')


greet('Marisa', 'Lieb')
# note here: (none is the return value of the greet function, in py all functions by default return the none value unless you specifically return a value
# none is the object that represent the absence of a value, so while print here as value none, it is still considered a function that carries out a task)


def get_greeting(name):
    return f'Hi {name}'


message = get_greeting('Marisa')
print(message)  # while this is more code it's is more versatile and reusable


def increment(number, by):  # you can give by a default value here like by=1, making it an optional parameter later when it is called
    # optional parameters have to come after default parameters
    return number + by


print(increment(number=2, by=1))  # here the increment function is called first
# and its returned value is stored in a value which is then passed to the print function


def multiply(*numbers):  # use plural here as parameter name to indicate it's a collection of arguments
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):  # the user argument here is a dictionary
    # using[] notation you can get the value of various keys in this dicitonary like this print(user['id])
    print(user)


save_user(id=3, name='mary', age=26)


def multiply(*numbers):  # use plural here as parameter name to indicate it's a collection of arguments
    total = 1
    for number in numbers:
        total *= number
    return total


print('start')
print(multiply(1, 2, 3))


print('  ')

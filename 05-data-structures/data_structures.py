from sys import getsizeof  # from the sys module import function getsizeof
from array import array  # module called array and in it there is a class called array
from collections import deque  # from collections module import deque class

print('  \n  ')


nums = [1, 2, 3, 9, 7, 4, 5, 6]
matrix = [[0, 1], [2, 3]]
zero = [0] * 100
combined = zero + nums
numbers = list(range(20))  # list function which takes an iterable as parameter
chars = list('Hello you')
print(len(chars))
print(nums[2])  # use [] here to acces an item on the list
print(numbers[1:15:2])  # the 2 here is the step can also be [::2]
print(numbers[::-1])

numbers = [1, 2, 3]
first, *other, last = numbers
print(last)

letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)

letters = ['a', 'b', 'c']
# items = (0, 'a')
# index, letter = items  # unpacking the items tuple
for index, letter in enumerate(letters):
    print(index, letter)
# if you need the index call enumerate() which will return an enumerate object which is iterable
# and in each iteration it will return a tuple and you can unpack that tuple in the for loop

letters.append('d')
letters.insert(1, 'ab')  # at position 1 so second ab will be added
letters.pop()
letters.pop(1)
# this will only remove the first b, if thre are more you have to loop over the list
letters.remove('b')

del letters[0]  # or use [:3] for a range of items to delete

print(letters)

letters = ['a', 'b', 'c']
if 'd' in letters:
    print(letters.index('d'))

print(letters.count('a'))


print(nums)
nums.sort(reverse=True)
print(nums)
print(sorted(nums))

items = [
    ('Product01', 10, 13),
    ('Product02', 5, 532),
    ('Product03', 14, 234)
]

# this is telling lambda we are defining lambda/anonymous function, afterwards add parameters:expression
items.sort(key=lambda item: item[2])  # sorted by third item in tuple
print(items)

items2 = [
    ('Product01', 10),
    ('Product02', 5),
    ('Product03', 14)
]

# first parameter to the map function is item and here we want to return the price of that item, the lambda functio here is item:item[1]
x = map(lambda item: item[1], items2)
# second argument of the map function pass the items list
for each_item in x:
    # if you just print variable x it will return a map object which is iterable so you have to iterate over it
    print(each_item)

# if you want to convert this map object into a list object, add a list() function before the map function and insert the map()
prices = list(map(lambda item: item[1], items2))
print(prices)


# filter the list and onyl get the items with price greater than 10
# the lambda function takes an item fil_item and returns a boolean value with this expression fil_item[1] >= 10 , which determines if this fil_item matches the criteria, if bool true the item will be returned
filtered = list(filter(lambda fil_item: fil_item[1] >= 10, items2))
print(filtered)

# map and filter functions in list comprehension:
prices2 = [item_y[1] for item_y in items2]
filtered2 = [item_z for item_z in items2 if item_z[1] >= 10]

print(prices2)
print(filtered2)

list1 = [1, 2, 3, 4]
list2 = [40, 30, 20, 10]

print(list(zip(list1, list2)))
# the returned  zip object is iterable so you can pass it to the list function to convert it to a list
# you dont have to pass a list in the zip function you can also pass a string
print(list(zip('asd', 'erfg')))


# stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# remove last tiem like closing a window:
last = browsing_session.pop()
print(last)  # this prints what is removed
print(browsing_session)
# now to take the user to the item on top of the stack use negative index
print('redirect:', browsing_session[-1])

# if stack becomes empty you need to disable the back button, check with falsy values so if you apply the not operator to a falsy object like an empty list you get a boolean true
browsing_session.clear()
if not browsing_session:
    print('disable back button')


# wrap empty list with a deque object, so call deque and pass the empty list as an argument
queue = deque([])
# deque object has similar methods to list objects
queue.append(2)
queue.append(4)
queue.append(6)
queue.popleft()  # to remove item from beginning of the list
print(queue)

if not queue:  # to check if queue is empty
    print('empty')


# now call array function, first parameter is a typecode which is a string of one character that determines the type of object in your array, here use 'i' for signed integer
# then as the second arguement you pass a list of integers, now you get an array
numbers_array = array('i', [1, 2, 3])


# sets
numbers = [1, 1, 2, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# get a union of two set with |, this will return a new set that includes all the items in either the first or second set, only uniques items
print(first | second)

# get intersection of two sets, so returns all the items that are in both sets:
print(first & second)

# difference between two sets:
print(first - second)

# symmetric difference, returns what is wither in the first or second set but not both:
print(first ^ second)


# Dictionaries
# dict can be empty or have one or more keyvalue pairs
point1 = {'x': 1, 'y': 2}
# here key is a string and value is an integer
point2 = dict(x=1, y=2)  # pass one or more keyword arguments

# point1 and point2 are the same thing just written differently
print(point2['x'])
point2['x'] = 10
# add a new key
point2['t'] = 3
# check for existence of a key with get
print(point2.get('a', 0))

# to loop over either:
for key in point2:
    print(key, point2[key])
# or:
for key, value in point2.items():
    print(key, value)


# list comprehension values1 == values2
values1 = []
for x in range(5):
    values1.append(x * 2)

values2 = [x * 2 for x in range(5)]  # like [expression for item in items]
# works the same with set just replace [] with {}
print(values2)

# dictionary comprehension
values3 = {x: x * 2 for x in range(5)}
print(values3)

# size of generator object
# from sys import getsizeof, this is up at the start of file
values4 = (x * 2 for x in range(100000))
print('generator object size:', getsizeof(values4))

values6 = list(range(5))
values5 = [*range(5)]  # could also be [*range(5), *'hello']
# values5 == values6

# to add lists together
values7 = [*values5, *values6]
print(values7)

# to combine dictionaries
first_dict = {'x': 2}
# if you have multiple items with the same key the last value will be used
second_dict = {'x': 5, 'y': 345}
combined_dict = {**first_dict, **second_dict, 'r': 234}
print(combined_dict)


print('  \n   ')

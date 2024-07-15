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
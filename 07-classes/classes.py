
from collections import namedtuple
from abc import ABC, abstractmethod


print('  \n   ')


# this is a blueprint for creating point objects:
class Point:  # in this block define all functions relating to Point, like drawing a point, removing, moving etc
    def draw(self):  # all functions in your class should have at least one parameter and by convention this parameter is called self
        print('draw')  # every Point object thst we create will have the draw method


point = Point()  # this returns a Point object that we assign to a variable and then this variable can call the draw method
point.draw()  # executes draw() function so prints 'draw'
print(type(point))
# isinstance is useful function to check if an object is an instance of a given class, like is point an instance of Point
print(isinstance(point, Point))

# constructor


class Point:
    default_colour = 'green'  # class attributes

    # instance attributes
    def __init__(self, x, y):  # x and y are parameters here
        self.x = x  # set the x attribute here
        self.y = y

    # class method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'Point ({self.x}, {self.y})')

    # string representation, otherwise .zero() will return unuseful information
    def __repr__(self):  # or __str__(self)
        return f'Point({self.x}, {self.y})'

    # comparison magic method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # greater than magic method
    def __gt__(self, other):
        return self.x > other.x or self.y > other.y

    # add magic method
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
point3 = Point(1, 2)
point.default_colour  # object reference
Point.default_colour  # class reference
point.t = 10  # you can define attributes later, doesnt have to be in the constructor
point.draw()

Point.default_colour = 'pink'  # reassigned class attribute
point.default_colour = 'purple'  # reassgined on instance level
print(Point.default_colour)
print(point.default_colour)

point2 = Point.zero()
print(point2)
print(point == point3)
print(point > point3)
print(point + point3)


# making custom containers, keep track of the number of tags ona blog
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
# you can get an item by its key eg number of articles tagged with 'python'
cloud['python']
cloud['python'] = 10  # and you can set the number
for tag in cloud:  # iterate over the container
    print(tag)


print('  \n   ')


# how to ensure that the products dont have a negative price

# Solution 1, unpythonic meaning its not using pythons best practices
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


# Solution 2, but get_price and set_price are stil accesible from the outside so are polluting the object interface
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
product2.price = 3  # you can set it but it throws exception when value is negative
print(product2.price)


# Solution 3,  get_price and set_price are not accesible from the outside
# instead of calling the property function to create a property object, apply a property decorator

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


print('  \n   ')

# Inheritance
# Animal: Parent, base
# Mammal: child, sub


class Animal:
    def __init__(self):
        self.age = 10

    def eat(self):
        print('eating')


class Mammal(Animal):
    def __init__(self):
        # get access to the base class with super() so you can still use .age, and call __init__
        super().__init__()  # if you have print statements or other functions in animal they will be carried out if you call mammal()
        self.weight = 300
        print('hi')

    def walk(self):
        print('walking')


class Fish(Animal):
    def swim(self):
        print('swimming')


lion = Mammal()  # just calling it still means all actions in this class in init will be carried out
lion.eat()
print(lion.age)
print(isinstance(lion, Animal))  # true because inheritance
print(issubclass(Mammal, Animal))
print(lion.age)
print(lion.weight)


# 7.17 example of inheritance: model the concept if a stream of data with difference of reading from file and network
# abstrace bas class because you shouldnt be able to create an instance of stream and have a common interface across sub classes

# from abc import ABC, abstractmethod
class InvalidOperationError:
    pass


class Stream(ABC):  # to make a class abstract derive it from ABC base class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream already opened.')
        self.open = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream already closed.')
        self.open = False

    @abstractmethod  # if yu create a new class with Stream as the base and you dont implement read to that new clas it will also be considered an abstract class
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Reading from file.')


class NetworkStream(Stream):
    def read(self):
        print('Reading from network.')


class MemoryStream(Stream):
    pass
    # like this this class wil be considered abstract becasue i didnt implement the read method here


stream = FileStream()
stream.read()


# Polymorphism

class Dog:
    def make_sound(self):
        return 'Wuff'


class Cat:
    def make_sound(self):
        return 'Miau'

# function that takes any animal and calls the make_sound method without knowing what specific animal it is


def animal_sound(animal):
    print(animal.make_sound())


# instances of each animal
dog = Dog()
cat = Cat()

# call function with different animals
animal_sound(dog)
animal_sound(cat)


# Data classes
# from collections import namedtuple
# return a named tuple and store it in variable Point which represents a type like a class, so <ou can call it to create a new point object
# first argumetn name for this new type we want to create, passing a string; second argument pass an array of attribute names, point object should have two attributes x and y
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)  # here you should pass keyword arguments
p2 = Point(x=1, y=2)
print(p1 == p2)

print('  \n   ')

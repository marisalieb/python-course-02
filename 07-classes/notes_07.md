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
## MODULES

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


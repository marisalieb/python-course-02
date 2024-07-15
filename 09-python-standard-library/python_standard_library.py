from pathlib import Path


print('  \n   ')

# paths
path = Path("08-modules/modules.py")
path.exists
path.is_file()
path.is_dir()
print(path.name)
path.stem  # without suffix
path.suffix
path.parent
path2 = path.with_name('file.txt')
path2 = path.with_suffix('.txt')
print(path2.absolute())


# directories
path = Path("08-modules")
print(path.iterdir())  # returns generator object
for p in path.iterdir():
    print(p)  # this returns all the file in that directory

# or list comprehension and filtering
paths = [p for p in path.iterdir()]
py_files = [p for p in path.glob('*.py')]  # non recurvive
# or recursive so all in that dir and child dirs
py_files_r = [p for p in path.rglob('*.py')]
print(py_files_r)


print('  \n   ')

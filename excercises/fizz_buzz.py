print('     ')
# fizz buzz exercise:
# function fizz_buzz takes an input and depending on the input we give it, it returns different results
# rules:
# if input is divisible by 3 return fizz
# by 5 return buzz
# by 3 and 5 return fizzbuzz
# any other number it will just return that number


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):  # or print if input % 15 == 0:
        return 'fizzbuzz'  # this if statement needs to be at the top since it is more specific and wrong results possible otherwise
    if input % 3 == 0:
        return 'FIzz'
    if input % 5 == 0:
        return 'buzz'

    return input


print(fizz_buzz(15))


print('  ')

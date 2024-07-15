print('  \n   ')


# exercise: you have some text and you write a program to find the most repeated character in the text
sentence = 'This is a common interview question. Also, today is a sunny day so stay hydrated!'
# (for each character store this and compare it to if you already have it)

# VERSION 1: LIST

all_characters = list(sentence.lower())
print(all_characters)
all_letters = [i for i in all_characters if i !=
               ' ' and i != ',' and i != '.' and i != '!']
print(all_letters)  # with duplicates
# print(type(all_letters))

print('START HERE')

highest_count = 0
most_frequent_letter = ' '

for letter in set(all_letters):
    count = all_letters.count(letter)  # from: print(all_letters.count('s'))
    print(letter, ':', count, 'times')
    if count > highest_count:
        highest_count = count
        most_frequent_letter = letter


print(f'the letter with highest count: {
      most_frequent_letter} with {highest_count} times.')


# uniques_of_sentence = set(sentence)
# print(uniques_of_sentence)
# characters that are in the set more than once so repeated, loop over them until

# VERSION 2: DICTIONARY

# empty dict so you can iterate over it and get each character and update its frequency
character_frequency = {}
for character in sentence:  # create a dict with character as key and frequency as value
    if character in character_frequency:
        character_frequency[character] += 1  # increment frequency
    else:
        character_frequency[character] = 1  # add it to dict

# pprint(character_frequency, width=1) #pprint print dicts nicer
# you cant sort dictionaries as they are unorderes collections
# so pull out items of dictionary and put into list for sorting
# so each keyvalue pair convert to tuple and put in list and then you can sort the list of tuples

character_frequency_sorted = sorted(  # use sorted function, takes iterable in this case character_frequence.items()
    character_frequency.items(),  # this returns all keyvalue pairs as tuples
    # how to sort it: pass key and set to lambda which takes a kv pair and returns a value of kv[1] so second item in tuple (so frequency of charcter)
    key=lambda keyvalue: keyvalue[1],
    reverse=True)  # reverse so highest count is start of the list

print(character_frequency_sorted[0])


print('  \n   ')

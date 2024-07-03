from pprint import pprint  # for prettier dictionary printing
print('  \n   ')


# exercise: you have some text and you write a program to find the most repeated character in the text
sentence = 'This is a common interview question. Also, today is a sunny day so stay hydrated!'


# Solution 1: list version (later dictionary version)
all_characters = [*sentence.lower()]  # create list with unpacking operator
all_letters = [i for i in all_characters if i !=
               ' ' and i != ',' and i != '.' and i != '!']  # with duplicates

highest_count = 0
most_frequent_letter = ' '

for letter in set(all_letters):
    count = all_letters.count(letter)
    # print(letter, ':', count, 'times')
    if count > highest_count:
        highest_count = count
        most_frequent_letter = letter

print(f'the letter with highest count: {
      most_frequent_letter} with {highest_count} times.')


# Solution 2: dictionary
character_frequency = {}
for character in sentence:  # create a dict with character as key and frequency as value
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1

character_frequency_sorted = sorted(
    character_frequency.items(),  # this returns all keyvalue pairs as tuples
    key=lambda keyvalue: keyvalue[1],
    reverse=True)

print(character_frequency_sorted[0])


print('  \n   ')

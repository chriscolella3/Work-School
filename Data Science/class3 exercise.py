letters = ['a', 'b', 'c', 'd', 'd', 'a', 'b', 'c', 'a']
letter_count = {}
for i in letters:
       if i not in letter_count:
        letter_count[i] = 1
else:
        letter_count[i] += 1

#print (letter_count)
# len(value) returns length of string
strings = ['a', 'as', 'ba', 'chicken']

print([i.upper() for i in strings if len(i) > 2])

numbers = [2, 5, 6, 7]

#pandas is a popular module to read data


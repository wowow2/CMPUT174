# q2.py

# open file, readlines then set up 2 empty lists
file = open('words.txt', 'r')
f = file.readlines()
word_list = []
counts = []

# iterate,strip, split each line and put each word in a list.
for i in range(len(f)):
    line_list = f[i].rstrip().split()
    for j in range(len(line_list)):
        word_list.append(line_list[j])

# make a dictionary from word_list then make it back into a list, remember the code is "dict.fromkeys(list))"
word_key = list(dict.fromkeys(word_list))

# go through they key list and iterate through word list to count up numbers and put counts in a ist
for i in range(len(word_key)):
    n = 0
    for j in range(len(word_list)):
        if word_key[i] == word_list[j]:
            n += 1
    counts.append(n)

max_count = max(counts)
min_count = min(counts)

# iterate through counts and use parallel lists to put out an output
for i in range(len(counts)):
    if counts[i] == max_count:
        print(f'{word_key[i]} {counts[i]}')
        break
for i in range(len(counts)):
    if counts[i] == min_count:
        print(f'{word_key[i]} {counts[i]}')
        break







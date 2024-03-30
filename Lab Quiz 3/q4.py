file = open('letter_scores.txt','r')
contents = file.readlines()
file.close()

scores_dict = {}
score = 0

for i in range(len(contents)):
    contents[i] = contents[i].rstrip().split()
    for j in range(len(contents[i])):
        scores_dict[contents[i][0]] = contents[i][1]

word = list(input(''))

for i in range(len(word)):
    try:
        score += int(scores_dict[word[i]])
    except KeyError:
        pass

print(score)
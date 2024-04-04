file = open('letter_scores.txt','r')
contents = file.readlines()
file.close()

scores_dict = {}
score = 0

for i in range(len(contents)):
    contents[i] = contents[i].rstrip().split() # removes /n and splits each line into letter and score value
    for j in range(len(contents[i])):
        scores_dict[contents[i][0]] = contents[i][1] #add key/value pairs to dictionary as letter: score

word = list(input('')) # make word input into a list

for i in range(len(word)):
    if word[i] in scores_dict:
        score += int(scores_dict[word[i]])

print(score)